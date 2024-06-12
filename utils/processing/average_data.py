# utils/processing/average_data.py

def calculate_average_voltage(data):
    total_voltage = sum(float(d['tegangan']) for d in data['data'])
    return total_voltage / len(data['data'])
