import React from 'react';
import { Brain, Target, Zap, Shield } from 'lucide-react';
import './About.css';

function About() {
  return (
    <div className="about-page">
      <div className="about-container">
        <h1>প্রকল্প সম্পর্কে</h1>
        
        <div className="about-content">
          <section className="about-section">
            <h2>এটি কী?</h2>
            <p>
              ব্যাখ্যাযোগ্য AI সহ বাংলা মুভি রিভিউ সেন্টিমেন্ট বিশ্লেষণের জন্য একটি ফুল-স্ট্যাক ওয়েব অ্যাপ্লিকেশন। 
              এই প্রকল্পটি বাংলা টেক্সট বিশ্লেষণ করতে এবং প্রতিটি প্রেডিকশনের পেছনের কারণ ব্যাখ্যা করতে উন্নত Machine Learning ব্যবহার করে।
            </p>
          </section>

          <div className="tech-grid">
            <div className="tech-card">
              <Brain size={40} />
              <h3>AI Model</h3>
              <p>নির্ভুল বাংলা সেন্টিমেন্ট সনাক্তকরণের জন্য Multilingual BERT</p>
            </div>
            <div className="tech-card">
              <Target size={40} />
              <h3>LIME Explainer</h3>
              <p>কোন শব্দগুলো AI-এর সিদ্ধান্তকে প্রভাবিত করেছে তা দেখায়</p>
            </div>
            <div className="tech-card">
              <Zap size={40} />
              <h3>রিয়েল-টাইম</h3>
              <p>Confidence Score সহ তাৎক্ষণিক বিশ্লেষণ</p>
            </div>
            <div className="tech-card">
              <Shield size={40} />
              <h3>নিরাপদ</h3>
              <p>সমস্ত ডেটা SQLite Database-এ স্থানীয়ভাবে সংরক্ষিত</p>
            </div>
          </div>

          <section className="about-section">
            <h2>Technology Stack</h2>
            <ul>
              <li><strong>Backend:</strong> Django + PyTorch + Transformers + LIME</li>
              <li><strong>Frontend:</strong> React + Axios</li>
              <li><strong>Database:</strong> SQLite</li>
              <li><strong>ML Model:</strong> nlptown/bert-base-multilingual-uncased-sentiment</li>
            </ul>
          </section>

          <section className="about-section">
            <h2>ফিচারসমূহ</h2>
            <ul>
              <li>রিয়েল-টাইম সেন্টিমেন্ট বিশ্লেষণ (Positive/Negative/Neutral)</li>
              <li>শব্দের গুরুত্ব Visualization সহ ব্যাখ্যাযোগ্য AI</li>
              <li>Color-coded শব্দ Highlighting</li>
              <li>বিশ্লেষণের ইতিহাস Tracking</li>
              <li>দ্বিভাষিক Support (বাংলা ও English)</li>
            </ul>
          </section>
        </div>
      </div>
    </div>
  );
}

export default About;
