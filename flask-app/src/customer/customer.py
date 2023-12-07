from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

customer = Blueprint('customer', __name__)

# Get all customers from the DB
@customer.route('/customer', methods=['GET'])
def get_customer():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * from customers')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@customer.route('/customer', methods=['POST'])
def add_new_customer():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    f_name = the_data['first_name']
    l_name = the_data['last_name']
    s_address = the_data['street_address']
    city = the_data['city']
    zip_code = the_data['zip_code']
    country = the_data['country']
    email = the_data['email']
    number = the_data['phone_number']
    access = the_data['accessibility_needs']
    role = the_data['cust_role']
    c_ages = the_data['customer_child_ages']
    c_interests = the_data['customer_child_interests']

    # Constructing the query
    query = 'insert into customer (customer_id, first_name, last_name, street_address, city, zip_code, country, email, phone_number, accessibility_needs,cust_role children_ages, children_interests) values ("'
    query += f_name + '", "'
    query += l_name + '", "'
    query += s_address + '", "'
    query += city + '", '
    query += zip_code + '", '
    query += country + '", '
    query += email + '", '
    query += number + '", '
    query += access + '", '
    query += role + '", '
    query += c_ages + '", '
    query += c_interests + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

@customer.route('/customer/<customer_id>', methods=['GET'])
def get_customer_detail (customer_id):

    query = 'SELECT * FROM customers WHERE customer_id = ' + str(customer_id)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@customer.route('/customer/<customer_id>', methods=['PUT'])
def update_customer(customer_id):
    
    the_data = request.json

    f_name = the_data['first_name']
    l_name = the_data['last_name']
    s_address = the_data['street_address']
    city = the_data['city']
    zip_code = the_data['zip_code']
    country = the_data['country']
    email = the_data['email']
    number = the_data['phone_number']
    access = the_data['accessibility_needs']
    role = the_data['cust_role']
    c_ages = the_data['customer_child_ages']
    c_interests = the_data['customer_child_interests']
    
    # grab customer_id and previous drink price for the given drink
    customerInfo = get_customer_detail(customer_id)
    
    current_app.logger.info(the_data)

    query = 'UPDATE customer SET'
    query += f_name + '", "'
    query += l_name + '", "'
    query += s_address + '", "'
    query += city + '", '
    query += zip_code + '", '
    query += country + '", '
    query += email + '", '
    query += number + '", '
    query += access + '", '
    query += role + '", '
    query += c_ages + '", '
    query += c_interests + ' '
    query += 'WHERE customer_id = {0};'.format(customer_id)

    current_app.logger.info(query)
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return "successfully editted drink #{0}!".format(customer_id)


