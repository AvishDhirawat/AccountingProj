// src/components/Overview.js
import React from 'react';
import styles from './styles/Overview.module.css';

function Overview() {
  return (
    <section id="overview" className={`${styles.overview} fade-in`}>
      <h2>Overview</h2>
      <p>
        Welcome to the Loan Tracking & Management System, designed to streamline the process of managing
        customer loans with jewelry as collateral. Track loan details, view pending payments, and maintain
        organized customer records all in one place.
      </p>
    </section>
  );
}

export default Overview;
