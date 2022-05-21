'''
inventory.py: Contains inventory-related endpoints
'''

from flask import Blueprint

inventory = Blueprint('inventory', __name__)

# Inventory Endpoints
@inventory.route('/inventory/create', methods = ['GET', 'POST'])
def create_inventory():
    pass

@inventory.route('/inventory', methods = ['GET'])
def read_inventory():
    pass

@inventory.route('/inventory/<int:id>/update', methods = ['GET', 'POST']):
def update_inventory(id):
    pass

@inventory.route('/inventory/<int:id>/delete', methods = ['GET', 'POST'])
def delete_inventory(id):
    pass

# Warehouse Endpoints
@inventory.route('/warehouse/create', methods = ['GET', 'POST'])
def create_warehouse():
    pass

@inventory.route('/warehouse', methods = ['GET'])
def read_warehouse():
    pass

@inventory.route('/warehouse/<int:id>/update', methods = ['GET', 'POST'])
def update_warehouse(id):
    pass

@inventory.route('/warehouse/<int:id>/delete', methods = ['GET', 'POST'])
def delete_warehouse(id):
    pass
