// src/components/Features.js
import React from 'react';
import styles from './styles/Features.module.css';

function Features() {
  return (
    <div className={styles.features}>
      <div className={`${styles.feature} fade-in`}>
        <h3>Customer Management</h3>
        <p>Quickly add, view, and search customer information with detailed loan history.</p>
      </div>
      <div className={`${styles.feature} fade-in`}>
        <h3>Loan Tracking</h3>
        <p>Monitor active loans, settled accounts, and view collateral details securely.</p>
      </div>
      <div className={`${styles.feature} fade-in`}>
        <h3>Intuitive Dashboard</h3>
        <p>Get a snapshot of key metrics and manage your operations efficiently.</p>
      </div>
    </div>
  );
}

export default Features;
