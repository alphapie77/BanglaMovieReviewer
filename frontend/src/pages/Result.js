import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { ArrowLeft, Smile, Frown, Meh } from 'lucide-react';
import { PieChart, Pie, Cell, BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';
import './Result.css';

function Result() {
  const location = useLocation();
  const navigate = useNavigate();
  const result = location.state?.result;

  if (!result) {
    navigate('/analyzer');
    return null;
  }

  const getSentimentIcon = () => {
    switch (result.sentiment) {
      case 'Positive': return <Smile size={60} />;
      case 'Negative': return <Frown size={60} />;
      default: return <Meh size={60} />;
    }
  };

  const getSentimentColor = () => {
    switch (result.sentiment) {
      case 'Positive': return '#10b981';
      case 'Negative': return '#ef4444';
      default: return '#f59e0b';
    }
  };

  const pieData = [
    { name: result.sentiment, value: result.confidence },
    { name: 'অন্যান্য', value: 100 - result.confidence }
  ];

  const barData = result.word_importance?.slice(0, 8).map(item => ({
    word: item.word,
    score: Math.abs(item.score * 100),
    fill: item.score > 0 ? '#10b981' : '#ef4444'
  }));

  return (
    <div className="result-page">
      <div className="result-container">
        <button className="back-button" onClick={() => navigate('/analyzer')}>
          <ArrowLeft size={20} />
          ফিরে যান
        </button>

        <div className="result-header">
          <div className="sentiment-icon" style={{ color: getSentimentColor() }}>
            {getSentimentIcon()}
          </div>
          <div>
            <h1>{result.sentiment}</h1>
            <p className="confidence-text">{result.confidence}% নিশ্চিত</p>
          </div>
        </div>

        <div className="charts-grid">
          <div className="chart-card pie-chart-card">
            <h3>নিশ্চয়তা</h3>
            <div className="pie-chart-wrapper">
              <ResponsiveContainer width="100%" height={220}>
                <PieChart>
                  <Pie
                    data={pieData}
                    cx="50%"
                    cy="50%"
                    innerRadius={65}
                    outerRadius={90}
                    paddingAngle={3}
                    dataKey="value"
                    strokeWidth={2}
                    stroke="rgba(255,255,255,0.1)"
                  >
                    <Cell fill={getSentimentColor()} />
                    <Cell fill="rgba(255, 255, 255, 0.1)" />
                  </Pie>
                  <Tooltip 
                    formatter={(value) => `${value.toFixed(1)}%`}
                    contentStyle={{ 
                      background: 'rgba(255, 255, 255, 0.95)',
                      backdropFilter: 'blur(10px)',
                      WebkitBackdropFilter: 'blur(10px)',
                      border: '1px solid rgba(0, 0, 0, 0.1)', 
                      borderRadius: '8px',
                      color: '#1f2937',
                      fontWeight: '600',
                      padding: '6px 12px',
                      boxShadow: '0 4px 12px rgba(0, 0, 0, 0.15)',
                      fontSize: '12px'
                    }}
                    wrapperStyle={{ zIndex: 1000 }}
                    coordinate={{ x: 0, y: 0 }}
                    position={{ x: 15, y: -10 }}
                  />
                </PieChart>
              </ResponsiveContainer>
              <div className="pie-center-text" style={{ color: getSentimentColor() }}>
                <div className="pie-percentage">{result.confidence}%</div>
                <div className="pie-label">{result.sentiment}</div>
              </div>
            </div>
          </div>

          <div className="chart-card bar-chart-card">
            <h3>শব্দের গুরুত্ব</h3>
            <ResponsiveContainer width="100%" height={220}>
              <BarChart data={barData}>
                <XAxis 
                  dataKey="word" 
                  stroke="rgba(255,255,255,0.7)" 
                  fontSize={13}
                  fontWeight="500"
                />
                <YAxis 
                  stroke="rgba(255,255,255,0.7)" 
                  fontSize={12} 
                />
                <Tooltip 
                  formatter={(value) => `${value.toFixed(1)}%`}
                  labelFormatter={(label) => label}
                  contentStyle={{ 
                    background: 'rgba(255, 255, 255, 0.95)',
                    backdropFilter: 'blur(10px)',
                    WebkitBackdropFilter: 'blur(10px)',
                    border: '1px solid rgba(0, 0, 0, 0.1)', 
                    borderRadius: '8px',
                    color: '#1f2937',
                    fontWeight: '600',
                    padding: '8px 12px',
                    boxShadow: '0 4px 12px rgba(0, 0, 0, 0.15)',
                    fontSize: '12px'
                  }}
                  labelStyle={{ color: '#6b7280', fontWeight: '600', marginBottom: '2px', fontSize: '11px' }}
                  cursor={{ fill: 'rgba(255,255,255,0.05)' }}
                  wrapperStyle={{ zIndex: 1000 }}
                  coordinate={{ x: 0, y: 0 }}
                  position={{ x: 15, y: -10 }}
                />
                <Bar 
                  dataKey="score" 
                  radius={[8, 8, 0, 0]}
                  onMouseEnter={(data, index, e) => {
                    e.target.style.filter = 'brightness(1.2)';
                  }}
                  onMouseLeave={(data, index, e) => {
                    e.target.style.filter = 'brightness(1)';
                  }}
                >
                  {barData?.map((entry, index) => (
                    <Cell 
                      key={`cell-${index}`} 
                      fill={entry.fill}
                      className="bar-cell"
                    />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="word-visualization-card">
          <h3>শব্দ বিশ্লেষণ</h3>
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
      </div>
    </div>
  );
}

export default Result;
