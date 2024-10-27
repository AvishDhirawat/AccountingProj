from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db
from models.customer import Customer
from models.collateral import Collateral

customer_bp = Blueprint('customer_bp', __name__, url_prefix='/customers')


@customer_bp.route('/add_customer', methods=['POST', 'GET'])
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
            return redirect(url_for('customer_bp.view_customer', customer_id=customer_id))  # Ensure correct URL
        except Exception as e:
            print(f"Error: {e}")
            return "There was an issue adding the customer."
    else:
        return render_template('add_customer.html')


@customer_bp.route('/view_customer/<int:customer_id>')
def view_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    pending_items = Collateral.query.filter_by(customer_id=customer_id, payment_status='Pending').all()
    settled_items = Collateral.query.filter_by(customer_id=customer_id, payment_status='Settled').all()
    return render_template('view_customer.html', customer=customer, pending_items=pending_items,
                           settled_items=settled_items)


@customer_bp.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form['search_query']
        names = search_query.split()
        if search_query.isdigit():  # Check if it's all digits
            customer = Customer.query.filter_by(customer_id=search_query).first()
            if customer:
                return redirect(url_for('customer_bp.view_customer', customer_id=customer.customer_id))
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
