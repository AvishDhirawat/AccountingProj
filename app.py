from flask import Flask, send_from_directory
from config import Config
from extensions import db
from routes.customer_routes import customer_bp
from routes.other_routes import other_bp  # Import the other routes
from routes.api_routes import api_bp  # Import the API routes

def create_app():
    app = Flask(__name__, static_folder='frontend/build', static_url_path='/')
    app.config.from_object(Config)
    db.init_app(app)

    # Register each blueprint with a URL prefix
    app.register_blueprint(other_bp)  # Register the other_bp for the home page
    app.register_blueprint(customer_bp, url_prefix='/customers')
    app.register_blueprint(api_bp, url_prefix='/api')  # Register the API routes

    @app.route('/')
    def serve_react_app():
        return send_from_directory(app.static_folder, 'index.html')

    @app.route('/<path:path>')
    def serve_static_file(path):
        return send_from_directory(app.static_folder, path)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
