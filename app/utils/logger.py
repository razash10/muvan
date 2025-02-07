import logging
import os
from flask import jsonify

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a file handler
file_handler = logging.FileHandler('logs/errors.log')
file_handler.setLevel(logging.ERROR)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

def logger_decorator(f):
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {f.__name__}: {e}")
            return jsonify({"error": "Internal Server Error"}), 500
    wrapper.__name__ = f.__name__
    return wrapper