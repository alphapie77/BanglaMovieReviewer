import torch
import numpy as np
import os
import sys
import joblib
import re
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from lime.lime_text import LimeTextExplainer
from huggingface_hub import hf_hub_download
import warnings
warnings.filterwarnings('ignore')

# Fix Unicode print errors on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE_MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '..', 'best2_models_per_family')

MODEL_CONFIGS = {
    # Transformer models - Load directly from Hugging Face
    'BanglaBERT': {
        'path': 'shksabbir7/bangla-movie-sentiment-banglabert',
        'type': 'transformer'
    },
    'mBERT': {
        'path': 'shksabbir7/bangla-movie-sentiment-mbert',
        'type': 'transformer'
    },
    
    # Deep Learning models - Download from Hugging Face
    'CNN': {
        'path': 'shksabbir7/bangla-movie-sentiment-cnn',
        'type': 'keras',
        'file': 'CNN_best.keras'
    },
    'Masked_LSTM': {
        'path': 'shksabbir7/bangla-movie-sentiment-lstm',
        'type': 'keras',
        'file': 'LSTM_masked_best.keras'
    },
    
    # Classical ML models - Download from Hugging Face
    'LightGBM': {
        'path': 'shksabbir7/bangla-movie-sentiment-lightgbm',
        'type': 'sklearn',
        'file': 'LightGBM_pipeline.joblib'
    },
    'Logistic_Regression': {
        'path': 'shksabbir7/bangla-movie-sentiment-logreg',
        'type': 'sklearn',
        'file': 'Logistic_Regression_pipeline.joblib'
    }
}

