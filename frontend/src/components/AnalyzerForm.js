import React, { useState } from 'react';
import { Send } from 'lucide-react';
import './AnalyzerForm.css';

const AnalyzerForm = ({ onAnalyze, loading }) => {
  const [reviewText, setReviewText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (reviewText.trim()) {
      onAnalyze(reviewText);
    }
  };

  const examples = [
    'সিনেমাটা অসাধারণ ছিল! অভিনয় এবং গান দুটোই চমৎকার।',
    'একদম বাজে সিনেমা। সময় নষ্ট ছাড়া কিছুই না।',
    'সিনেমাটা ভালো তবে শেষটা একটু দুর্বল ছিল।'
  ];

  return (
    <div className="analyzer-form">
      <form onSubmit={handleSubmit}>
        <textarea
          value={reviewText}
          onChange={(e) => setReviewText(e.target.value)}
          placeholder="আপনার সিনেমার রিভিউ বাংলায় লিখুন..."
          rows="6"
          disabled={loading}
        />
        <button type="submit" disabled={loading || !reviewText.trim()}>
          {loading ? 'বিশ্লেষণ করা হচ্ছে...' : 'বিশ্লেষণ করুন'}
          <Send size={18} />
        </button>
      </form>
      
      <div className="examples">
        <p>উদাহরণ:</p>
        {examples.map((example, idx) => (
          <button
            key={idx}
            className="example-btn"
            onClick={() => setReviewText(example)}
            disabled={loading}
          >
            {example}
          </button>
        ))}
      </div>
    </div>
  );
};

export default AnalyzerForm;
