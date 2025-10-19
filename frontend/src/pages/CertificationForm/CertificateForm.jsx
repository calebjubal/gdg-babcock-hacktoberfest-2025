import React, { useState } from 'react';
import axios from 'axios';
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
  const [certificateUrl, setCertificateUrl] = useState(null);
  const [imageLoading, setImageLoading] = useState(false);
  const [imageError, setImageError] = useState(null);

  const API_BASE_URL = 'http://localhost:8000';

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setSuccess(null);
    setError(null);
    setCertificateUrl(null);
    setImageError(null);

    try {
      const res = await axios.post(`${API_BASE_URL}/certificates/`, {
        participant_name: form.participant_name,
        event_name: form.event_name,
        date_issued: form.date_issued,
      });

      setSuccess(res.data);
      setForm({ participant_name: '', event_name: '', role: '', date_issued: '' });

      if (res.data.download_url) {
        setImageLoading(true);
        const url = `${API_BASE_URL}${res.data.download_url}`;
        try {
          await axios.get(url);
          setCertificateUrl(url);
        } catch (imgErr) {
          setImageError('Could not load certificate image.');
        } finally {
          setImageLoading(false);
        }
      }
    } catch (err) {
      setError(err.response?.data?.message || err.message || 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  return (
    <main style={{ flex: 1, display: 'flex', justifyContent: 'center', alignItems: 'center', flexDirection: 'column' }}>
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
        {success && <div className="cert-success">Certificate generated!</div>}
        {error && <div className="cert-error">{error}</div>}
      </form>

      {certificateUrl && (
        <div style={{ marginTop: '2rem', textAlign: 'center' }}>
          <h3>Certificate Preview</h3>
          {imageLoading ? (
            <p>Loading certificate...</p>
          ) : (
            <img
              src={certificateUrl}
              alt="Certificate Preview"
              style={{ maxWidth: '100%', border: '1px solid #ccc', marginBottom: '1rem' }}
            />
          )}
          <div>
            <a href={certificateUrl} download>
              <button type="button">Download Certificate</button>
            </a>
          </div>
        </div>
      )}
      {imageError && <p className="cert-error">{imageError}</p>}
    </main>
  );
};

export default CertificateForm;
