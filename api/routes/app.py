from flask import Flask
from flask_cors import CORS

from user import user
from money import money
from store import store
from inventory import inventory

# Create a flask app
app = Flask(__name__)

# Add prefix of /api to all routes
URL_PREFIX = "/api"

# Register blueprints of modules
app.register_blueprint(user, url_prefix=URL_PREFIX)
app.register_blueprint(money, url_prefix=URL_PREFIX)
app.register_blueprint(store, url_prefix=URL_PREFIX)
app.register_blueprint(inventory, url_prefix=URL_PREFIX)

# CORS configuration
cors = CORS(app, resources={
    r"/*": { 
        # "origins": ["http://localhost:8080", "https://moneygame-frontend.herokuapp.com"]
        "origins": ["*"]
        }
    }, 
    supports_credentials=True) # allow frontend to access API

if __name__ == "__main__":
  app.run(port=5000, debug=True)