from flask import Blueprint, request, jsonify, make_response
import json
from src import db


toy = Blueprint('toy', __name__)

# Get all customers from the DB
@toy.route('/toy', methods=['GET'])
def get_toy():
    cursor = db.get_db().cursor()
    cursor.execute('select toy, name,\
        engagement_level, age_range, description, price, \
            safety_rating, suitability_for_special_needs, material_type, \
                educational_value, category from customers')
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
@toy.route('/toy/<toyID>', methods=['GET'])
def get_customer(userID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from toy where id = {0}'.format(toyID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response