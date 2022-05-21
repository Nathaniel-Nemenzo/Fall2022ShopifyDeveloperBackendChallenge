from flask import Flask
from models import db
from inventory import inventory

# Create app and set DB config parameters
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Register inventory blueprint
app.register_blueprint(inventory)

# Initialize DB and create tables
db.init_app(app)

@app.before_first_request
def create_tables():
    # TEMP: drop all before adding
    db.drop_all()
    db.create_all()

# Run app
app.run(host = 'localhot', port = 5000)