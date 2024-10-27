// src/components/Nav.js
import React from 'react';
import { Link } from 'react-router-dom';

function Nav() {
  return (
    <nav>
      <Link to="/add-customer" className="nav-link">Add New Customer</Link>
      <Link to="/search-customer" className="nav-link">Search Customer</Link>
      <Link to="/" className="nav-link">Dashboard</Link>
      <Link to="/about" className="nav-link">About</Link>
    </nav>
  );
}

export default Nav;
