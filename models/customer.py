from extensions import db
from datetime import datetime

class Customer(db.Model):
    customer_id = db.Column(db.String(100), primary_key=True, unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    mobile_number = db.Column(db.String(15), nullable=False)
    notes = db.Column(db.Text, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    collaterals = db.relationship('Collateral', backref='owner', lazy=True)
