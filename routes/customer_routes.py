from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from extensions import db
from models.customer import Customer
from models.collateral import Collateral

customer_bp = Blueprint('customer_bp', __name__, url_prefix='/customers')


@customer_bp.route('/add_customer', methods=['POST'])
def add_customer():
    data = request.get_json()
    customer_id = data['customer_id']
    first_name = data['first_name']
    last_name = data['last_name']
    city = data.get('city', '')
    mobile_number = data.get('mobile_number', '')
    notes = data.get('notes', '')

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
        return jsonify({"message": "Customer added successfully"}), 201
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "There was an issue adding the customer."}), 500


@customer_bp.route('/view_customer/<int:customer_id>')
def view_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    pending_items = Collateral.query.filter_by(customer_id=customer_id, payment_status='Pending').all()
    settled_items = Collateral.query.filter_by(customer_id=customer_id, payment_status='Settled').all()
    return jsonify({
        'customer': customer.serialize(),
        'pending_items': [item.serialize() for item in pending_items],
        'settled_items': [item.serialize() for item in settled_items]
    })


@customer_bp.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.json['search_query']
        names = search_query.split()

        if search_query.isdigit():
            customer = Customer.query.filter_by(customer_id=search_query).first()
            if customer:
                return jsonify(customer.serialize())
            return jsonify({"error": "Customer not found with that ID."}), 404

        elif len(names) == 1:
            results = Customer.query.filter(
                (Customer.first_name.ilike(f'%{names[0]}%')) | (Customer.last_name.ilike(f'%{names[0]}%'))).all()
        elif len(names) == 2:
            results = Customer.query.filter(
                (Customer.first_name.ilike(f'%{names[0]}%')) & (Customer.last_name.ilike(f'%{names[1]}%'))).all()
        else:
            return jsonify({"error": "Please enter a valid search string."}), 400

        return jsonify([result.serialize() for result in results])
    return render_template('search.html')
