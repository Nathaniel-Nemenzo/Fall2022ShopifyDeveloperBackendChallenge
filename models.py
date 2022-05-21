from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy DB
db = SQLAlchemy()

'''
DB Design:
    - Each inventory item can belong in multiple warehouses
    - Each warehouse can hold multiple inventory items
    - Therefore, we must establish a many-many relationship between inventory items and warehouses
'''

# Define the join-table
allocations = db.Table('allocations',
    db.Column('inventory_id', db.Integer, db.ForeignKey('inventory.id'), primary_key = True),
    db.Column('warehouse_id', db.Integer, db.ForeignKey('warehouse.id'), primary_key = True)
)

class Inventory(db.model):
    __tablename__ = "inventory"

    id = db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.String())
    product_description = db.Column(db.String())
    product_unit = db.Column(db.String())
    product_price = db.Column(db.Float)
    product_quantity = db.Column(db.Integer)
    other_details = db.Column(db.String())

    allocations = db.relationship('Warehouse', secondary = allocations, backref = db.backref('inventory'))

class Warehouse(db.model):
    __tablename__ = 'warehouse'

    id = db.Column(db.Integer, primary_key = True)
    warehouse_name = db.Column(db.String())
    warehouse_description = db.Column(db.String())
    warehouse_location = db.Column(db.String())
    warehouse_status = db.Column(db.Boolean)