from flask import Blueprint, request, jsonify, make_response
from src import db  # Import your database module

gift_wrapping = Blueprint('gift_wrapping', __name__)



@gift_wrapping.route('/gift_wrapping_services', methods=['GET'])
def get_gift_wrapping_services():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM gift_wrapping_service')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


@gift_wrapping.route('/gift_wrapping_services', methods=['POST'])
def create_gift_wrapping_service():
    data = request.get_json()
    current_app.logger.info(the_data)

    custom_message = the_data['custom_message']
    wrapping_options = the_data['wrapping_options']
    service_id = the_data['service_id']
  

    query = 'insert into order (custom_message, service_id, wrapping_options) values ("'
    query += custom_message + '", "'
    query += service_id + '", "'
    query += wrapping_options + '", '
    current_app.logger.info(query)



@gift_wrapping.route('/gift_wrapping_services/<int:serviceID>', methods=['GET'])
def get_gift_wrapping_service(serviceID):
    query = ‘SELECT * FROM gift_wrapping_service WHERE service_id = %s', (serviceID,)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)


@gift_wrapping.route('/gift_wrapping_services/<int:serviceID>', methods=['DELETE'])
def delete_order(orderID):
        query = ''DELETE FROM gift_wrapping_service WHERE service_id = %s
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        
        db.get_db().commit()
        
        return "successfully deleted gift_wrapping_service #{0}!".format(serviceID)


