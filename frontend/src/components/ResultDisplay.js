import React from 'react';
import { Smile, Frown, Meh, TrendingUp } from 'lucide-react';
import './ResultDisplay.css';

const ResultDisplay = ({ result }) => {
  if (!result) return null;

  const getSentimentIcon = () => {
    switch (result.sentiment) {
      case 'Positive': return <Smile size={32} />;
      case 'Negative': return <Frown size={32} />;
      default: return <Meh size={32} />;
    }
  };

  const getSentimentColor = () => {
    switch (result.sentiment) {
      case 'Positive': return '#10b981';
      case 'Negative': return '#ef4444';
      default: return '#f59e0b';
    }
  };

  return (
    <div className="result-display">
      <div className="sentiment-card" style={{ borderColor: getSentimentColor() }}>
        <div className="sentiment-icon" style={{ color: getSentimentColor() }}>
          {getSentimentIcon()}
        </div>
        <div className="sentiment-info">
          <h3>{result.sentiment}</h3>
          <div className="confidence">
            <TrendingUp size={16} />
            <span>{result.confidence}% নিশ্চিত</span>
          </div>
        </div>
      </div>

      <div className="word-visualization">
        <h4>শব্দ বিশ্লেষণ</h4>
        <div className="colored-words">
          {result.colored_html?.map((item, idx) => (
            <span
              key={idx}
              className="word-badge"
              style={{ backgroundColor: item.color }}
              title={`${item.effect}: ${item.score}`}
            >
              {item.word}
            </span>
          ))}
        </div>
        <div className="legend">
          <div className="legend-item">
            <span className="legend-color positive"></span>
            <span>ইতিবাচক প্রভাব</span>
          </div>
          <div className="legend-item">
            <span className="legend-color negative"></span>
            <span>নেতিবাচক প্রভাব</span>
          </div>
          <div className="legend-item">
            <span className="legend-color neutral"></span>
            <span>নিরপেক্ষ</span>
          </div>
        </div>
      </div>

      <div className="word-importance">
        <h4>গুরুত্বপূর্ণ শব্দসমূহ</h4>
        <div className="importance-list">
          {result.word_importance?.slice(0, 10).map((item, idx) => (
            <div key={idx} className="importance-item">
              <span className="word">{item.word}</span>
              <div className="score-bar">
                <div
                  className="score-fill"
                  style={{
                    width: `${Math.abs(item.score) * 100}%`,
                    backgroundColor: item.score > 0 ? '#10b981' : '#ef4444'
                  }}
                ></div>
              </div>
              <span className="score">{item.score.toFixed(3)}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default ResultDisplay;
