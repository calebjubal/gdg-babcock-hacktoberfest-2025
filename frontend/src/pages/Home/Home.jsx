import { useState } from "react";
import "./Home.css";

export default function Home() {
  const [count, setCount] = useState(0);

  return (
    <main className="home-main">
      <h1>HacktoberFest Demo</h1>
      <div className="card">
        <button onClick={() => setCount((c) => c + 1)}>count is {count}</button>
        <p>
          Edit <code>src/pages/Home/Home.jsx</code> and save to test HMR
        </p>
      </div>
    </main>
  );
}
