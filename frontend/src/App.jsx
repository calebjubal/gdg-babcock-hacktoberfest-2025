import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import NotFound from './pages/NotFound/NotFound.jsx';
import CertificateForm from './pages/CertificationForm/CertificateForm.jsx';
import Home from './pages/Home/Home.jsx';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/certificate" element={<CertificateForm />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );
}

export default App;