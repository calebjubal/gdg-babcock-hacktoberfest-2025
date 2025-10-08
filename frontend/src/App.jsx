import { useState } from 'react';
import './App.css';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

function App() {
  const [count, setCount] = useState(0);

  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <Navbar />
      <main style={{ flex: 1 }}>
        <h1>HacktoberFest Demo by Favour!</h1>
        <div className="card">
          <button onClick={() => setCount((count) => count + 1)}>
            count is {count}
          </button>
          <p>
            Edit <code>src/App.jsx</code> and save to test HMR
          </p>
        </div>
      </main>
      <Footer />
    </div>
  );
}
export default App;