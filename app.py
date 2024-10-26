from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import or_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loan_tracking.db'
db = SQLAlchemy(app)


# Models
class Customer(db.Model):
    customer_id = db.Column(db.String(100), primary_key=True, unique=True, nullable=False)  # Unique customer ID
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    mobile_number = db.Column(db.String(15), nullable=False)
    notes = db.Column(db.Text, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    collaterals = db.relationship('Collateral', backref='owner', lazy=True)


class Collateral(db.Model):
    customer_id = db.Column(db.String(100), db.ForeignKey('customer.customer_id'), primary_key=True)
    loan_id = db.Column(db.Integer, primary_key=True)  # Unique loan ID for each customer
    item_description = db.Column(db.String(200), nullable=False)
    loan_amount = db.Column(db.Float, nullable=False)
    reason_for_loan = db.Column(db.String(200), nullable=False)
    date_of_loan_taken = db.Column(db.DateTime, nullable=False)
    interest_rate = db.Column(db.Float, default=2.5)
    payment_status = db.Column(db.String(20), default='Pending')


# Routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_customer', methods=['POST', 'GET'])
def add_customer():
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        city = request.form.get('city', '')
        mobile_number = request.form.get('mobile_number', '')
        notes = request.form.get('notes', '')

        new_customer = Customer(
            customer_id=customer_id,
            first_name=first_name,
            last_name=last_name,
            city=city,
            mobile_number=mobile_number,
            notes=notes
        )

        try:
            db.session.add(new_customer)
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e:
            print(f"Error: {e}")
            return "There was an issue adding the customer."
    else:
        return render_template('add_customer.html')


@app.route('/view_customer/<int:customer_id>')
def view_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    pending_items = Collateral.query.filter_by(owner=customer, payment_status='Pending').all()
    settled_items = Collateral.query.filter_by(owner=customer, payment_status='Settled').all()
    return render_template('view_customer.html', customer=customer, pending_items=pending_items,
                           settled_items=settled_items)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form['search_query']
        names = search_query.split()
        if search_query.isdigit():  # Check if it's all digits
            customer = Customer.query.filter_by(customer_id=search_query).first()
            if customer:
                return redirect(url_for('view_customer', customer_id=customer.customer_id))
            else:
                return "Customer not found with that ID."
        elif len(names) == 1:
            # If one name is given, search both first and last name
            results = Customer.query.filter(
                (Customer.first_name.ilike(f'%{names[0]}%')) |
                (Customer.last_name.ilike(f'%{names[0]}%'))
            ).all()
        elif len(names) == 2:
            # If two names are given, search for first and last name exactly
            results = Customer.query.filter(
                (Customer.first_name.ilike(f'%{names[0]}%')) &
                (Customer.last_name.ilike(f'%{names[1]}%'))
            ).all()
        else:
            return "Please enter a valid search string."
        # # Search customers based on any field
        # results = Customer.query.filter(
        #     (Customer.first_name.ilike(f'%{search_query}%')) |
        #     (Customer.last_name.ilike(f'%{search_query}%')) |
        # ).all()
        return render_template('search_results.html', results=results, search_query=search_query)
    return render_template('search.html')


@app.route('/add_loan/<int:customer_id>', methods=['POST', 'GET'])
def add_loan(customer_id):
    customer = Customer.query.get_or_404(customer_id)  # Fetch the customer
    full_name = f"{customer.first_name} {customer.last_name}"
    if request.method == 'POST':
        item_description = request.form['item_description']
        loan_amount = float(request.form['loan_amount'])
        reason_for_loan = request.form['reason_for_loan']
        date_of_loan_taken = datetime.strptime(request.form['date_of_loan_taken'], '%Y-%m-%d')

        # Calculate interest till current date
        months_elapsed = (datetime.utcnow() - date_of_loan_taken).days // 30
        interest = loan_amount * (2.5 / 100) * months_elapsed

        # Get the maximum loan number for the customer and increment it
        last_loan = Collateral.query.filter_by(customer_id=customer_id).order_by(Collateral.loan_id.desc()).first()
        loan_id = last_loan.loan_id + 1 if last_loan else 1  # Start from 1 if no loans exist

        new_collateral = Collateral(
            customer_id=customer_id,
            loan_id=loan_id,  # Ensure this is loan_id, not loan_number
            item_description=item_description,
            loan_amount=loan_amount,
            reason_for_loan=reason_for_loan,
            date_of_loan_taken=date_of_loan_taken,
            interest_rate=interest
        )

        try:
            db.session.add(new_collateral)
            db.session.commit()
            return redirect(url_for('view_customer', customer_id=customer_id))
        except Exception as e:
            print(f"Error: {e}")
            return "There was an issue adding the loan details."
    else:
        return render_template('add_loan.html', customer_id=customer_id)


@app.route('/settle_collateral/<int:customer_id>/<int:loan_id>', methods=['POST'])
def settle_collateral(customer_id, loan_id):
    # Logic to settle the collateral
    collateral = Collateral.query.filter_by(customer_id=customer_id, loan_id=loan_id).first_or_404()
    collateral.payment_status = 'Settled'

    try:
        db.session.commit()
        return redirect(url_for('view_customer', customer_id=customer_id))
    except Exception as e:
        print(f"Error: {e}")
        return "There was an issue settling the collateral."


@app.route('/reset_db')
def reset_db():
    db.drop_all()  # Drops all tables
    db.create_all()  # Creates new tables
    return "Database has been reset."


# Ensure tables are created within application context
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
