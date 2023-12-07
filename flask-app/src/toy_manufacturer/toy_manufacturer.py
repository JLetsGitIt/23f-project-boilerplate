from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

toy_manufacturer = Blueprint('toy_manufacturer', __name__)


# Get all the manufacturing from the database
@toy_manufacturer.route('/toy_manufacturer', methods=['GET'])
def get_toy_manufacturer():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT manufacturer_id, name, location, sustainability_score, environmental_policies FROM toy_manufacturer')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@toy_manufacturer.route('/toy_manufacturer/<manufacturer_id>', methods=['GET'])
def get_manufacturing_detail (id):

    query = 'SELECT manufacturer_id, name, location, sustainability_score, environmental_policies FROM toy_manufacturer WHERE id = ' + str(toy_manufacturer)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

