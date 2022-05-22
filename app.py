from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models import db
from inventory import inventory

# Create app and set DB config parameters
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Register inventory blueprint
app.register_blueprint(inventory)

# Bind DB with application
db.init_app(app)

@app.before_first_request
def create_tables():
    # TEMP: drop all before adding
    db.drop_all()
    db.create_all()

@app.route('/')
def index():
  return 'Inventory Tracking Software, look at endpoints in README.md to explore!'

if __name__ == "__main__":
    app.run(debug=True, port='3000', host='0.0.0.0')