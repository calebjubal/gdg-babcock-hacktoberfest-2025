import React, { useState } from 'react';
import Navbar from '../components/Navbar/Navbar';
import Footer from '../components/Footer/Footer';
import './CertificateForm.css';

const CertificateForm = () => {
  const [form, setForm] = useState({
    participant_name: '',
    event_name: '',
    role: '',
    date_issued: '',
  });
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState(null);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setSuccess(null);
    setError(null);
    try {
      const res = await fetch('/api/certificates/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          participant_name: form.participant_name,
          event_name: form.event_name,
          date_issued: form.date_issued,
          // role is not used in backend, but included in form for future
        }),
      });
      if (!res.ok) throw new Error('Failed to create certificate');
      const data = await res.json();
      setSuccess(data);
      setForm({ participant_name: '', event_name: '', role: '', date_issued: '' });
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <Navbar />
      <main style={{ flex: 1, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <form className="cert-form" onSubmit={handleSubmit}>
          <h2>Generate Certificate</h2>
          <label>
            Name
            <input
              type="text"
              name="participant_name"
              value={form.participant_name}
              onChange={handleChange}
              required
              minLength={2}
              maxLength={100}
              placeholder="Enter full name"
            />
          </label>
          <label>
            Event
            <input
              type="text"
              name="event_name"
              value={form.event_name}
              onChange={handleChange}
              required
              minLength={3}
              maxLength={200}
              placeholder="Event name"
            />
          </label>
          <label>
            Role
            <input
              type="text"
              name="role"
              value={form.role}
              onChange={handleChange}
              placeholder="Role (optional)"
            />
          </label>
          <label>
            Date
            <input
              type="date"
              name="date_issued"
              value={form.date_issued}
              onChange={handleChange}
              required
            />
          </label>
          <button type="submit" disabled={loading}>
            {loading ? 'Generating...' : 'Generate'}
          </button>
          {success && (
            <div className="cert-success">
              Certificate generated! <br />
              <a href={success.download_url} target="_blank" rel="noopener noreferrer">Download Certificate</a>
            </div>
          )}
          {error && <div className="cert-error">{error}</div>}
        </form>
      </main>
      <Footer />
    </div>
  );
};

export default CertificateForm;
