// src/components/MainContent.js
import React from 'react';
import './styles/MainContent.css';

function MainContent({ children }) {
  return (
    <div className="main-content">
      {children}
    </div>
  );
}

export default MainContent;
