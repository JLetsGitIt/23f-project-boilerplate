#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
toy_safety_information
"""

from flask import Blueprint, request, jsonify, make_response
import json
from src import db

toy_safety = Blueprint('toy_safety_information', __name__)

# Get all toy safety information
@toy_safety.route('/toy_safety_information', methods=['GET'])
def get_all_toy_safety():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM toy_safety_information')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get toy safety information by safety id
@toy_safety.route('/toysafety/<safety_id>', methods=['GET'])
def get_toy_safety_by_id(safety_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM toy_safety_information WHERE safety_id =' + safety_id)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


