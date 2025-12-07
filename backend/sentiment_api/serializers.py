from rest_framework import serializers
from .models import SentimentAnalysis

class SentimentAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentimentAnalysis
        fields = ['id', 'review_text', 'sentiment', 'confidence', 'word_importance', 'created_at']
        read_only_fields = ['id', 'created_at']

class AnalyzeRequestSerializer(serializers.Serializer):
    review_text = serializers.CharField(max_length=5000)