class SentimentAnalyzer:
    def __init__(self, model_name='BanglaBERT'):
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
        self.keras_tokenizer = None
        self.explainer = None
        self._initialized = False
        # Different max lengths for different models
        self.max_lengths = {
            'CNN': 160,
            'Masked_LSTM': 160,
            'default': 100
        }
    
    def _initialize(self):
        if self._initialized:
            return
        
        try:
            print(f"[INFO] Loading {self.model_name} model...")
            config = MODEL_CONFIGS[self.model_name]
            
            if config['type'] == 'transformer':
                self.tokenizer = AutoTokenizer.from_pretrained(config['path'])
                model = AutoModelForSequenceClassification.from_pretrained(config['path'])
                self.model = pipeline('sentiment-analysis', model=model, tokenizer=self.tokenizer, device=-1)
            elif config['type'] == 'keras':
                # Download Keras model from Hugging Face
                model_path = hf_hub_download(
                    repo_id=config['path'],
                    filename=config['file']
                )
                self.model = keras.models.load_model(model_path)
                # Create a simple tokenizer for Keras models
                self.keras_tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>')
                # Build vocabulary with common Bangla words
                sample_texts = [
                    'ভালো সুন্দর অসাধারণ চমৎকার দারুণ মজার',
                    'খারাপ বিরক্তিকর দুর্বল বাজে নষ্ট ভয়ানক',
                    'সিনেমা ছবি মুভি ফিল্ম গান নাচ অভিনয়'
                ]
                self.keras_tokenizer.fit_on_texts(sample_texts)
            elif config['type'] == 'sklearn':
                # Download sklearn model from Hugging Face
                model_path = hf_hub_download(
                    repo_id=config['path'],
                    filename=config['file']
                )
                self.model = joblib.load(model_path)
            
            self.explainer = LimeTextExplainer(
                class_names=["Negative", "Neutral", "Positive"],
                split_expression=lambda x: x.split()
            )
            self._initialized = True
            print(f"[SUCCESS] {self.model_name} loaded successfully!")
        except Exception as e:
            print(f"[ERROR] Model load failed: {str(e)}")
            import traceback
            traceback.print_exc()
            raise
    
    def _preprocess_for_keras(self, text):
        """Preprocess text for Keras models (CNN, LSTM)"""
        # Get max length for this model
        max_length = self.max_lengths.get(self.model_name, self.max_lengths['default'])
        # Tokenize and pad
        sequences = self.keras_tokenizer.texts_to_sequences([text])
        padded = pad_sequences(sequences, maxlen=max_length, padding='post', truncating='post')
        return padded
    
    def predict_sentiment(self, text):
        self._initialize()
        
        if not text or not isinstance(text, str):
            raise ValueError("Text must be a non-empty string")
        
        config = MODEL_CONFIGS[self.model_name]
        
        try:
            if config['type'] == 'transformer':
                result = self.model(text[:512])[0]  # Truncate long text
                label_map = {'LABEL_0': 'Negative', 'LABEL_1': 'Neutral', 'LABEL_2': 'Positive'}
                sentiment = label_map.get(result['label'], result['label'])
                confidence = result['score'] * 100
                return sentiment, confidence
            elif config['type'] in ['keras', 'sklearn']:
                if config['type'] == 'keras':
                    # Preprocess for Keras models
                    try:
                        processed_text = self._preprocess_for_keras(text)
                        prediction = self.model.predict(processed_text, verbose=0)[0]
                    except Exception as keras_error:
                        # Fallback: return neutral prediction if preprocessing fails
                        print(f"Keras preprocessing error: {keras_error}")
                        return 'Neutral', 50.0
                else:
                    # Sklearn models handle text directly
                    prediction = self.model.predict([text])[0]
                
                # Handle different prediction formats
                if isinstance(prediction, (list, np.ndarray)):
                    if len(prediction) == 3:
                        labels = ['Negative', 'Neutral', 'Positive']
                        idx = int(np.argmax(prediction))
                        confidence = float(prediction[idx]) * 100
                        return labels[idx], confidence
                    elif len(prediction) == 1:
                        # Binary classification
                        prob = float(prediction[0])
                        if prob > 0.5:
                            return 'Positive', prob * 100
                        else:
                            return 'Negative', (1 - prob) * 100
                else:
                    # Single value prediction
                    prob = float(prediction)
                    if prob > 0.5:
                        return 'Positive', prob * 100
                    else:
                        return 'Negative', (1 - prob) * 100
        except Exception as e:
            print(f"Prediction error: {str(e)}")
            raise ValueError(f"Failed to predict sentiment: {str(e)}")
    
    def predict_for_lime(self, texts):
        results = []
        config = MODEL_CONFIGS[self.model_name]
        
        for text in texts:
            try:
                if not text or not isinstance(text, str) or len(text.strip()) == 0:
                    results.append([0.33, 0.34, 0.33])
                    continue
                    
                if config['type'] == 'transformer':
                    pred = self.model(text[:512])[0]
                    label = pred['label']
                    score = pred['score']
                    # Create probability distribution based on confidence
                    if label == 'LABEL_0':  # Negative
                        probs = [score, (1-score)/2, (1-score)/2]
                    elif label == 'LABEL_1':  # Neutral
                        probs = [(1-score)/2, score, (1-score)/2]
                    else:  # Positive
                        probs = [(1-score)/2, (1-score)/2, score]
                elif config['type'] == 'keras':
                    processed_text = self._preprocess_for_keras(text)
                    pred = self.model.predict(processed_text, verbose=0)[0]
                    if isinstance(pred, (list, np.ndarray)):
                        if len(pred) == 3:
                            # Normalize to ensure sum = 1
                            probs = np.array(pred)
                            probs = probs / probs.sum()
                            probs = probs.tolist()
                        elif len(pred) == 1:
                            prob = float(pred[0])
                            # Binary: negative vs positive
                            probs = [1-prob, 0.0, prob]
                        else:
                            probs = [0.33, 0.34, 0.33]
                    else:
                        prob = float(pred)
                        probs = [1-prob, 0.0, prob]
                else:  # sklearn
                    # Get probability predictions
                    if hasattr(self.model, 'predict_proba'):
                        pred = self.model.predict_proba([text])[0]
                        if len(pred) == 3:
                            probs = pred.tolist()
                        elif len(pred) == 2:
                            # Binary classification: convert to 3-class
                            probs = [pred[0], 0.0, pred[1]]
                        else:
                            probs = [0.33, 0.34, 0.33]
                    else:
                        # Fallback to predict
                        pred = self.model.predict([text])[0]
                        if isinstance(pred, (int, np.integer)):
                            # Class label returned
                            probs = [0.0, 0.0, 0.0]
                            probs[int(pred)] = 1.0
                        else:
                            probs = [0.33, 0.34, 0.33]
                
                results.append(probs)
            except Exception as e:
                print(f"LIME prediction error for '{text[:50]}...': {str(e)}")
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
        if not text:
            return []
            
        score_dict = {word: score for word, score in word_scores if word and score is not None}
        words = text.split()
        
        html_parts = []
        for word in words:
            if not word:
                continue
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
