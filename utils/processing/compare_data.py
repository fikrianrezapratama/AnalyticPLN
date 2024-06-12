# utils/processing/compare_data.py

def compare_data(data, threshold):
    return [d for d in data['data'] if float(d['tegangan']) > threshold]
