import React, { useEffect, useState } from 'react';
import axios from 'axios';

const CustomerList = () => {
    const [customers, setCustomers] = useState([]);

    useEffect(() => {
        const fetchCustomers = async () => {
            const response = await axios.get('/api/customers'); // Adjust the endpoint based on your Flask API
            setCustomers(response.data);
        };
        fetchCustomers();
    }, []);

    return (
        <div>
            <h2>Customer List</h2>
            <ul>
                {customers.map(customer => (
                    <li key={customer.customer_id}>
                        {customer.first_name} {customer.last_name}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default CustomerList;
