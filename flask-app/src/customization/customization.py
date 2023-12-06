from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


customization = Blueprint('customization', __name__)

# Get all customers from the DB
@customization.route('/customization', methods=['GET'])
def get_customization():
    cursor = db.get_db().cursor()
    cursor.execute('select customization, customization_type,\
        toyID from customers')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get customer detail for customer with particular userID
@customization.route('/customization/<optionID>', methods=['GET'])
def get_customer(optionID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from customization where id = {0}'.format(optionID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@customization.route('/customization', methods=['POST'])
def add_new_product():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    type = the_data['customization_type']
    toyID = the_data['toyID']

    # Constructing the query
    query = 'insert into products (customization_type, toyID) values ("'
    query += type + '", "'
    query += str(toyID) + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

# Changes size, price, sugar level, and/or ice level of a drink in a given order
@customization.route('/customization/<optionID>', methods=['PUT'])
def update_customization(optionID):
    
    the_data = request.json

    type = the_data['Type']
    toyID = the_data['ToyID']
    
    # grab order_id and previous drink price for the given drink
    # customizationInfo = get_customization_info(optionID)
    
    # orderID = str(drinkInfo['order_id'])
    # prev_price = str(drinkInfo['price'])
    
    # calculate price change (if any)
    # price_change = float(price) - float(prev_price)
    
    # update order total price
    # order_query = 'UPDATE `Order` SET total_price = total_price + ' + str(price_change) + ' WHERE order_id = ' + str(orderID) + ';'

    current_app.logger.info(the_data)

    the_query = 'UPDATE Customization SET '
    the_query += 'type = "' + type + '", '
    the_query += 'toyID = ' + str(toyID) + ' '
    the_query += 'WHERE option_id = {0};'.format(optionID)

    current_app.logger.info(the_query)
    
    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    # cursor.execute(order_query)
    db.get_db().commit()

    return "successfully editted customization #{0}!".format(optionID)

# Deletes a given drink
# Also reduces the corresponding order's total price
@customization.route('/customization/<optionID>', methods=['DELETE'])
def delete_customization(optionID):
    query = '''
        DELETE
        FROM Customization
        WHERE option_id = {0};
    '''.format(optionID)
    
    # grab order_id and previous drink price for the given drink
    # drinkInfo = get_drink_info(drinkID)
    
    # orderID = str(drinkInfo['order_id'])
    # price = str(drinkInfo['price'])
    
    # update order total price
    # order_query = 'UPDATE `Order` SET total_price = total_price - ' + str(price) + ' WHERE order_id = ' + str(orderID) + ';'
    
    cursor = db.get_db().cursor()
    # cursor.execute(order_query)
    cursor.execute(query)
    
    db.get_db().commit()
    return "successfully deleted customization #{0}!".format(optionID)
