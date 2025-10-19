import { useState } from 'react';
import Navbar from '../../components/Navbar/Navbar.jsx';
import Footer from '../../components/Footer/Footer.jsx';
import './Home.css';

export default function Home() {
  const [count, setCount] = useState(0);

  return (
    <div className="home-container">
      <Navbar />
      <main className="home-main">
        <h1>HacktoberFest Demo by Favour!</h1>
        <div className="card">
          <button onClick={() => setCount((c) => c + 1)}>
            count is {count}
          </button>
          <p>
            Edit <code>src/pages/Home/Home.jsx</code> and save to test HMR
          </p>
        </div>
      </main>
      <Footer />
    </div>
  );
}
