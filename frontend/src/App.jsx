import React from 'react';
import FileUpload from './FileUpload';
import Header from './header';

function App() {
  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      minHeight: '100vh',
      backgroundColor: '#f5f5f5',
      padding: '20px',
    }}>
      <Header />
      <div style={{ marginTop: '30px' }}>
        <FileUpload />
      </div>
    </div>
  );
}

export default App;
