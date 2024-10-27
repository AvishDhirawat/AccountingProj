# Loan Tracking & Management System

## Introduction
The Loan Tracking & Management System is designed for jewelry shops to efficiently track, manage, and analyze loans with jewelry as collateral. This system provides a streamlined process for managing customer loans, tracking pending payments, and maintaining organized customer records.

## Features
- **Customer Management**: Add, view, and search customer information with detailed loan history.
- **Loan Tracking**: Monitor active loans, settled accounts, and view collateral details securely.
- **Intuitive Dashboard**: Get a snapshot of key metrics and manage your operations efficiently.

## Tech Stack
- **Frontend**: React, CSS Modules
- **Backend**: Flask, SQLAlchemy
- **Database**: SQLite (or specify if using another DBMS)
- **Other Tools**: axios

## Project Structure
```plaintext
AccountingProj/
├── app.py
├── config.py
├── extensions.py
├── models/
│   ├── __init__.py
│   ├── customer.py
│   └── collateral.py
├── routes/
│   ├── __init__.py
│   ├── customer_routes.py
│   └── loan_routes.py
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── add_customer.html
│   └── add_collateral.html
├── static/
│   ├── index_style.css
│   ├── about_page_style.css
│   └── add_customer_style.css
├── frontend/
│   ├── package.json
│   ├── public/
│   └── src/
│       ├── components/
│       │   ├── Header.js
│       │   ├── Nav.js
│       │   ├── Overview.js
│       │   ├── Features.js
│       │   ├── CustomerList.js
│       │   ├── AddCustomerForm.js
│       │   ├── CollateralForm.js
│       │   ├── About.js
│       │   ├── Footer.js
│       │   ├── ViewCustomer.js
│       │   └── styles/
│       │       ├── Header.module.css
│       │       ├── Nav.module.css
│       │       ├── Overview.module.css
│       │       ├── Features.module.css
│       │       ├── AddCustomerForm.module.css
│       │       ├── ViewCustomer.module.css
│       │       └── global.css
│       ├── App.js
│       └── index.js
