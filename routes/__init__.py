from .customer_routes import customer_bp
from .loan_routes import loan_bp

# List of all blueprints to register in the app
all_blueprints = [customer_bp, loan_bp]
