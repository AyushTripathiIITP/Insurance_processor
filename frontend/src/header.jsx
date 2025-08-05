import React from 'react';

export default function Header() {
  return (
    <header style={{
      backgroundColor: '#007bff',
      color: 'white',
      padding: '10px 20px',
      textAlign: 'center',
      borderRadius: '5px'
    }}>
      <h1>Insurance Claim Processor</h1>
      <p>Upload your insurance claim documents for processing.</p>
    </header>
  );
}