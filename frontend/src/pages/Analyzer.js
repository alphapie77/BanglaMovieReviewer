import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import AnalyzerForm from '../components/AnalyzerForm';
import { analyzeSentiment } from '../services/api';
import './Analyzer.css';

function Analyzer() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleAnalyze = async (reviewText) => {
    setLoading(true);
    setError(null);
    
    try {
      const data = await analyzeSentiment(reviewText);
      navigate('/result', { state: { result: data } });
    } catch (err) {
      let errorMsg = 'বিশ্লেষণে ত্রুটি হয়েছে। ';
      
      if (err.code === 'ERR_NETWORK') {
        errorMsg += 'Backend server চালু আছে কিনা পরীক্ষা করুন (http://localhost:8000)';
      } else if (err.response?.status === 500) {
        errorMsg += 'ML model load হতে সমস্যা হয়েছে। Backend logs দেখুন।';
      } else if (err.response?.data?.error) {
        errorMsg += err.response.data.error;
      } else {
        errorMsg += 'অনুগ্রহ করে আবার চেষ্টা করুন।';
      }
      
      setError(errorMsg);
      console.error('Analysis error:', err);
      setLoading(false);
    }
  };

  return (
    <div className="analyzer-page">
      <div className="analyzer-container">
        <AnalyzerForm onAnalyze={handleAnalyze} loading={loading} />
        {error && <div className="error-message">{error}</div>}
      </div>
    </div>
  );
}

export default Analyzer;
