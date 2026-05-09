"""
Automatic API Testing Script - No user input required
Run: python auto_test.py
"""

import requests
import json
import sys

BASE_URL = "http://localhost:8000/api/sentiment"

def print_header(text):
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)

def print_test(test_name):
    print(f"\n>>> {test_name}")

def test_backend_connection():
    """Check if backend is running"""
    print_test("Testing Backend Connection")
    try:
        response = requests.get(f"{BASE_URL}/models/", timeout=5)
        if response.status_code == 200:
            print("✓ Backend is running")
            return True
        else:
            print(f"✗ Backend returned status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("✗ Backend is NOT running!")
        print("  Please start backend: python manage.py runserver")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_get_models():
    """Test: Get available models"""
    print_test("Test 1: Get Available Models")
    try:
        response = requests.get(f"{BASE_URL}/models/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            models = data.get('models', [])
            print(f"✓ Status: {response.status_code}")
            print(f"✓ Models found: {len(models)}")
            print(f"  Models: {', '.join(models)}")
            
            expected_models = ['BanglaBERT', 'mBERT', 'CNN', 'Masked_LSTM', 'LightGBM', 'Logistic_Regression']
            if len(models) == 6:
                print("✓ All 6 models available")
                return True
            else:
                print(f"⚠ Expected 6 models, got {len(models)}")
                return False
        else:
            print(f"✗ Failed with status {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_valid_analysis(model_name="BanglaBERT"):
    """Test: Valid sentiment analysis"""
    print_test(f"Test 2: Valid Analysis with {model_name}")
    try:
        data = {
            "review_text": "সিনেমাটা অসাধারণ ছিল!",
            "model_name": model_name
        }
        response = requests.post(f"{BASE_URL}/analyze/", json=data, timeout=60)  # Increased timeout
        
        if response.status_code == 200:
            result = response.json()
            print(f"✓ Status: {response.status_code}")
            print(f"✓ Model Used: {result.get('model_used')}")
            print(f"✓ Sentiment: {result.get('sentiment')}")
            print(f"✓ Confidence: {result.get('confidence')}%")
            print(f"✓ Word Importance: {len(result.get('word_importance', []))} words")
            print(f"✓ Colored HTML: {len(result.get('colored_html', []))} parts")
            return True
        else:
            print(f"✗ Failed with status {response.status_code}")
            print(f"  Response: {response.text}")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_empty_text():
    """Test: Empty review text"""
    print_test("Test 3: Empty Text Validation")
    try:
        data = {
            "review_text": "",
            "model_name": "BanglaBERT"
        }
        response = requests.post(f"{BASE_URL}/analyze/", json=data, timeout=5)
        
        if response.status_code == 400:
            print(f"✓ Correctly rejected with status 400")
            print(f"  Error: {response.json()}")
            return True
        else:
            print(f"✗ Should return 400, got {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_invalid_model():
    """Test: Invalid model name"""
    print_test("Test 4: Invalid Model Name")
    try:
        data = {
            "review_text": "ভালো সিনেমা",
            "model_name": "InvalidModel"
        }
        response = requests.post(f"{BASE_URL}/analyze/", json=data, timeout=5)
        
        if response.status_code == 400:
            result = response.json()
            print(f"✓ Correctly rejected with status 400")
            print(f"  Error: {result.get('error')}")
            if 'available_models' in result:
                print(f"✓ Available models list provided")
            return True
        else:
            print(f"✗ Should return 400, got {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_long_text():
    """Test: Text exceeding 5000 characters"""
    print_test("Test 5: Long Text Validation")
    try:
        data = {
            "review_text": "অসাধারণ " * 1000,  # ~10000 chars
            "model_name": "BanglaBERT"
        }
        response = requests.post(f"{BASE_URL}/analyze/", json=data, timeout=5)
        
        if response.status_code == 400:
            print(f"✓ Correctly rejected with status 400")
            print(f"  Error: {response.json()}")
            return True
        else:
            print(f"✗ Should return 400, got {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_all_models():
    """Test: All available models"""
    print_test("Test 6: Testing All Models")
    try:
        # Get models first
        models_response = requests.get(f"{BASE_URL}/models/", timeout=5)
        if models_response.status_code != 200:
            print("✗ Could not get models list")
            return False
            
        models = models_response.json()['models']
        text = "সিনেমাটা চমৎকার ছিল"
        
        passed = 0
        failed = 0
        
        for model in models:
            print(f"\n  Testing {model}...", end=" ")
            try:
                data = {
                    "review_text": text,
                    "model_name": model
                }
                response = requests.post(f"{BASE_URL}/analyze/", json=data, timeout=60)  # Increased timeout for slow models
                
                if response.status_code == 200:
                    result = response.json()
                    print(f"✓ {result.get('sentiment')} ({result.get('confidence')}%)")
                    passed += 1
                else:
                    print(f"✗ Status {response.status_code}")
                    failed += 1
            except Exception as e:
                print(f"✗ Error: {e}")
                failed += 1
        
        print(f"\n  Results: {passed} passed, {failed} failed")
        return failed == 0
        
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_special_characters():
    """Test: Text with special characters"""
    print_test("Test 7: Special Characters")
    try:
        data = {
            "review_text": "সিনেমা!!! @#$% 😊 ভালো ছিল...",
            "model_name": "BanglaBERT"
        }
        response = requests.post(f"{BASE_URL}/analyze/", json=data, timeout=60)  # Increased timeout
        
        if response.status_code == 200:
            result = response.json()
            print(f"✓ Status: {response.status_code}")
            print(f"✓ Sentiment: {result.get('sentiment')}")
            return True
        else:
            print(f"✗ Failed with status {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def main():
    print_header("AUTOMATIC API TESTING")
    print("Testing backend at:", BASE_URL)
    
    # Check backend connection first
    if not test_backend_connection():
        print("\n" + "="*60)
        print("  TESTING ABORTED - Backend not running")
        print("="*60)
        sys.exit(1)
    
    # Run all tests
    results = []
    
    results.append(("Get Models", test_get_models()))
    results.append(("Valid Analysis", test_valid_analysis("BanglaBERT")))
    results.append(("Empty Text", test_empty_text()))
    results.append(("Invalid Model", test_invalid_model()))
    results.append(("Long Text", test_long_text()))
    results.append(("Special Characters", test_special_characters()))
    results.append(("All Models", test_all_models()))
    
    # Summary
    print_header("TEST SUMMARY")
    passed = sum(1 for _, result in results if result)
    failed = sum(1 for _, result in results if not result)
    
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{status:12} - {test_name}")
    
    print(f"\nTotal: {passed} passed, {failed} failed out of {len(results)} tests")
    
    if failed == 0:
        print("\n🎉 ALL TESTS PASSED! System is working correctly.")
    else:
        print(f"\n⚠ {failed} test(s) failed. Check errors above.")
    
    print("="*60)

if __name__ == "__main__":
    main()
