from flask import Flask
from flask_cors import CORS

from routes.auth.auth import auth
from routes.money.money import money
from routes.store.store import store
from routes.inventory.inventory import inventory

# Create a flask app
app = Flask(__name__)

# Add prefix of /api to all routes
URL_PREFIX = "/api"

# Register blueprints of modules
app.register_blueprint(auth, url_prefix=URL_PREFIX)
app.register_blueprint(money, url_prefix=URL_PREFIX)
app.register_blueprint(store, url_prefix=URL_PREFIX)
app.register_blueprint(inventory, url_prefix=URL_PREFIX)

# CORS configuration
cors = CORS(app, resources={r"/*": { "origins": "http://localhost:8080"}}) # allow frontend to access API

########################################
# Run your flask app on port 80
if __name__ == "__main__":
  app.run(port=80, debug=True)