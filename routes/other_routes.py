from flask import Blueprint, render_template, abort, jsonify
from extensions import db

other_bp = Blueprint('other_bp', __name__)


@other_bp.route('/')
def index():
    return render_template('index.html')


@other_bp.route('/reset_db')
def reset_db():
    try:
        db.drop_all()
        db.create_all()
        return jsonify({"message": "Database has been reset."}), 200
    except Exception as e:
        print(f"Error resetting database: {e}")
        return jsonify({"error": "An error occurred while resetting the database."}), 500



@other_bp.route('/about')
def about():
    return render_template('about.html')
