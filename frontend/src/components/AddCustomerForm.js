// src/components/AddCustomerForm.js
import React, { useState } from 'react';

function AddCustomerForm() {
  const [customer, setCustomer] = useState({
    customer_id: '',
    first_name: '',
    last_name: '',
    city: '',
    mobile_number: '',
    notes: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCustomer({ ...customer, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('/customers/add_customer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(customer)
      });
      if (response.ok) {
        alert('Customer added successfully');
      } else {
        alert('Error adding customer');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="container">
      <div className="card">
        <h2>Add Customer</h2>
        <form onSubmit={handleSubmit}>
          <label htmlFor="customer_id">Customer ID:</label>
          <input type="text" id="customer_id" name="customer_id" required value={customer.customer_id} onChange={handleChange} />
          <div className="form-group">
            <label htmlFor="first_name">First Name:</label>
            <input type="text" id="first_name" name="first_name" required value={customer.first_name} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label htmlFor="last_name">Last Name:</label>
            <input type="text" id="last_name" name="last_name" required value={customer.last_name} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label htmlFor="city">City:</label>
            <input type="text" id="city" name="city" required value={customer.city} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label htmlFor="mobile_number">Mobile Number:</label>
            <input type="tel" id="mobile_number" name="mobile_number" required pattern="[0-9]{10}" placeholder="10-digit number" value={customer.mobile_number} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label htmlFor="notes">Additional Notes:</label>
            <textarea id="notes" name="notes" rows="4" placeholder="Optional" value={customer.notes} onChange={handleChange}></textarea>
          </div>
          <button type="submit" className="submit-button">Add Customer</button>
        </form>
        <a href="/" className="back-link">Back to Home</a>
      </div>
    </div>
  );
}

export default AddCustomerForm;
