// src/components/CustomerList.js
import React, { useEffect, useState } from 'react';
import LoanList from './LoanList';

function CustomerList() {
  const [customers, setCustomers] = useState([]);

  useEffect(() => {
    // Fetch customer data from your backend API
    fetch('/api/customers')
      .then(response => response.json())
      .then(data => setCustomers(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      <h2>Customers</h2>
      {customers.map(customer => (
        <div key={customer.customer_id} className="customer-item">
          <h3>{customer.first_name} {customer.last_name}</h3>
          <p>City: {customer.city}</p>
          <p>Mobile: {customer.mobile_number}</p>
          <LoanList loans={customer.collaterals} />
        </div>
      ))}
    </div>
  );
}

export default CustomerList;
