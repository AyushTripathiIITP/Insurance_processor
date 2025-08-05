import os
import sys
from flask import Flask
from flask_cors import CORS # type: ignore
from controller import register_routes

# Add the parent directory to the sys.path to allow imports from src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def create_app():
    """Application factory pattern for creating Flask app"""
    app = Flask(__name__)
    CORS(app)
    
    # Configuration
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload size
    
    # Ensure the upload folder exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    # Register routes
    register_routes(app)
    
    return app

if __name__ == '__main__':
    # Ensure GOOGLE_API_KEY is set
    if "GOOGLE_API_KEY" not in os.environ:
        print("Error: GOOGLE_API_KEY environment variable not set. Please set it before running the server.")
        sys.exit(1)
    
    app = create_app()
    app.run(debug=True, port=5001)