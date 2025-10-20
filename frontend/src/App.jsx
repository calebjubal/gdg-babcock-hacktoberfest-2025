import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Navbar from './components/Navbar/Navbar.jsx';
import Footer from './components/Footer/Footer.jsx';
import NotFound from './pages/NotFound/NotFound.jsx';
import CertificateForm from './pages/CertificationForm/CertificateForm.jsx';
import Home from './pages/Home/Home.jsx';
import { Toaster } from 'react-hot-toast';

function App() {
  return (
    <Router>
      <div className="app-container">
        <Navbar />
        <main className="app-main">
          <Toaster
            position="top-right"
            gutter={16}
            toastOptions={{
              duration: 5000,
              success: { duration: 5000 },
              error: { duration: 6000 },
              loading: { duration: Infinity },
            }}
          />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/certificate" element={<CertificateForm />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;