# utils/processing/average_data.py

def calculate_average_voltage(data):
    """
    Calculate the average voltage from the data.

    Args:
        data (dict): The raw data from the API.

    Returns:
        float: The average voltage.
    """
    total_voltage = sum(float(d['tegangan']) for d in data['data'])
    return total_voltage / len(data['data'])
