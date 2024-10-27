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
```
## Initialization and Setup

### Backend Setup
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd AccountingProj

2. **Create and Activate a Virtual Environment**:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```
3. **Install the required packages**:

```bash

pip install -r requirements.txt
```
4. **Run the Flask app**:

```bash


set FLASK_APP=app.py  # On Windows
set FLASK_ENV=development
flask run
```
###Frontend Setup
1. **Navigate to the frontend directory**:

```bash

cd frontend
```
##Install the dependencies:

```bash

npm install
```
##Start the React development server:

```bash

npm start
```
###Usage
Open your browser and go to ```http://localhost:3000``` to access the frontend.

Use the navigation menu to add new customers, search customers, and view customer details.

The backend should be running at ```http://127.0.0.1:5000.```

Development
This project is currently in progress. Upcoming features include:

Advanced loan filtering and sorting

Notification system for due payments

Enhanced dashboard metrics

Contributions
Contributions are welcome! Please fork this repository and create a pull request for any feature additions or bug fixes.

License
This project is licensed under the MIT License.

Contact
For any questions or feedback, feel free to reach out to the developer:

Name: Avish Dhirawat

Role: Java Backend Developer

GitHub: avishdhirawat

LinkedIn: linkedin.com/in/avishdhirawat



