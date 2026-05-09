from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
import sys
from .models import SentimentAnalysis
from .serializers import SentimentAnalysisSerializer, AnalyzeRequestSerializer
from .ml_service import SentimentAnalyzer, MODEL_CONFIGS

# Fix Unicode print errors on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Cache for different model instances
analyzers = {}

def get_analyzer(model_name='BanglaBERT'):
    if model_name not in analyzers:
        analyzers[model_name] = SentimentAnalyzer(model_name)
    return analyzers[model_name]

class SentimentAnalysisViewSet(viewsets.ModelViewSet):
    queryset = SentimentAnalysis.objects.all()
    serializer_class = SentimentAnalysisSerializer
    
    @action(detail=False, methods=['get'])
    def models(self, request):
        return Response({'models': list(MODEL_CONFIGS.keys())})
    
    @action(detail=False, methods=['post'])
    def analyze(self, request):
        serializer = AnalyzeRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        review_text = serializer.validated_data['review_text']
        model_name = request.data.get('model_name', 'BanglaBERT')
        
        # Validate model name
        if not model_name or not isinstance(model_name, str):
            return Response({'error': 'Model name must be a valid string'}, status=status.HTTP_400_BAD_REQUEST)
        
        if model_name not in MODEL_CONFIGS:
            return Response({
                'error': f'Invalid model name: {model_name}',
                'available_models': list(MODEL_CONFIGS.keys())
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Validate text length
        if len(review_text) > 5000:
            return Response({'error': 'Review text too long (max 5000 characters)'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            result = get_analyzer(model_name).analyze(review_text)
            
            # Save to database
            analysis = SentimentAnalysis.objects.create(
                review_text=review_text[:1000],  # Limit DB storage
                sentiment=result['sentiment'],
                confidence=result['confidence'],
                word_importance=result['word_importance']
            )
            
            return Response({
                'id': analysis.id,
                'model_used': model_name,
                'sentiment': result['sentiment'],
                'confidence': result['confidence'],
                'word_importance': result['word_importance'],
                'colored_html': result['colored_html']
            })
        except ValueError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            print(f"Error in sentiment analysis: {error_details}")
            return Response(
                {'error': f'Analysis failed: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def history(self, request):
        analyses = self.get_queryset()[:20]
        serializer = self.get_serializer(analyses, many=True)
        return Response(serializer.data)
