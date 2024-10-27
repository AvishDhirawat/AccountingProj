from flask import Blueprint, render_template, request, redirect, url_for
from models.collateral import Collateral
from extensions import db
from datetime import datetime

loan_bp = Blueprint('loan_bp', __name__)


@loan_bp.route('/add_loan/<int:customer_id>', methods=['POST', 'GET'])
def add_loan(customer_id):
    from models.collateral import Collateral  # Delay import
    from models.customer import Customer  # Delay import
    from app import db  # Delay impor
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


@loan_bp.route('/settle_collateral/<int:customer_id>/<int:loan_id>', methods=['POST'])
def settle_collateral(customer_id, loan_id):
    collateral = Collateral.query.filter_by(customer_id=customer_id, loan_id=loan_id).first_or_404()
    collateral.payment_status = 'Settled'

    try:
        db.session.commit()
        return redirect(url_for('view_customer', customer_id=customer_id))
    except Exception as e:
        print(f"Error: {e}")
        return "There was an issue settling the collateral."
