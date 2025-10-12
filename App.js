import React from 'react';
import './App.css';
import NotFound from './components/NotFound';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// Simple Home component for main page
function Home() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome Home,User!</h1>
        <p>This is the main page of your app.</p>
      </header>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        {/* Main Home page */}
        <Route path="/" element={<Home />} />
        {/* Shrut 404 page */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );
}

export default App;
