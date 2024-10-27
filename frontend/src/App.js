// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Nav from './components/Nav';
import Overview from './components/Overview';
import Features from './components/Features';
import CustomerList from './components/CustomerList';
import AddCustomerForm from './components/AddCustomerForm';
import AddCollateralForm from './components/AddCollateralForm';
import About from './components/About';
import Footer from './components/Footer';
import ViewCustomer from './components/ViewCustomer';
import './components/styles/global.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Nav />
        <Routes>
          <Route path="/" element={<><Overview /><Features /></>} />
          <Route path="/customers/add_customer" element={<AddCustomerForm />} />
          <Route path="/add_collateral/:customerId" element={<AddCollateralForm />} />
          <Route path="/customers/search" element={<CustomerList />} />
          <Route path="/view_customer/:customerId" element={<ViewCustomer />} />
          <Route path="/about" element={<About />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
