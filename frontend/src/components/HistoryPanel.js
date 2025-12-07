import React from 'react';
import { Clock, Smile, Frown, Meh } from 'lucide-react';
import './HistoryPanel.css';

const HistoryPanel = ({ history }) => {
  const getSentimentIcon = (sentiment) => {
    switch (sentiment) {
      case 'Positive': return <Smile size={16} />;
      case 'Negative': return <Frown size={16} />;
      default: return <Meh size={16} />;
    }
  };

  const getSentimentColor = (sentiment) => {
    switch (sentiment) {
      case 'Positive': return '#10b981';
      case 'Negative': return '#ef4444';
      default: return '#f59e0b';
    }
  };

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleString('bn-BD', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  if (!history || history.length === 0) {
    return (
      <div className="history-panel">
        <h3><Clock size={20} /> বিশ্লেষণের ইতিহাস</h3>
        <p className="empty-state">এখনো কোনো বিশ্লেষণ নেই</p>
      </div>
    );
  }

  return (
    <div className="history-panel">
      <h3><Clock size={20} /> বিশ্লেষণের ইতিহাস</h3>
      <div className="history-list">
        {history.map((item) => (
          <div key={item.id} className="history-item">
            <div className="history-header">
              <span
                className="sentiment-badge"
                style={{ backgroundColor: getSentimentColor(item.sentiment) }}
              >
                {getSentimentIcon(item.sentiment)}
                {item.sentiment}
              </span>
              <span className="confidence">{item.confidence}%</span>
            </div>
            <p className="review-text">{item.review_text}</p>
            <span className="timestamp">{formatDate(item.created_at)}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default HistoryPanel;
