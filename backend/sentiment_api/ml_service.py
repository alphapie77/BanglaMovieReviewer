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
        
        # Enhanced keyword detection
        negative_words = ['খারাপ', 'বিরক্তিকর', 'দুর্বল', 'বাজে', 'নষ্ট', 'ভয়ানক', 'জোর করা', 'bad', 'worst', 'terrible', 'boring', 'waste']
        positive_words = ['ভালো', 'সুন্দর', 'অসাধারণ', 'চমৎকার', 'দারুণ', 'মজার', 'good', 'great', 'excellent', 'amazing', 'wonderful']
        neutral_words = ['মোটামুটি', 'সাধারণ', 'এভারেজ', 'মাঝামাঝি', 'ঠিক আছে', 'okay', 'average', 'normal', 'ordinary']
        
        text_lower = text.lower()
        neg_count = sum(1 for word in negative_words if word in text_lower)
        pos_count = sum(1 for word in positive_words if word in text_lower)
        neu_count = sum(1 for word in neutral_words if word in text_lower)
        
        # Get model prediction
        result = self.model(text)[0]
        label = result['label']
        score = result['score']
        
        # Map star ratings to sentiment
        star_map = {
            '5 star': ('Positive', 0.9),
            '4 star': ('Positive', 0.75),
            '3 star': ('Neutral', 0.8),
            '2 star': ('Negative', 0.75),
            '1 star': ('Negative', 0.9)
        }
        
        model_sentiment, base_multiplier = star_map.get(label, ('Neutral', 0.5))
        base_confidence = score * 100 * base_multiplier
        
        # Strong keyword override
        if neg_count >= 2 and neg_count > pos_count:
            return "Negative", min(75 + neg_count * 8, 95)
        elif pos_count >= 2 and pos_count > neg_count:
            return "Positive", min(75 + pos_count * 8, 95)
        elif neu_count >= 2 or (pos_count > 0 and neg_count > 0 and abs(pos_count - neg_count) <= 1):
            # Clear neutral indicators or mixed sentiment
            return "Neutral", min(70 + neu_count * 10, 92)
        
        # Apply realistic confidence ranges
        if model_sentiment == "Positive":
            confidence = max(base_confidence, 72)
            return "Positive", min(confidence, 98)
        elif model_sentiment == "Negative":
            confidence = max(base_confidence, 35)
            return "Negative", min(confidence, 45)
        else:  # Neutral
            confidence = max(base_confidence, 65)
            return "Neutral", min(confidence, 88)
    
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
