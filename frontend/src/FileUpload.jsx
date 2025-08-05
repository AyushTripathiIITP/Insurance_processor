import React, { useState } from 'react';

function FileUpload() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
    setResponse(null);
    setError(null);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setError("Please select a file first.");
      return;
    }

    setLoading(true);
    setError(null);
    setResponse(null);

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const res = await fetch('http://localhost:5001/process_document', {
        method: 'POST',
        body: formData,
      });

      if (!res.ok) {
        const errorData = await res.json();
        throw new Error(errorData.error || `HTTP error! status: ${res.status}`);
      }

      const data = await res.json();
      setResponse(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const renderSafeField = (value) => {
    if (value == null) return '';
    return typeof value === 'object' ? JSON.stringify(value, null, 2) : value;
  };

  return (
    <div style={{
      fontFamily: 'Arial, sans-serif',
      maxWidth: '600px',
      margin: '20px auto',
      padding: '20px',
      border: '1px solid #ccc',
      borderRadius: '8px',
      boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
    }}>
      <h2 style={{ textAlign: 'center', color: '#333' }}>Document Processor</h2>
      <div style={{ marginBottom: '15px' }}>
        <input type="file" onChange={handleFileChange} style={{ display: 'block', marginBottom: '10px' }} />
        <button onClick={handleUpload} disabled={loading} style={{
          backgroundColor: '#007bff',
          color: 'white',
          padding: '10px 15px',
          border: 'none',
          borderRadius: '5px',
          cursor: 'pointer',
          fontSize: '16px'
        }}>
          {loading ? 'Uploading...' : 'Upload and Process'}
        </button>
      </div>

      {error && (
        <div style={{
          color: 'red',
          marginBottom: '10px',
          border: '1px solid red',
          padding: '10px',
          borderRadius: '5px',
          backgroundColor: '#ffe6e6'
        }}>
          <strong>Error:</strong> {error}
        </div>
      )}

      {response && (
        <div style={{
          border: '1px solid #28a745',
          padding: '15px',
          borderRadius: '5px',
          backgroundColor: '#e6ffe6'
        }}>
          <h3 style={{ color: '#28a745', marginTop: '0' }}>Processing Result:</h3>
          <p><strong>Message:</strong> {renderSafeField(response.message)}</p>
          <p><strong>Classification:</strong> {renderSafeField(response.classification)}</p>
          <p><strong>Storage Path:</strong> {renderSafeField(response.storage_path)}</p>

          <h4>Extracted Text:</h4>
          <pre style={{
            whiteSpace: 'pre-wrap',
            backgroundColor: '#f8f9fa',
            padding: '10px',
            borderRadius: '5px',
            border: '1px solid #ddd'
          }}>{renderSafeField(response.extracted_text)}</pre>

          <h4>Summary:</h4>
          <pre style={{
            whiteSpace: 'pre-wrap',
            backgroundColor: '#f8f9fa',
            padding: '10px',
            borderRadius: '5px',
            border: '1px solid #ddd'
          }}>{renderSafeField(response.summary)}</pre>

          <h4>Metrics:</h4>
          <pre style={{
            whiteSpace: 'pre-wrap',
            backgroundColor: '#f8f9fa',
            padding: '10px',
            borderRadius: '5px',
            border: '1px solid #ddd'
          }}>{JSON.stringify(response.metrics, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default FileUpload;
