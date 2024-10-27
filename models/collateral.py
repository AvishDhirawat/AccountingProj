from extensions import db
from datetime import datetime

class Collateral(db.Model):
    customer_id = db.Column(db.String(100), db.ForeignKey('customer.customer_id'), primary_key=True)
    loan_id = db.Column(db.Integer, primary_key=True)
    item_description = db.Column(db.String(200), nullable=False)
    loan_amount = db.Column(db.Float, nullable=False)
    reason_for_loan = db.Column(db.String(200), nullable=False)
    date_of_loan_taken = db.Column(db.DateTime, nullable=False)
    interest_rate = db.Column(db.Float, default=2.5)
    payment_status = db.Column(db.String(20), default='Pending')
