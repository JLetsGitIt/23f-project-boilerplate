from flask import Blueprint, request, jsonify, make_response
import json
from src import db

feedback = Blueprint('feedback', __name__)

# Get all feedback from the DB
@feedback.route('/feedback', methods=['GET'])
def get_feedback():
    cursor = db.get_db().cursor()
    cursor.execute('select toy_id, customer_id, feedback_id, date, rating')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@feedback.route('/feedback', methods=['POST'])
def add_new_feedback(data):
    # collecting data from the request object
    data = request.json
    current_app.logger.info(data)

    # extracting the variables
    toy = data['toy_id']
    customer = data['customer_id']
    feedback_id = data['feedback_id']
    date = data['date']
    rating = data['rating']

    # Constructing the query
    query = 'INSERT INTO feedback (toy_id, customer_id, feedback_id, date, rating) VALUES ('
    query += f'"{toy}", "{customer}", "{feedback_id}", "{date}", {rating})'
    current_app.logger.info(query)

    # executing and committing the insert statement
    cursor = get_db().cursor()
    cursor.execute(query)
    get_db().commit()

    return 'Success!'

# Changes rating 
@feedback.route('/editFeedback/<feedbackID>', methods=['PUT'])
def update_feedback(feedbackID):
    
    data = request.json
    rating = data['Rating']  # Assuming 'Rating' is the key for the rating in the JSON data
    
    # grab feedback_ID and previous feedback
    feedbackInfo = get_feedback(feedbackID)
    
    # Assuming get_feedback returns a dictionary with keys 'feedback_id' and 'rating'
    prev_rating = str(feedbackInfo['rating'])
    
    # update feedback
    feedback_query = 'UPDATE Feedback SET rating = ' + str(rating) + ' WHERE feedback_id = ' + str(feedbackID) + ';'
    
    current_app.logger.info(data)

    query = 'UPDATE Feedback SET '
    query += 'rating = ' + str(rating) + ' '
    query += 'WHERE feedback_id = {0};'.format(feedbackID)

    current_app.logger.info(query)
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    cursor.execute(feedback_query)
    db.get_db().commit()

    return "successfully edited feedback #{0}!".format(feedbackID)


# Deletes a given feedbackID
@feedback.route('/deleteFeedback/<feedbackID>', methods=['DELETE'])
def delete_feedback(feedbackID):
    query = '''
        DELETE
        FROM Feedback
        WHERE feedback_ID = {0};
    '''.format(feedbackID)
    
    # grab feedback_ID and previous rating for the given feedback
    feedbackInfo = get_feedback(feedbackID)
    
    # Assuming get_feedback returns a dictionary with keys 'feedback_ID' and 'rating'
    rating = str(feedbackInfo['rating'])
    
    # update feedback rating (assuming you want to update the rating, adjust the query accordingly)
    feedback_query = 'UPDATE Feedback SET rating = ' + str(rating) + ' WHERE feedback_ID = ' + str(feedbackID) + ';'
    
    cursor = db.get_db().cursor()
    cursor.execute(feedback_query)
    cursor.execute(query)
    
    db.get_db().commit()
    return "successfully deleted feedback #{0}!".format(feedbackID)