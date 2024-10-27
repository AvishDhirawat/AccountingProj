import React, { useEffect, useState } from 'react';

const CollateralList = () => {
    const [collaterals, setCollaterals] = useState([]);

    useEffect(() => {
        const fetchCollaterals = async () => {
            const response = await fetch('/api/collaterals');
            const data = await response.json();
            setCollaterals(data);
        };

        fetchCollaterals();
    }, []);

    return (
        <div>
            <h2>Collateral List</h2>
            <table>
                <thead>
                    <tr>
                        <th>Customer ID</th>
                        <th>Loan ID</th>
                        <th>Item Description</th>
                        <th>Loan Amount</th>
                        <th>Reason for Loan</th>
                        <th>Date of Loan Taken</th>
                        <th>Interest Rate</th>
                        <th>Payment Status</th>
                    </tr>
                </thead>
                <tbody>
                    {collaterals.map((collateral) => (
                        <tr key={collateral.loan_id}>
                            <td>{collateral.customer_id}</td>
                            <td>{collateral.loan_id}</td>
                            <td>{collateral.item_description}</td>
                            <td>{collateral.loan_amount}</td>
                            <td>{collateral.reason_for_loan}</td>
                            <td>{new Date(collateral.date_of_loan_taken).toLocaleDateString()}</td>
                            <td>{collateral.interest_rate}</td>
                            <td>{collateral.payment_status}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default CollateralList;
