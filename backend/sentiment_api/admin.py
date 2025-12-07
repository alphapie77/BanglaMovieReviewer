from django.contrib import admin
from .models import SentimentAnalysis

@admin.register(SentimentAnalysis)
class SentimentAnalysisAdmin(admin.ModelAdmin):
    list_display = ['id', 'sentiment', 'confidence', 'created_at']
    list_filter = ['sentiment', 'created_at']
    search_fields = ['review_text']
    readonly_fields = ['created_at']
