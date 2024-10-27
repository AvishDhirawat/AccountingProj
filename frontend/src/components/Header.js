// src/components/Header.js
import React from 'react';
import styles from './style/Header.module.css';

function Header() {
  return (
    <header className={`${styles.header} fade-in`}>
      <h1>Loan Tracking & Management System</h1>
      <p className={styles.tagline}>Efficiently track, manage, and analyze loans with ease.</p>
    </header>
  );
}

export default Header;
