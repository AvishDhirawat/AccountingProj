from flask import Flask
from config import Config
from extensions import db
from routes.loan_routes import loan_bp
from routes.customer_routes import customer_bp
from routes.other_routes import other_bp  # Import the other routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Register each blueprint with a URL prefix
    app.register_blueprint(other_bp)  # Register the other_bp for the home page
    app.register_blueprint(customer_bp, url_prefix='/customers')
    app.register_blueprint(loan_bp, url_prefix='/loans')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
