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
            return None
    
    except Exception as e:
        logger.error(f'Exception occurred while fetching data: {e}')
        return None
