from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import or_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loan_tracking.db'
db = SQLAlchemy(app)


# Models
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=True)
    mobile_number = db.Column(db.String(15), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    collaterals = db.relationship('Collateral', backref='owner', lazy=True)


class Collateral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_description = db.Column(db.String(200), nullable=False)
    loan_amount = db.Column(db.Float, nullable=False)
    interest_rate = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.String(20), default='Pending')  # Pending or Settled
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)


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
        except:
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
        # Search customers based on any field
        results = Customer.query.filter(
            (Customer.first_name.ilike(f'%{search_query}%')) |
            (Customer.last_name.ilike(f'%{search_query}%')) |
            (Customer.city.ilike(f'%{search_query}%')) |
            (Customer.mobile_number.ilike(f'%{search_query}%')) |
            (Customer.customer_id.ilike(f'%{search_query}%')) |
            (Customer.notes.ilike(f'%{search_query}%'))
        ).all()
        return render_template('search_results.html', results=results, search_query=search_query)
    return render_template('search.html')



# Ensure tables are created within application context
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
