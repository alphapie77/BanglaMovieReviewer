import React, { useState, useEffect } from 'react';
import { Send, ChevronDown } from 'lucide-react';
import { getModels } from '../services/api';
import './AnalyzerForm.css';

const AnalyzerForm = ({ onAnalyze, loading }) => {
  const [reviewText, setReviewText] = useState('');
  const [selectedModel, setSelectedModel] = useState('BanglaBERT');
  const [models, setModels] = useState(['BanglaBERT']);
  const [loadingModels, setLoadingModels] = useState(true);
  const [dropdownOpen, setDropdownOpen] = useState(false);

  useEffect(() => {
    getModels()
      .then(data => {
        if (data && data.models && Array.isArray(data.models)) {
          setModels(data.models);
          if (data.models.length > 0 && !data.models.includes(selectedModel)) {
            setSelectedModel(data.models[0]);
          }
        }
      })
      .catch(err => {
        console.error('Failed to load models:', err);
        setModels(['BanglaBERT', 'mBERT']);
      })
      .finally(() => setLoadingModels(false));
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Close dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownOpen && !event.target.closest('.custom-dropdown')) {
        setDropdownOpen(false);
      }
    };
    
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, [dropdownOpen]);

  const getModelIcon = (modelName) => {
    const icons = {
      'BanglaBERT': '🇧🇩',
      'mBERT': '🌍',
      'CNN': '🧠',
      'Masked_LSTM': '🔄',
      'LightGBM': '⚡',
      'Logistic_Regression': '📊'
    };
    return icons[modelName] || '🤖';
  };

  const handleModelSelect = (model) => {
    setSelectedModel(model);
    setDropdownOpen(false);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const trimmedText = reviewText.trim();
    if (trimmedText && trimmedText.length <= 5000) {
      onAnalyze(trimmedText, selectedModel);
    }
  };

  const isTextTooLong = reviewText.length > 5000;

  const examples = [
    'সিনেমাটা অসাধারণ ছিল! অভিনয় এবং গান দুটোই চমৎকার।',
    'একদম বাজে সিনেমা। সময় নষ্ট ছাড়া কিছুই না।',
    'সিনেমাটা ভালো তবে শেষটা একটু দুর্বল ছিল।'
  ];

  return (
    <div className="analyzer-form">
      <form onSubmit={handleSubmit}>
        <div className="model-selector">
          <label className="model-label">
            <span className="label-icon">🤖</span>
            মডেল নির্বাচন করুন
            <span className="model-count">({models.length} টি মডেল)</span>
          </label>
          
          <div className="custom-dropdown">
            <button
              type="button"
              className="dropdown-trigger"
              onClick={() => setDropdownOpen(!dropdownOpen)}
              disabled={loading || loadingModels}
            >
              <span className="model-icon">{getModelIcon(selectedModel)}</span>
              <span className="selected-model">{selectedModel}</span>
              <ChevronDown 
                size={20} 
                className={`dropdown-icon ${dropdownOpen ? 'open' : ''}`}
              />
            </button>
            
            {dropdownOpen && (
              <div className="dropdown-menu">
                {models.map(model => (
                  <button
                    key={model}
                    type="button"
                    className={`dropdown-item ${selectedModel === model ? 'active' : ''}`}
                    onClick={() => handleModelSelect(model)}
                  >
                    <span className="dropdown-item-content">
                      <span className="dropdown-item-icon">{getModelIcon(model)}</span>
                      <span className="dropdown-item-text">{model}</span>
                    </span>
                    {selectedModel === model && <span className="check-icon">✓</span>}
                  </button>
                ))}
              </div>
            )}
          </div>
        </div>
        <textarea
          value={reviewText}
          onChange={(e) => setReviewText(e.target.value)}
          placeholder="আপনার সিনেমার রিভিউ বাংলায় লিখুন..."
          rows="6"
          disabled={loading}
          maxLength={5000}
        />
        {isTextTooLong && <p className="error-text">টেক্সট অনেক বড় (সর্বোচ্চ ৫০০০ অক্ষর)</p>}
        <p className="char-count">{reviewText.length}/5000</p>
        <button type="submit" disabled={loading || !reviewText.trim() || isTextTooLong}>
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
