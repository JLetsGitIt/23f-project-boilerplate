from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db  

orders = Blueprint('orders', __name__)

@orders.route('/orders', methods=['GET'])
def get_orders():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM orders')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    return jsonify(json_data)

@orders.route('/orders', methods=['POST'])
def create_order():
    the_data = request.get_json()
    current_app.logger.info(the_data)

    date = the_data['date']
    toy_id = the_data['toy_id']
    customer_id = the_data['customer_id']
    quantity = the_data['quantity']
    delivery_status = the_data['delivery_status']
    price_per_item = the_data['price_per_item']
    
    query = 'insert into order (toy_id, customer_id, date, quantity, delivery_status, price_per_item) values ("'
    query += toy_id + '", "'
    query += customer_id + '", "'
    query += quantity + '", "'
    query += date + '", "'
    query += delivery_status + '", '
    query += str(price_per_item) + ')'
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


@orders.route('/orders/<int:orderID>', methods=['GET'])
def get_order(orderID):
    query = 'SELECT * FROM orders WHERE id = %s', (orderID,)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)


@orders.route('/editOrder/<orderID>', methods=['PUT'])
def update_order(orderID):
    data = request.json

    quantity = data['quantity']
    totalPrice = data['totalPrice']
    date = data['date']
    deliveryStatus = data['deliveryStatus']

    orderInfo = get_order(orderID)

    orderID = str(orderInfo['order_id'])
    prev_price = str(orderInfo['total_price'])

    price_change = float(totalPrice) - float(prev_price)

    order_query = 'UPDATE `Order` SET total_price = total_price + ' + str(price_change) + ' WHERE order_id = ' + str(orderID) + ';'

    current_app.logger.info(data)

    the_query = 'UPDATE `order` SET '
    the_query += 'quantity = "' + quantity + '", '
    the_query += 'totalPrice = "' + totalPrice + '",'
    the_query += 'date = "' + date + '", '
    the_query += 'deliveryStatus = ' + str(deliveryStatus) + ' '
    the_query += 'WHERE orderID = {0};'.format(orderID)

    current_app.logger.info(the_query)

    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    cursor.execute(order_query)
    db.get_db().commit()

    return "successfully edited order #{0}!".format(orderID)




