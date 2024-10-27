// src/components/ViewCustomer.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import styles from './styles/ViewCustomer.module.css';

function ViewCustomer() {
  const { customerId } = useParams();
  const [customer, setCustomer] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`/view_customer/${customerId}`)
      .then(response => response.json())
      .then(data => setCustomer(data))
      .catch(error => setError(error.toString()));
  }, [customerId]);

  if (error) {
    return (
      <div className={styles.container}>
        <p className={styles.errorMessage}>{error}</p>
        <a href="/" className={styles.backToHomeButton}>Back to Home</a>
        <a href="/search-customer" className={styles.backToSearchButton}>Back to Customer Search</a>
      </div>
    );
  }

  if (!customer) {
    return <p>Loading...</p>;
  }

  return (
    <div className={styles.container}>
      <a href="/" className={styles.backToHomeButton}>Back to Home</a>
      <h1>Customer Details for {customer.first_name} {customer.last_name}</h1>
      <p>Customer ID: {customer.customer_id}</p>
      <p>Name: {customer.first_name} {customer.last_name}</p>
      <p>City: {customer.city}</p>
      <p>Mobile Number: {customer.mobile_number}</p>
      <p>Notes: {customer.notes}</p>

      <h2>Pending Loans</h2>
      <table className={styles.table}>
        <thead>
          <tr>
            <th>Item Description</th>
            <th>Date of Loan Taken</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {customer.pending_items.map(item => (
            <tr key={item.loan_id}>
              <td>{item.item_description}</td>
              <td>{new Date(item.date_of_loan_taken).toLocaleDateString()}</td>
              <td>
                <form method="POST" action={`/settle_collateral/${customer.customer_id}/${item.loan_id}`}>
                  <button type="submit" className={styles.settleButton}>Settle</button>
                </form>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <h2>Settled Loans</h2>
      <table className={styles.table}>
        <thead>
          <tr>
            <th>Item Description</th>
            <th>Date of Loan Taken</th>
          </tr>
        </thead>
        <tbody>
          {customer.settled_items.map(item => (
            <tr key={item.loan_id}>
              <td>{item.item_description}</td>
              <td>{new Date(item.date_of_loan_taken).toLocaleDateString()}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <a href={`/add_loan/${customer.customer_id}`} className={styles.addLoanButton}>Add New Loan</a>
    </div>
  );
}

export default ViewCustomer;
