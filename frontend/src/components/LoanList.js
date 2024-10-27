// src/components/LoanList.js
import React from 'react';

function LoanList({ loans }) {
  return (
    <div>
      <h2>Customer Loans</h2>
      {loans.map((loan, index) => (
        <div key={index} className="loan-item">
          <h3>Item: {loan.item_description}</h3>
          <p>Loan Amount: ${loan.loan_amount}</p>
          <p>Reason: {loan.reason_for_loan}</p>
          <p>Date: {new Date(loan.date_of_loan_taken).toLocaleDateString()}</p>
          <p>Interest Rate: {loan.interest_rate}%</p>
          <p>Status: {loan.payment_status}</p>
        </div>
      ))}
    </div>
  );
}

export default LoanList;
