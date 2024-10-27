import React, { useState } from 'react';
import axios from 'axios';

const AddCustomerForm = () => {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const newCustomer = { first_name: firstName, last_name: lastName };
        await axios.post('/api/customers', newCustomer); // Adjust endpoint as necessary
        // Optionally, reset form or handle success
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
                placeholder="First Name"
                required
            />
            <input
                type="text"
                value={lastName}
                onChange={(e) => setLastName(e.target.value)}
                placeholder="Last Name"
                required
            />
            <button type="submit">Add Customer</button>
        </form>
    );
};

export default AddCustomerForm;
