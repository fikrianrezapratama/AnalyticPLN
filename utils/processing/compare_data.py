# utils/processing/compare_data.py

def compare_data(data, threshold):
    """
    Compare data based on a given threshold.

    Args:
        data (dict): The raw data from the API.
        threshold (float): The threshold for comparison (e.g., voltage).

    Returns:
        list: Data entries where voltage is above the threshold.
    """
    return [d for d in data['data'] if float(d['tegangan']) > threshold]
