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
        warehouses = Warehouse.query.all()
        return render_template('inventory/create.html', warehouses = warehouses)

    if request.method == 'POST':
        product_name = request.form['product_name']
        product_description = request.form['product_description']
        product_unit = request.form['product_unit']
        product_price = request.form['product_price']
        product_quantity = request.form['product_quantity']
        other_details = request.form['other_details']

        # Parse the warehouses
        warehouses = request.form['warehouse_allocation']
        warehouses = warehouses.split(',')

        # Make sure all the warehouses are present
        if warehouses[0] != '':
            for warehouse in warehouses:
                if not Warehouse.query.filter_by(id = warehouse).first():
                    return f'Warehouse ID does not exist.'

        # Add the warehouses to inventory
        inventory = Inventory(product_name, product_description, product_unit, product_price, product_quantity, other_details)
        if warehouses[0] != '':
            for warehouse in warehouses:
                inventory.warehouses.append(Warehouse.query.filter_by(id = warehouse).first())
                
        db.session.add(inventory)
        db.session.commit()
        return redirect('/inventory')

@inventory.route('/inventory', methods = ['GET'])
def read_inventory():
    inventories = Inventory.query.all()
    return render_template('inventory/read.html', inventories = inventories)

@inventory.route('/inventory/<int:id>', methods = ['GET'])
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
    if request.method == 'GET':
        inventories = Inventory.query.all()
        return render_template('warehouse/create.html', inventories = inventories)

    if request.method == 'POST':
        warehouse_name = request.form['warehouse_name']
        warehouse_description = request.form['warehouse_description']
        warehouse_location = request.form['warehouse_location']
        warehouse_status = True if request.form.get('warehouse_status', '') else False

        # Parse the inventories
        inventories = request.form['inventory_allocation']
        inventories = inventories.split(',')

        # Make sure all the warehouses are present
        if inventories[0] != '':
            for inventory in inventories:
                if not Inventory.query.filter_by(id = inventory).first():
                    return f'Inventory ID does not exist.'

        warehouse = Warehouse(warehouse_name, warehouse_description, warehouse_location, warehouse_status)
        if inventories[0] != '':
            for inventory in inventories:
                warehouse.inventories.append(Inventory.query.filter_by(id = inventory).first())

        db.session.add(warehouse)
        db.session.commit()
        return redirect('/warehouse')

@inventory.route('/warehouse', methods = ['GET'])
def read_warehouse():
    warehouses = Warehouse.query.all()
    return render_template('warehouse/read.html', warehouses = warehouses)

@inventory.route('/warehouse/<int:id>', methods = ['GET'])
def read_single_warehouse(id):
    warehouse = Warehouse.query.filter_by(id = id).first()
    if warehouse:
        return render_template('warehouse/read_single.html', warehouse = warehouse)
    return f'Warehouse with id {id} does not exist.'

@inventory.route('/warehouse/<int:id>/update', methods = ['GET', 'POST'])
def update_warehouse(id):
    warehouse = Warehouse.query.filter_by(id = id).first()
    if request.method == 'POST':
        if warehouse:
            db.session.delete(warehouse)
            db.session.commit()

        warehouse_name = request.form['warehouse_name']
        warehouse_description = request.form['warehouse_description']
        warehouse_location = request.form['warehouse_location']
        warehouse_status = True if request.form.get('warehouse_status', '') else False
        warehouse = Warehouse(warehouse_name, warehouse_description, warehouse_location, warehouse_status)
       
        db.session.add(warehouse)
        db.session.commit()
        return redirect(f'/warehouse/{id}')
    return render_template('warehouse/update.html', warehouse = warehouse)

@inventory.route('/warehouse/<int:id>/delete', methods = ['GET', 'POST'])
def delete_warehouse(id):
    warehouse = Warehouse.query.filter_by(id = id).first()
    if request.method == 'POST':
        if warehouse:
            db.session.delete(warehouse)
            db.session.commit()
            return redirect('/warehouse')
        abort(404)
    return render_template('warehouse/delete.html')
