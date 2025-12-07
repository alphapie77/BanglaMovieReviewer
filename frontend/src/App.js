import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useLocation } from 'react-router-dom';
import { Film, Sparkles, Home as HomeIcon, BarChart, Info } from 'lucide-react';
import Home from './pages/Home';
import Analyzer from './pages/Analyzer';
import Result from './pages/Result';
import History from './pages/History';
import About from './pages/About';
import './App.css';

function Navigation() {
  const location = useLocation();
  
  const isActive = (path) => location.pathname === path;
  
  return (
    <nav className="nav">
      <Link to="/" className={`nav-link ${isActive('/') ? 'active' : ''}`}>
        <HomeIcon size={20} />
        <span>হোম</span>
      </Link>
      <Link to="/analyzer" className={`nav-link ${isActive('/analyzer') ? 'active' : ''}`}>
        <Sparkles size={20} />
        <span>বিশ্লেষক</span>
      </Link>
      <Link to="/history" className={`nav-link ${isActive('/history') ? 'active' : ''}`}>
        <BarChart size={20} />
        <span>ইতিহাস</span>
      </Link>
      <Link to="/about" className={`nav-link ${isActive('/about') ? 'active' : ''}`}>
        <Info size={20} />
        <span>সম্পর্কে</span>
      </Link>
    </nav>
  );
}

function App() {
  return (
    <Router>
      <div className="app">
        <header className="header">
          <div className="header-content">
            <Link to="/" className="logo">
              <Film size={32} />
              <h1>সিনেমা রিভিউ পরীক্ষক</h1>
            </Link>
            <Navigation />
          </div>
        </header>

        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/analyzer" element={<Analyzer />} />
            <Route path="/result" element={<Result />} />
            <Route path="/history" element={<History />} />
            <Route path="/about" element={<About />} />
          </Routes>
        </main>

        <footer className="footer">
          <p>© 2025 সিনেমা রিভিউ পরীক্ষক | Academic Research Project</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;
