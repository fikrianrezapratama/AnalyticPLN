# utils/processing/filter_data.py

def filter_data(data, condition):
    """
    Filter the data based on a given condition.

    Args:
        data (dict): The raw data from the API.
        condition (int): The condition to filter by (e.g., lcd_condition).

    Returns:
        list: Filtered data.
    """
    return [d for d in data['data'] if d['lcd_condition'] == condition]
