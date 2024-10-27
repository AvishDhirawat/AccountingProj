from flask import Blueprint, jsonify
from models.collateral import Collateral  # Ensure this points to your Collateral model

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/collaterals', methods=['GET'])
def get_collaterals():
    collaterals = Collateral.query.all()
    collateral_list = [{
        'customer_id': collateral.customer_id,
        'loan_id': collateral.loan_id,
        'item_description': collateral.item_description,
        'loan_amount': collateral.loan_amount,
        'reason_for_loan': collateral.reason_for_loan,
        'date_of_loan_taken': collateral.date_of_loan_taken.isoformat(),  # Convert datetime to string
        'interest_rate': collateral.interest_rate,
        'payment_status': collateral.payment_status
    } for collateral in collaterals]
    return jsonify(collateral_list)
