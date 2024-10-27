// src/components/Nav.js
import React from 'react';
import { Link } from 'react-router-dom';
import styles from './styles/Nav.module.css';

function Nav() {
  return (
    <nav className={styles.nav}>
      <Link to="/add-customer" className={styles.navLink}>Add New Customer</Link>
      <Link to="/search-customer" className={styles.navLink}>Search Customer</Link>
      <Link to="/" className={styles.navLink}>Dashboard</Link>
      <Link to="/about" className={styles.navLink}>About</Link>
    </nav>
  );
}

export default Nav;
