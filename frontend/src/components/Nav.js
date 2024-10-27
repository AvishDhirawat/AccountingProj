// src/components/Nav.js
import React from 'react';

function Nav() {
  return (
    <nav>
      <a href="/add-customer" className="nav-link">Add New Customer</a>
      <a href="/search-customer" className="nav-link">Search Customer</a>
      <a href="/dashboard" className="nav-link">Dashboard</a>
      <a href="/about" className="nav-link">About</a>
    </nav>
  );
}

export default Nav;
