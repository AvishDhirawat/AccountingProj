from flask import Blueprint, render_template, abort
from app import db

other_bp = Blueprint('other_bp', __name__)

@other_bp.route('/')
def index():
    return render_template('index.html')  # Correct path if it's in templates/

@other_bp.route('/reset_db')
def reset_db():
    try:
        db.drop_all()
        db.create_all()
        return "Database has been reset."
    except Exception as e:
        print(f"Error resetting database: {e}")
        return "An error occurred while resetting the database.", 500  # Return a 500 error code
