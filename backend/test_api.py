# -*- coding: utf-8 -*-
import requests
import json
import sys
import io

# Fix encoding for Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

API_URL = "http://localhost:8000/api/sentiment/analyze/"

test_review = "এই সিনেমাটি অসাধারণ ছিল। অভিনয় এবং গল্প দুটোই চমৎকার।"

print("Testing Sentiment Analysis API...")
print(f"Review: {test_review}\n")

try:
    response = requests.post(
        API_URL,
        json={"review_text": test_review},
        timeout=30
    )
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print("\n✓ Success!")
        print(f"Sentiment: {data['sentiment']}")
        print(f"Confidence: {data['confidence']}%")
        print(f"Words analyzed: {len(data['word_importance'])}")
    else:
        print(f"\n✗ Error: {response.text}")
        
except requests.exceptions.ConnectionError:
    print("\n✗ Connection Error: Backend server is not running!")
    print("Please start the backend server with: python manage.py runserver")
except Exception as e:
    print(f"\n✗ Error: {str(e)}")
