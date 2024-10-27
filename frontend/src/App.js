// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Nav from './components/Nav';
import Overview from './components/Overview';
import Features from './components/Features';
import CustomerList from './components/CustomerList';
import AddCustomerForm from './components/AddCustomerForm';
import CollateralForm from './components/CollateralForm';
import About from './components/About';
import Footer from './components/Footer';
import './App.css';
import './components/About.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Nav />
        <Routes>
          <Route path="/" element={<><Overview /><Features /></>} />
          <Route path="/add-customer" element={<AddCustomerForm />} />
          <Route path="/add-collateral/:customerId" element={<CollateralForm />} />
          <Route path="/search-customer" element={<CustomerList />} />
          <Route path="/about" element={<About />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
