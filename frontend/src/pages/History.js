import React, { useState, useEffect } from 'react';
import { getHistory } from '../services/api';
import HistoryPanel from '../components/HistoryPanel';
import './History.css';

function History() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadHistory();
  }, []);

  const loadHistory = async () => {
    try {
      const data = await getHistory();
      setHistory(data);
    } catch (err) {
      console.error('Failed to load history:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="history-page">
      <div className="history-container">
        <h1>বিশ্লেষণের ইতিহাস</h1>
        {loading ? (
          <p className="loading">লোড হচ্ছে...</p>
        ) : (
          <HistoryPanel history={history} />
        )}
      </div>
    </div>
  );
}

export default History;
