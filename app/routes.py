import json
import logging
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

@main.route('/process_data', methods=['GET'])
def process_data_route():
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
    
@main.route('/process_data/<int:data_id>', methods=['GET'])
def process_data_route_by_id(data_id):
    login_response = login()
    if 'token' not in login_response:
        return jsonify({"error": "Failed to authenticate"}), 401

    token = login_response['token']
    data = fetch_data_by_id(token, data_id)

    if data is None:
        return jsonify({"error": "Failed to fetch data"}), 500

    processed_data = process_data(data)

    if str(data_id) not in processed_data:
        return jsonify({"error": f"No processed data found for ID {data_id}"}), 404

    response_data = {str(data_id): processed_data[str(data_id)]}
    response_json = json.dumps(response_data, indent=2)
    return Response(response_json, mimetype='application/json')
    # return jsonify(data)
    
@main.route('/data_pln', methods=['GET'])
def data_pln():
    login_response = login()
    if 'token' not in login_response:
        logging.error("Failed to authenticate: No token in login response")
        return jsonify({"error": "Failed to authenticate"}), 401

    token = login_response['token']
    data = fetch_data(token)

    if not data or 'data' not in data:
        logging.error("Fetched data is empty or does not contain 'data' key.")
        return jsonify({"error": "Failed to fetch data"}), 500

    # cek Log fetched data
    # logging.info(f"Fetched data: {data['data']}")

    processed_data = process_data(data)

    if not processed_data:
        logging.error("Processed data is empty.")
        return jsonify({"error": "Failed to process data"}), 500

    # cek Log processed data
    # logging.info(f"Processed data: {processed_data}")

    combined_data = []
    for item in data['data']:
        # logging.info(f"Processing item: {item}")  # Log each item to inspect it
        if isinstance(item, dict):
            item_id = item.get('id')
            if item_id is not None:
                processed_item = processed_data.get(str(item_id))  # Ensure the key is a string
                if processed_item:
                    fetched_item = item
                    combined_item = {
                        "id": item_id,
                        "user_id": fetched_item["user_id"],
                        "latitude": fetched_item["latitude"],
                        "longitude": fetched_item["longitude"],
                        "address": fetched_item["address"],
                        "photo": fetched_item["photo"],
                        "no_meteran": fetched_item["no_meteran"],
                        "capacity": fetched_item["capacity"],
                        "energy_kredit": fetched_item["energy_kredit"],
                        "tegangan": fetched_item["tegangan"],
                        "arus": fetched_item["arus"],
                        "power_limit": fetched_item["power_limit"],
                        "power_factor": fetched_item["power_factor"],
                        "phase_current_rms": fetched_item["phase_current_rms"],
                        "neutral_current_rms": fetched_item["neutral_current_rms"],
                        "tampering_status": fetched_item["tampering_status"],
                        "terminal_covers_open": fetched_item["terminal_covers_open"],
                        "meter_covers_open": fetched_item["meter_covers_open"],
                        "power_outages": fetched_item["power_outages"],
                        "kwh_credit_tokens_received": fetched_item["kwh_credit_tokens_received"],
                        "technical_tokens_received": fetched_item["technical_tokens_received"],
                        "tariff_index": fetched_item["tariff_index"],
                        "read_code": fetched_item["read_code"],
                        "lcd_condition": fetched_item["lcd_condition"],
                        "terminal_quantity": fetched_item["terminal_quantity"],
                        "seal_status": fetched_item["seal_status"],
                        "meter_location": fetched_item["meter_location"],
                        "user": fetched_item["user"],
                        "created_at": fetched_item["created_at"],
                        "status": processed_item["Hasil Analisis"]["status"],
                        "message": processed_item["Hasil Analisis"]["message"]
                    }
                    combined_data.append(combined_item)
                else:
                    logging.error(f"Processed data for ID {item_id} not found.")
            else:
                logging.error(f"Item ID is None: {item}")
        else:
            logging.error(f"Item is not a dictionary: {item}")

    if not combined_data:
        logging.error("No combined data created.")
        return jsonify({"error": "No combined data created"}), 500

    response_data = {"data": combined_data}
    response_json = json.dumps(response_data, indent=2)
    return Response(response_json, mimetype='application/json')


@main.route('/data_pln/<int:data_id>', methods=['GET'])
def data_pln_by_id(data_id):
    login_response = login()
    if 'token' not in login_response:
        return jsonify({"error": "Failed to authenticate"}), 401

    token = login_response['token']
    data_response = fetch_data_by_id(token, data_id)

    if data_response is None:
        return jsonify({"error": "Failed to fetch data"}), 500

    fetched_item = data_response.get('data', {})
    if not fetched_item:
        return jsonify({"error": "No data found"}), 404

    # cek Log fetched_item
    # logging.info(f"Fetched item: {fetched_item}")

    # Wrap the fetched_item in a dictionary with a "data" key
    processed_data = process_data({"data": fetched_item})

    # cek Log processed_data
    # logging.info(f"Processed data: {processed_data}")

    if str(data_id) not in processed_data:
        return jsonify({"error": f"No processed data found for ID {data_id}"}), 404

    processed_item = processed_data[str(data_id)]

    # cek Log the processed_item
    # logging.info(f"Processed item: {processed_item}")

    combined_item = {
        "id": fetched_item.get("id", "N/A"),
        "user_id": fetched_item.get("user_id", "N/A"),
        "latitude": fetched_item.get("latitude", "N/A"),
        "longitude": fetched_item.get("longitude", "N/A"),
        "address": fetched_item.get("address", "N/A"),
        "photo": fetched_item.get("photo", "N/A"),
        "no_meteran": fetched_item.get("no_meteran", "N/A"),
        "capacity": fetched_item.get("capacity", "N/A"),
        "energy_kredit": fetched_item.get("energy_kredit", "N/A"),
        "tegangan": fetched_item.get("tegangan", "N/A"),
        "arus": fetched_item.get("arus", "N/A"),
        "power_limit": fetched_item.get("power_limit", "N/A"),
        "power_factor": fetched_item.get("power_factor", "N/A"),
        "phase_current_rms": fetched_item.get("phase_current_rms", "N/A"),
        "neutral_current_rms": fetched_item.get("neutral_current_rms", "N/A"),
        "tampering_status": fetched_item.get("tampering_status", "N/A"),
        "terminal_covers_open": fetched_item.get("terminal_covers_open", "N/A"),
        "meter_covers_open": fetched_item.get("meter_covers_open", "N/A"),
        "power_outages": fetched_item.get("power_outages", "N/A"),
        "kwh_credit_tokens_received": fetched_item.get("kwh_credit_tokens_received", "N/A"),
        "technical_tokens_received": fetched_item.get("technical_tokens_received", "N/A"),
        "tariff_index": fetched_item.get("tariff_index", "N/A"),
        "read_code": fetched_item.get("read_code", "N/A"),
        "lcd_condition": fetched_item.get("lcd_condition", "N/A"),
        "terminal_quantity": fetched_item.get("terminal_quantity", "N/A"),
        "seal_status": fetched_item.get("seal_status", "N/A"),
        "meter_location": fetched_item.get("meter_location", "N/A"),
        "user": fetched_item.get("user", "N/A"),
        "created_at": fetched_item.get("created_at", "N/A"),
        "status": processed_item.get("Hasil Analisis", {}).get("status", "N/A"),
        "message": processed_item.get("Hasil Analisis", {}).get("message", "N/A")
    }

    response_data = {"data": combined_item}
    response_json = json.dumps(response_data, indent=2)
    return Response(response_json, mimetype='application/json')