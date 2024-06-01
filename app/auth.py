import http.client
from codecs import encode
import json
import os
import logging

logger = logging.getLogger(__name__)

def login():
    """
    Perform login to the API and return the authentication token.
    
    Returns:
        dict: JSON response containing the authentication token if successful.
    """
    try:
        conn = http.client.HTTPSConnection(os.getenv('API_HOST'))
        dataList = []
        boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
        dataList.append(encode('--' + boundary))
        dataList.append(encode('Content-Disposition: form-data; name=email;'))
        dataList.append(encode('Content-Type: text/plain'))
        dataList.append(encode(''))
        dataList.append(encode(os.getenv('EMAIL')))
        dataList.append(encode('--' + boundary))
        dataList.append(encode('Content-Disposition: form-data; name=password;'))
        dataList.append(encode('Content-Type: text/plain'))
        dataList.append(encode(''))
        dataList.append(encode(os.getenv('PASSWORD')))
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
        logger.info('Login successful')
        return json.loads(data.decode("utf-8"))
    
    except Exception as e:
            logger.error(f'Login failed: {e}')
            return {}
