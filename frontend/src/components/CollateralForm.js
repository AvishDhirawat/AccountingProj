// src/components/AddCollateralForm.js
import React, { useState } from 'react';
import { useParams } from 'react-router-dom';

function AddCollateralForm() {
  const { customerId } = useParams();
  const [collateral, setCollateral] = useState({
    item_description: '',
    loan_amount: '',
    interest_rate: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCollateral({ ...collateral, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(`/add_collateral/${customerId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(collateral)
      });
      if (response.ok) {
        alert('Collateral added successfully');
      } else {
        alert('Error adding collateral');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h1>Add Collateral for Customer {customerId}</h1>
      <label htmlFor="item_description">Item Description:</label>
      <input type="text" id="item_description" name="item_description" required value={collateral.item_description} onChange={handleChange} />
      <label htmlFor="loan_amount">Loan Amount:</label>
      <input type="number" id="loan_amount" name="loan_amount" step="0.01" required value={collateral.loan_amount} onChange={handleChange} />
      <label htmlFor="interest_rate">Interest Rate (%):</label>
      <input type="number" id="interest_rate" name="interest_rate" step="0.01" required value={collateral.interest_rate} onChange={handleChange} />
      <button type="submit">Add Collateral</button>
    </form>
  );
}

export default AddCollateralForm;
