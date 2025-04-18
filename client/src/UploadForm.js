import React, { useState } from 'react';
import axios from 'axios';

function UploadForm({ onTopicsDetected }) {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState('');

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) {
      setStatus('Please select a file.');
      return;
    }

    const formData = new FormData();
    formData.append('resume', file);

    try {
      const response = await axios.post('http://localhost:5000/upload-resume', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      const topics = response.data.topics;
      onTopicsDetected(topics);  // pass topics back to App
      setStatus(`Detected topics: ${topics.join(', ')}`);
    } catch (err) {
      console.error(err);
      setStatus('Error uploading file.');
    }
  };

  return (
    <div style={{ marginTop: '20px' }}>
      <h3>Upload Your Resume (PDF)</h3>
      <form onSubmit={handleUpload}>
        <input type="file" accept=".pdf" onChange={(e) => setFile(e.target.files[0])} />
        <button type="submit">Upload</button>
      </form>
      <p>{status}</p>
    </div>
  );
}

export default UploadForm;
