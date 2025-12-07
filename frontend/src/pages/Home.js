import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Film, Sparkles, TrendingUp, Clock } from 'lucide-react';
import './Home.css';

function Home() {
  const navigate = useNavigate();

  return (
    <div className="home">
      <div className="hero">
        <div className="hero-content">
          <Film size={80} className="hero-icon" />
          <h1>সিনেমা রিভিউ পরীক্ষক</h1>
          <p>ব্যাখ্যাযোগ্য AI সহ বাংলা সিনেমা রিভিউ মনোভাব পরীক্ষা</p>
          <button className="cta-button" onClick={() => navigate('/analyzer')}>
            <Sparkles size={20} />
            শুরু করুন
          </button>
        </div>
      </div>

      <div className="features">
        <div className="feature-card">
          <TrendingUp size={40} />
          <h3>রিয়েল-টাইম বিশ্লেষণ</h3>
          <p>AI-চালিত নির্ভুলতার সাথে তাৎক্ষণিক সেন্টিমেন্ট সনাক্তকরণ</p>
        </div>
        <div className="feature-card">
          <Sparkles size={40} />
          <h3>ব্যাখ্যাযোগ্য AI</h3>
          <p>কোন শব্দগুলো সেন্টিমেন্ট সিদ্ধান্তকে প্রভাবিত করেছে তা দেখুন</p>
        </div>
        <div className="feature-card">
          <Clock size={40} />
          <h3>ইতিহাস সংরক্ষণ</h3>
          <p>ভবিষ্যতের রেফারেন্সের জন্য সমস্ত বিশ্লেষণ স্বয়ংক্রিয়ভাবে সংরক্ষিত</p>
        </div>
      </div>
    </div>
  );
}

export default Home;
