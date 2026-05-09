# API Documentation - Model Selection Feature

## Base URL
```
http://localhost:8000/api/sentiment
```

## Endpoints

### 1. Get Available Models
**GET** `/models/`

Returns list of all available models.

**Response:**
```json
{
  "models": [
    "BanglaBERT",
    "mBERT",
    "CNN",
    "Masked_LSTM",
    "LightGBM",
    "Logistic_Regression"
  ]
}
```

---

### 2. Analyze Sentiment
**POST** `/analyze/`

Analyzes sentiment of review text using selected model.

**Request Body:**
```json
{
  "review_text": "সিনেমাটা অসাধারণ ছিল!",
  "model_name": "BanglaBERT"  // Optional, defaults to "BanglaBERT"
}
```

**Success Response (200):**
```json
{
  "id": 123,
  "model_used": "BanglaBERT",
  "sentiment": "Positive",
  "confidence": 92.45,
  "word_importance": [
    {"word": "অসাধারণ", "score": 0.856},
    {"word": "ছিল", "score": 0.123}
  ],
  "colored_html": [
    {
      "word": "সিনেমাটা",
      "score": 0.045,
      "color": "rgba(200, 200, 200, 0.2)",
      "effect": "neutral"
    }
  ]
}
```

**Error Responses:**

**400 - Empty Text:**
```json
{
  "review_text": ["This field may not be blank."]
}
```

**400 - Text Too Long:**
```json
{
  "error": "Review text too long (max 5000 characters)"
}
```

**400 - Invalid Model:**
```json
{
  "error": "Invalid model name: InvalidModel",
  "available_models": ["BanglaBERT", "mBERT", "CNN", "Masked_LSTM", "LightGBM", "Logistic_Regression"]
}
```

**500 - Server Error:**
```json
{
  "error": "Analysis failed: Model processing failed"
}
```

---

### 3. Get History
**GET** `/history/`

Returns last 20 sentiment analyses.

**Response:**
```json
[
  {
    "id": 123,
    "review_text": "সিনেমাটা ভালো",
    "sentiment": "Positive",
    "confidence": 85.5,
    "word_importance": [...],
    "created_at": "2024-01-15T10:30:00Z"
  }
]
```

---

## Model Types

### Transformer Models
- **BanglaBERT**: Fine-tuned BERT for Bangla sentiment
- **mBERT**: Multilingual BERT supporting 104 languages

### Deep Learning Models
- **CNN**: Convolutional Neural Network
- **Masked_LSTM**: LSTM with masking for variable length sequences

### Classical ML Models
- **LightGBM**: Gradient boosting framework
- **Logistic_Regression**: Linear classification model

---

## Validation Rules

1. **review_text**: 
   - Required
   - Cannot be empty or whitespace only
   - Maximum 5000 characters
   - Type: string

2. **model_name**:
   - Optional (defaults to "BanglaBERT")
   - Must be one of available models
   - Type: string

---

## Edge Cases Handled

### Input Validation
✓ Empty text → 400 error
✓ Whitespace only → 400 error  
✓ Text > 5000 chars → 400 error
✓ Invalid model name → 400 error with available models list
✓ Missing model_name → Uses default "BanglaBERT"
✓ Special characters → Processed normally
✓ Mixed language text → Processed normally

### Model Processing
✓ Long text truncation (512 tokens for transformers)
✓ Different prediction formats (3-class, binary)
✓ Model loading errors → 500 error with details
✓ Prediction failures → Fallback to neutral probabilities

### Response Handling
✓ Database storage limited to 1000 chars
✓ Word importance scores rounded to 3 decimals
✓ Confidence scores rounded to 2 decimals
✓ Empty word scores filtered out

---

## Usage Examples

### JavaScript (Frontend)
```javascript
// Get models
const models = await fetch('http://localhost:8000/api/sentiment/models/')
  .then(r => r.json());

// Analyze with specific model
const result = await fetch('http://localhost:8000/api/sentiment/analyze/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    review_text: 'সিনেমাটা ভালো',
    model_name: 'BanglaBERT'
  })
}).then(r => r.json());
```

### Python
```python
import requests

# Get models
response = requests.get('http://localhost:8000/api/sentiment/models/')
models = response.json()['models']

# Analyze
data = {
    'review_text': 'সিনেমাটা অসাধারণ',
    'model_name': 'mBERT'
}
response = requests.post('http://localhost:8000/api/sentiment/analyze/', json=data)
result = response.json()
```

### cURL
```bash
# Get models
curl http://localhost:8000/api/sentiment/models/

# Analyze
curl -X POST http://localhost:8000/api/sentiment/analyze/ \
  -H "Content-Type: application/json" \
  -d '{"review_text": "সিনেমাটা ভালো", "model_name": "BanglaBERT"}'
```

---

## Testing

Run edge case tests:
```bash
cd backend
python test_edge_cases.py
```

This will test:
- Model listing
- Valid analysis
- Empty/whitespace text
- Long text
- Invalid model names
- Special characters
- Mixed languages
- All available models
- History retrieval
