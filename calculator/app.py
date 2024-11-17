"""
Main application module for the Flask calculator application.
"""

from flask import Flask
from urls import calculate_bp

app = Flask(__name__)
app.register_blueprint(calculate_bp)

if __name__ == '__main__':
    app.run()
