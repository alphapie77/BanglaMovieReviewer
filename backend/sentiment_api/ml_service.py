import torch
import numpy as np
from transformers import pipeline
from lime.lime_text import LimeTextExplainer
import warnings
warnings.filterwarnings('ignore')

class SentimentAnalyzer:
    def __init__(self):
        self.model = None
        self.explainer = None
        self._initialized = False
    
    def _initialize(self):
        if self._initialized:
            return
        
        try:
            print("[INFO] Loading ML model...")
            # Use multilingual BERT - supports 104 languages including Bangla
            self.model = pipeline(
                "sentiment-analysis",
                model="nlptown/bert-base-multilingual-uncased-sentiment",
                device=-1
            )
            self.explainer = LimeTextExplainer(
                class_names=["Negative", "Neutral", "Positive"],
                split_expression=lambda x: x.split()
            )
            self._initialized = True
            print("[SUCCESS] Model loaded successfully!")
        except Exception as e:
            print(f"[ERROR] Model load failed: {str(e)}")
            import traceback
            traceback.print_exc()
            raise
    
    def predict_sentiment(self, text):
        self._initialize()
        
        # Negative keywords for better Bangla detection
        negative_words = ['খারাপ', 'বিরক্তিকর', 'দুর্বল', 'বাজে', 'নষ্ট', 'ভয়ানক', 'জোর করা', 'bad', 'worst', 'terrible', 'boring', 'waste']
        positive_words = ['ভালো', 'সুন্দর', 'অসাধারণ', 'চমৎকার', 'দারুণ', 'মজার', 'good', 'great', 'excellent', 'amazing', 'wonderful']
        
        text_lower = text.lower()
        neg_count = sum(1 for word in negative_words if word in text_lower)
        pos_count = sum(1 for word in positive_words if word in text_lower)
        
        # Get model prediction
        result = self.model(text)[0]
        label = result['label']
        score = result['score']
        
        # Convert star rating to sentiment with confidence consideration
        if '5 star' in label:
            model_sentiment = "Positive"
        elif '4 star' in label:
            model_sentiment = "Positive" if score > 0.5 else "Neutral"
        elif '3 star' in label:
            model_sentiment = "Neutral"
        elif '2 star' in label:
            model_sentiment = "Negative" if score > 0.5 else "Neutral"
        elif '1 star' in label:
            model_sentiment = "Negative"
        else:
            model_sentiment = "Neutral"
        
        # Calculate base confidence
        base_confidence = score * 100
        
        # Keyword-based override (strong signal)
        if neg_count > pos_count and neg_count >= 2:
            return "Negative", min(70 + neg_count * 10, 95)
        elif pos_count > neg_count and pos_count >= 2:
            return "Positive", min(70 + pos_count * 10, 95)
        
        # Use model prediction with confidence thresholds
        if model_sentiment == "Positive":
            confidence = max(base_confidence, 70)  # Boost positive to 70+
            return "Positive", min(confidence, 99)
        elif model_sentiment == "Negative":
            confidence = min(base_confidence, 45)  # Cap negative at 45
            return "Negative", max(confidence, 30)
        else:  # Neutral
            confidence = base_confidence
            if confidence < 46:
                confidence = 46
            elif confidence > 69:
                confidence = 69
            return "Neutral", confidence
    
    def predict_for_lime(self, texts):
        results = []
        for text in texts:
            try:
                pred = self.model(text)[0]
                label = pred['label']
                score = pred['score']
                
                # Map star ratings to [negative, neutral, positive] probabilities
                if '5 star' in label:
                    probs = [0.05, 0.05, 0.90]
                elif '4 star' in label:
                    probs = [0.10, 0.20, 0.70]
                elif '3 star' in label:
                    probs = [0.25, 0.50, 0.25]
                elif '2 star' in label:
                    probs = [0.70, 0.20, 0.10]
                elif '1 star' in label:
                    probs = [0.90, 0.05, 0.05]
                else:
                    probs = [0.33, 0.34, 0.33]
                
                results.append(probs)
            except:
                results.append([0.33, 0.34, 0.33])
        
        return np.array(results)
    
    def get_word_importance(self, text, num_words=10):
        self._initialize()
        exp = self.explainer.explain_instance(
            text,
            self.predict_for_lime,
            num_features=num_words,
            num_samples=100,
            labels=(0, 1, 2)
        )
        
        pred_probs = self.predict_for_lime([text])[0]
        pred_class = int(np.argmax(pred_probs))
        
        return exp.as_list(label=pred_class)
    
    def create_colored_html(self, text, word_scores):
        score_dict = {word: score for word, score in word_scores}
        words = text.split()
        
        html_parts = []
        for word in words:
            score = score_dict.get(word, 0)
            
            if score > 0.05:
                color = f'rgba(0, 200, 0, {min(score*3, 0.7)})'
                effect = 'positive'
            elif score < -0.05:
                color = f'rgba(255, 0, 0, {min(abs(score)*3, 0.7)})'
                effect = 'negative'
            else:
                color = 'rgba(200, 200, 200, 0.2)'
                effect = 'neutral'
            
            html_parts.append({
                'word': word,
                'score': round(score, 3),
                'color': color,
                'effect': effect
            })
        
        return html_parts
    
    def analyze(self, text):
        if not text or len(text.strip()) == 0:
            raise ValueError("Review text cannot be empty")
        
        try:
            sentiment, confidence = self.predict_sentiment(text)
            word_scores = self.get_word_importance(text)
            colored_html = self.create_colored_html(text, word_scores)
            
            return {
                'sentiment': sentiment,
                'confidence': round(confidence, 2),
                'word_importance': [{'word': w, 'score': round(s, 3)} for w, s in word_scores],
                'colored_html': colored_html
            }
        except Exception as e:
            print(f"ML Analysis Error: {str(e)}")
            raise Exception(f"Model processing failed: {str(e)}")
