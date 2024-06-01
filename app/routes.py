from flask import Blueprint, jsonify
from .auth import login
from .utils import fetch_data

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
    
    return jsonify(data)
