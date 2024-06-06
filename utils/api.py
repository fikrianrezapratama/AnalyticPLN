import requests
import os
import logging

logger = logging.getLogger(__name__)

def fetch_data(token):
    """
    Fetch data from the API using the provided token.

    Args:
        token (str): Authentication token.

    Returns:
        dict: JSON response containing the data if successful.
        None: If the request failed.
    """
    try:
        api_endpoint = f"https://{os.getenv('API_HOST')}/api/device"
        headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/json'
        }
        response = requests.get(api_endpoint, headers=headers)
        if response.status_code == 200:
            logger.info('Data fetched successfully')
            return response.json()
        else:
            logger.error(f'Failed to fetch data: {response.status_code}')
            return {"error": f"Failed to fetch data: {response.status_code}"}
    
    except Exception as e:
        logger.error(f'Exception occurred while fetching data: {e}')
        return {"error": f"Exception occurred: {e}"}
    
def fetch_data_by_id(token, data_id):
    try:
        api_endpoint = f"https://{os.getenv('API_HOST')}/api/device/{data_id}"
        headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/json'
        }
        response = requests.get(api_endpoint, headers=headers)
        if response.status_code == 200:
            logger.info(f'Data with ID {data_id} fetched successfully')
            return response.json()
        else:
            logger.error(f'Failed to fetch data with ID {data_id}: {response.status_code}')
            return {"error": f"Failed to fetch data with ID {data_id}: {response.status_code}"}
    except Exception as e:
        logger.error(f'Exception occurred while fetching data with ID {data_id}: {e}')
        return {"error": f"Exception occurred: {e}"}
