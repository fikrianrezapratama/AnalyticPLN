from flask import Flask, jsonify, request
import requests
import http.client
from codecs import encode
import json

app = Flask(__name__)

# Konfigurasi URL dasar untuk API
BASE_URL = 'https://pln-probe.kopibub.uk'  # Ganti dengan URL dasar API Anda

def login():
    conn = http.client.HTTPSConnection("pln-probe.kopibub.uk")
    dataList = []
    boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=email;'))
    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))
    dataList.append(encode("admin@gmail.com"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=password;'))
    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))
    dataList.append(encode("password"))
    dataList.append(encode('--'+boundary+'--'))
    dataList.append(encode(''))
    body = b'\r\n'.join(dataList)
    payload = body
    headers = {
        'Accept': 'application/json',
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("POST", "/api/login", payload, headers)
    res = conn.getresponse()
    data = res.read()
    conn.close()
    return json.loads(data.decode("utf-8"))

@app.route('/get_data', methods=['GET'])
def get_data():
    login_response = login()
    if 'token' not in login_response:
        return jsonify({"error": "Failed to authenticate"}), 401
    
    token = login_response['token']
    api_endpoint = f"{BASE_URL}/api/device"
    
    # Permintaan GET ke API dengan header otentikasi
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'
    }
    response = requests.get(api_endpoint, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        processed_data = process_data(data)
        return jsonify(processed_data)
    else:
        return jsonify({"error": "Failed to fetch data"}), response.status_code

def process_data(data):
    return data
    
if __name__ == '__main__':
    app.run(debug=True)
