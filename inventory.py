'''
inventory.py: Contains inventory-related endpoints
'''

from flask import Blueprint, request, render_template, redirect, abort
from models import Inventory, Warehouse, db

inventory = Blueprint('inventory', __name__)

# Inventory Endpoints
@inventory.route('/inventory/create', methods = ['GET', 'POST'])
def create_inventory():
    if request.method == 'GET':
        return render_template('inventory/create.html')

    if request.method == 'POST':
        product_name = request.form['product_name']
        product_description = request.form['product_description']
        product_unit = request.form['product_unit']
        product_price = request.form['product_price']
        product_quantity = request.form['product_quantity']
        other_details = request.form['other_details']
        inventory = Inventory(product_name, product_description, product_unit, product_price, product_quantity, other_details)
        db.session.add(inventory)
        db.session.commit()
        return redirect('/inventory')

@inventory.route('/inventory', methods = ['GET'])
def read_inventory():
    inventories = Inventory.query.all()
    return render_template('inventory/read.html', inventories = inventories)

@inventory.route('/inventory/<int:id>')
def read_single_inventory(id):
    inventory = Inventory.query.filter_by(id = id).first()
    if inventory:
        return render_template('inventory/read_single.html', inventory = inventory)
    return f'Inventory item with id {id} does not exist.'

@inventory.route('/inventory/<int:id>/update', methods = ['GET', 'POST'])
def update_inventory(id):
    inventory = Inventory.query.filter_by(id = id).first()
    if request.method == 'POST':
        if inventory:
            db.session.delete(inventory)
            db.session.commit()

            product_name = request.form['product_name']
            product_description = request.form['product_description']
            product_unit = request.form['product_unit']
            product_price = request.form['product_price']
            product_quantity = request.form['product_quantity']
            other_details = request.form['other_details']
            inventory = Inventory(product_name, product_description, product_unit, product_price, product_quantity, other_details)

            db.session.add(inventory)
            db.session.commit()

            return redirect(f'/inventory/{id}')
    return render_template('inventory/update.html', inventory = inventory)

@inventory.route('/inventory/<int:id>/delete', methods = ['GET', 'POST'])
def delete_inventory(id):
    inventory = Inventory.query.filter_by(id = id).first()
    if request.method == 'POST':
        if inventory:
            db.session.delete(inventory)
            db.session.commit()
            return redirect('/inventory')
        abort(404)
    return render_template('inventory/delete.html')

# Warehouse Endpoints
@inventory.route('/warehouse/create', methods = ['GET', 'POST'])
def create_warehouse():
    return 'Warehouse Create'

@inventory.route('/warehouse', methods = ['GET'])
def read_warehouse():
    return 'Warehouse Read'

@inventory.route('/warehouse/<int:id>/update', methods = ['GET', 'POST'])
def update_warehouse(id):
    return 'Warehouse Update'

@inventory.route('/warehouse/<int:id>/delete', methods = ['GET', 'POST'])
def delete_warehouse(id):
    return 'Warehouse Delete'
