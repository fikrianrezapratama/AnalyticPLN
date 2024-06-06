import json
from flask import Blueprint, jsonify, Response
from auth.auth import login
from utils.api import fetch_data, fetch_data_by_id
from utils.data_processing import process_data

main = Blueprint('main', __name__)

@main.route('/get_data', methods=['GET'])
def get_data():
    login_response = login()
    if 'token' not in login_response:
        return jsonify({"error": "Failed to authenticate"}), 401

    token = login_response['token']
    data = fetch_data(token)
    if data is None:
        return jsonify({"error": "Failed to fetch data"}), 500
    
    response_data = {"data": data}
    response_json = json.dumps(response_data, indent=2)
    return Response(response_json, mimetype='application/json')
    # return jsonify(data)

@main.route('/get_data/<int:data_id>', methods=['GET'])
def get_data_by_id(data_id):
    login_response = login()
    if 'token' not in login_response:
        return jsonify({"error": "Failed to authenticate"}), 401

    token = login_response['token']
    data = fetch_data_by_id(token, data_id)
    if data is None:
        return jsonify({"error": "Failed to fetch data"}), 500

    response_data = {"data": data}
    response_json = json.dumps(response_data, indent=2)
    return Response(response_json, mimetype='application/json')
    # return jsonify(data)

# @main.route('/get_data', methods=['GET'])
# def get_data():
#     login_response = login()
#     if 'error' in login_response:
#         return jsonify(login_response), 401

#     token = login_response['token']
#     data = fetch_data(token)
#     if 'error' in data:
#         return jsonify(data), 500

#     return jsonify(data)

# @main.route('/get_data/<int:data_id>', methods=['GET'])
# def get_data_by_id(data_id):
#     login_response = login()
#     if 'error' in login_response:
#         return jsonify(login_response), 401

#     token = login_response['token']
#     data = fetch_data_by_id(token, data_id)
#     if 'error' in data:
#         return jsonify(data), 500

#     return jsonify(data)

@main.route('/process_data', methods=['GET'])
def process_data_route():
    """
    Process the data fetched from the API.
    """
    login_response = login()
    if 'token' not in login_response:
        return jsonify({"error": "Failed to authenticate"}), 401

    token = login_response['token']
    data = fetch_data(token)
    if data is None:
        return jsonify({"error": "Failed to fetch data"}), 500
    
    processed_data = process_data(data)
    response_json = json.dumps(processed_data, indent=2)
    return Response(response_json, mimetype='application/json')
    # return jsonify(processed_data)