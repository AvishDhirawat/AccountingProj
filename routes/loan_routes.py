from flask import Blueprint, request, jsonify, render_template
from models.collateral import Collateral
from extensions import db
from models.customer import Customer
from datetime import datetime

loan_bp = Blueprint('loan_bp', __name__)


@loan_bp.route('/add_loan/<int:customer_id>', methods=['POST', 'GET'])
def add_loan(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    full_name = f"{customer.first_name} {customer.last_name}"
    if request.method == 'POST':
        data = request.get_json()
        item_description = data['item_description']
        loan_amount = float(data['loan_amount'])
        reason_for_loan = data['reason_for_loan']
        date_of_loan_taken = datetime.strptime(data['date_of_loan_taken'], '%Y-%m-%d')

        months_elapsed = (datetime.utcnow() - date_of_loan_taken).days // 30
        interest = loan_amount * (2.5 / 100) * months_elapsed

        last_loan = Collateral.query.filter_by(customer_id=customer_id).order_by(Collateral.loan_id.desc()).first()
        loan_id = last_loan.loan_id + 1 if last_loan else 1

        new_collateral = Collateral(
            customer_id=customer_id,
            loan_id=loan_id,
            item_description=item_description,
            loan_amount=loan_amount,
            reason_for_loan=reason_for_loan,
            date_of_loan_taken=date_of_loan_taken,
            interest_rate=interest
        )
        try:
            db.session.add(new_collateral)
            db.session.commit()
            return jsonify({"message": "Collateral added successfully"}), 201
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"error": "There was an issue adding the collateral."}), 500
    else:
        return render_template('add_loan.html', customer_id=customer_id)


@loan_bp.route('/settle_collateral/<int:customer_id>/<int:loan_id>', methods=['POST'])
def settle_collateral(customer_id, loan_id):
    collateral = Collateral.query.filter_by(customer_id=customer_id, loan_id=loan_id).first_or_404()
    collateral.payment_status = 'Settled'
    try:
        db.session.commit()
        return jsonify({"message": "Collateral settled successfully"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "There was an issue settling the collateral."}), 500
