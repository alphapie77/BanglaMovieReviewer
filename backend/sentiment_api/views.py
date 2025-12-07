from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import SentimentAnalysis
from .serializers import SentimentAnalysisSerializer, AnalyzeRequestSerializer
from .ml_service import SentimentAnalyzer

# Lazy initialization - model loads on first request
analyzer = None

def get_analyzer():
    global analyzer
    if analyzer is None:
        analyzer = SentimentAnalyzer()
    return analyzer

class SentimentAnalysisViewSet(viewsets.ModelViewSet):
    queryset = SentimentAnalysis.objects.all()
    serializer_class = SentimentAnalysisSerializer
    
    @action(detail=False, methods=['post'])
    def analyze(self, request):
        serializer = AnalyzeRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        review_text = serializer.validated_data['review_text']
        
        try:
            result = get_analyzer().analyze(review_text)
            
            # Save to database
            analysis = SentimentAnalysis.objects.create(
                review_text=review_text,
                sentiment=result['sentiment'],
                confidence=result['confidence'],
                word_importance=result['word_importance']
            )
            
            return Response({
                'id': analysis.id,
                'sentiment': result['sentiment'],
                'confidence': result['confidence'],
                'word_importance': result['word_importance'],
                'colored_html': result['colored_html']
            })
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
