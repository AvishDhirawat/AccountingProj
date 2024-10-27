from flask import Flask
from config import Config
from extensions import db
from routes.loan_routes import loan_bp
from routes.customer_routes import customer_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Register each blueprint
    app.register_blueprint(customer_bp)
    app.register_blueprint(loan_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
