# 📡 API Documentation

Base URL: `http://localhost:8000/api`

## Endpoints

### 1. Analyze Sentiment

**POST** `/sentiment/analyze/`

Analyzes the sentiment of a review text.

**Request Body:**
```json
{
  "review_text": "সিনেমাটা অসাধারণ ছিল!"
}
```

**Response:**
```json
{
  "id": 1,
  "sentiment": "Positive",
  "confidence": 85.5,
  "word_importance": [
    {"word": "অসাধারণ", "score": 0.456},
    {"word": "ছিল", "score": 0.123}
  ],
  "colored_html": [
    {
      "word": "সিনেমাটা",
      "score": 0.045,
      "color": "rgba(200, 200, 200, 0.2)",
      "effect": "neutral"
    },
    {
      "word": "অসাধারণ",
      "score": 0.456,
      "color": "rgba(0, 200, 0, 0.7)",
      "effect": "positive"
    }
  ]
}
```

**Status Codes:**
- `200 OK` - Success
- `400 Bad Request` - Invalid input
- `500 Internal Server Error` - Analysis failed

---

### 2. Get Analysis History

**GET** `/sentiment/history/`

Returns the last 20 sentiment analyses.

**Response:**
```json
[
  {
    "id": 1,
    "review_text": "সিনেমাটা অসাধারণ ছিল!",
    "sentiment": "Positive",
    "confidence": 85.5,
    "word_importance": [...],
    "created_at": "2024-01-15T10:30:00Z"
  }
]
```

---

### 3. List All Analyses

**GET** `/sentiment/`

Returns all sentiment analyses (paginated).

**Response:**
```json
{
  "count": 50,
  "next": "http://localhost:8000/api/sentiment/?page=2",
  "previous": null,
  "results": [...]
}
```

---

### 4. Get Single Analysis

**GET** `/sentiment/{id}/`

Returns a specific analysis by ID.

**Response:**
```json
{
  "id": 1,
  "review_text": "সিনেমাটা অসাধারণ ছিল!",
  "sentiment": "Positive",
  "confidence": 85.5,
  "word_importance": [...],
  "created_at": "2024-01-15T10:30:00Z"
}
```

---

## Example Usage

### Using cURL

```bash
# Analyze sentiment
curl -X POST http://localhost:8000/api/sentiment/analyze/ \
  -H "Content-Type: application/json" \
  -d '{"review_text": "সিনেমাটা অসাধারণ ছিল!"}'

# Get history
curl http://localhost:8000/api/sentiment/history/
```

### Using JavaScript (Fetch)

```javascript
// Analyze sentiment
const response = await fetch('http://localhost:8000/api/sentiment/analyze/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    review_text: 'সিনেমাটা অসাধারণ ছিল!'
  })
});
const data = await response.json();
console.log(data);
```

### Using Python (requests)

```python
import requests

# Analyze sentiment
response = requests.post(
    'http://localhost:8000/api/sentiment/analyze/',
    json={'review_text': 'সিনেমাটা অসাধারণ ছিল!'}
)
print(response.json())

# Get history
response = requests.get('http://localhost:8000/api/sentiment/history/')
print(response.json())
```

---

## Response Fields

### Sentiment Analysis Object

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Unique identifier |
| `review_text` | string | Original review text |
| `sentiment` | string | "Positive", "Negative", or "Neutral" |
| `confidence` | float | Confidence score (0-100) |
| `word_importance` | array | List of important words with scores |
| `colored_html` | array | Word-by-word visualization data |
| `created_at` | datetime | Timestamp of analysis |

### Word Importance Object

| Field | Type | Description |
|-------|------|-------------|
| `word` | string | The word |
| `score` | float | Importance score (-1 to 1) |

Positive score = makes sentiment more positive
Negative score = makes sentiment more negative

### Colored HTML Object

| Field | Type | Description |
|-------|------|-------------|
| `word` | string | The word |
| `score` | float | Importance score |
| `color` | string | RGBA color for visualization |
| `effect` | string | "positive", "negative", or "neutral" |

---

## Error Responses

### 400 Bad Request
```json
{
  "review_text": ["This field is required."]
}
```

### 500 Internal Server Error
```json
{
  "error": "Model loading failed"
}
```

---

## Rate Limiting

Currently no rate limiting. For production, consider adding:
- Django REST Framework throttling
- Redis-based rate limiting
- API key authentication

---

## CORS

CORS is enabled for:
- `http://localhost:3000`
- `http://127.0.0.1:3000`

To add more origins, edit `backend/config/settings.py`:
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://your-domain.com",
]
```
