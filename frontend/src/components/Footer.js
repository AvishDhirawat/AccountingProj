// src/components/Footer.js
import React from 'react';
import styles from './styles/Footer.module.css';

function Footer() {
  return (
    <footer className={`${styles.footer} fade-in`}>
      <p>&copy; 2024 Loan Tracking System. All Rights Reserved.</p>
      <a href="#top" className={styles.backToTop}>Back to Top</a>
    </footer>
  );
}

export default Footer;
