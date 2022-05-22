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

if __name__ == "__main__":
    app.run(host = 'localhost', port = 5000)