from flask_sqlalchemy import SQLAlchemy

'''
DB Design:
    - Each inventory item can belong in multiple warehouses
    - Each warehouse can hold multiple inventory items
    - Therefore, we must establish a many-many relationship between inventory items and warehouses
'''
db = SQLAlchemy()

allocations = db.Table('allocations',
    db.Column('inventory_id', db.Integer, db.ForeignKey('inventory.id'), primary_key = True),
    db.Column('warehouse_id', db.Integer, db.ForeignKey('warehouse.id'), primary_key = True)
)

class Inventory(db.Model):
    __tablename__ = "inventory"

    id = db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.String())
    product_description = db.Column(db.String())
    product_unit = db.Column(db.String())
    product_price = db.Column(db.Float)
    product_quantity = db.Column(db.Integer)
    other_details = db.Column(db.String())

    allocations = db.relationship('Warehouse', secondary = allocations, backref = db.backref('inventory'))

    def __init__(self, product_name, product_description, product_unit, product_price, product_quantity, other_details):
        self.product_name = product_name
        self.product_description = product_description
        self.product_unit = product_unit
        self.product_price = product_price
        self.product_quantity = product_quantity
        self.other_details = other_details

class Warehouse(db.Model):
    __tablename__ = 'warehouse'

    id = db.Column(db.Integer, primary_key = True)
    warehouse_name = db.Column(db.String())
    warehouse_description = db.Column(db.String())
    warehouse_location = db.Column(db.String())
    warehouse_status = db.Column(db.Boolean)

    def __init__(self, warehouse_name, warehouse_description, warehouse_location, warehouse_status):
        self.warehouse_name = warehouse_name
        self.warehouse_description = warehouse_description
        self.warehouse_location = warehouse_location
        self.warehouse_status = warehouse_status