// src/components/SearchCustomer.js
import React, { useState } from 'react';
import styles from './styles/SearchCustomer.module.css';

function SearchCustomer() {
  const [searchQuery, setSearchQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleChange = (e) => {
    setSearchQuery(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('/customers/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ search_query: searchQuery })
      });
      const data = await response.json();
      setResults(data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className={styles.container}>
      <h2>Search Customer</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="search_query">Enter Name, City, Mobile, etc.:</label>
        <input type="text" id="search_query" name="search_query" required value={searchQuery} onChange={handleChange} />
        <button type="submit">Search</button>
      </form>
      {results.length > 0 && (
        <div className={styles.results}>
          <h3>Search Results</h3>
          <ul>
            {results.map(result => (
              <li key={result.customer_id}>
                <a href={`/view-customer/${result.customer_id}`}>
                  {result.first_name} {result.last_name}
                </a>
              </li>
            ))}
          </ul>
        </div>
      )}
      <a href="/" className={styles.backLink}>Back to Home</a>
    </div>
  );
}

export default SearchCustomer;
