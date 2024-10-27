// src/components/AddLoanForm.js
import React, { useState } from 'react';

function AddLoanForm({ customerId }) {
  const [loan, setLoan] = useState({
    item_description: '',
    loan_amount: '',
    reason_for_loan: '',
    date_of_loan_taken: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setLoan({ ...loan, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(`/loans/add_loan/${customerId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(loan)
      });
      if (response.ok) {
        alert('Loan added successfully');
      } else {
        alert('Error adding loan');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="item_description" placeholder="Item Description" value={loan.item_description} onChange={handleChange} />
      <input name="loan_amount" placeholder="Loan Amount" value={loan.loan_amount} onChange={handleChange} />
      <input name="reason_for_loan" placeholder="Reason for Loan" value={loan.reason_for_loan} onChange={handleChange} />
      <input name="date_of_loan_taken" placeholder="Date of Loan Taken" value={loan.date_of_loan_taken} onChange={handleChange} />
      <button type="submit">Add Loan</button>
    </form>
  );
}

export default AddLoanForm;
