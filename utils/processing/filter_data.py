# utils/processing/filter_data.py

def filter_data(data, condition):
    return [d for d in data['data'] if d['lcd_condition'] == condition]
