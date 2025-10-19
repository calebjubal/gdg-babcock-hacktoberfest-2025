import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import NotFound from './pages/NotFound/NotFound.jsx';
import CertificateForm from './pages/CertificationForm/CertificateForm.jsx';
import Home from './pages/Home/Home.jsx';


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/certificate" element={<CertificateForm />} />
        <Route path="*" element={<NotFound   />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;