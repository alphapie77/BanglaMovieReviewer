# -*- coding: utf-8 -*-
import sys
import os
import io

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Add backend to path
sys.path.insert(0, os.path.dirname(__file__))

print("Testing ML Model Loading...\n")

try:
    print("1. Importing dependencies...")
    import torch
    print("   ✓ PyTorch imported")
    
    from transformers import pipeline
    print("   ✓ Transformers imported")
    
    from lime.lime_text import LimeTextExplainer
    print("   ✓ LIME imported")
    
    print("\n2. Loading BERT model (this may take 2-5 minutes)...")
    model = pipeline(
        "sentiment-analysis",
        model="nlptown/bert-base-multilingual-uncased-sentiment",
        device=-1
    )
    print("   ✓ Model loaded successfully!")
    
    print("\n3. Testing with sample text...")
    test_text = "This movie is great"
    result = model(test_text)[0]
    print(f"   ✓ Prediction: {result['label']} (confidence: {result['score']:.2%})")
    
    print("\n✓ All tests passed! Model is working correctly.")
    print("\nYou can now run: python manage.py runserver")
    
except ImportError as e:
    print(f"\n✗ Import Error: {str(e)}")
    print("\nSolution: Install dependencies")
    print("  pip install -r requirements.txt")
    
except Exception as e:
    print(f"\n✗ Error: {str(e)}")
    print("\nPossible causes:")
    print("  1. First time download - wait for model to download (~500MB)")
    print("  2. Network issue - check internet connection")
    print("  3. Insufficient RAM - need at least 4GB free")
    print("  4. Disk space - need at least 2GB free")
