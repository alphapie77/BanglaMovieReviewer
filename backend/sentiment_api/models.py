from django.db import models

class SentimentAnalysis(models.Model):
    review_text = models.TextField()
    sentiment = models.CharField(max_length=20)
    confidence = models.FloatField()
    word_importance = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Sentiment Analyses'
    
    def __str__(self):
        return f"{self.sentiment} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
