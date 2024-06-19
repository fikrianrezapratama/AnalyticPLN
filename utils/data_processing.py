from utils.processing.filter_data import filter_data
from utils.processing.compare_data import compare_data
from utils.processing.average_data import calculate_average_voltage
from utils.processing.processing_so import (
    kriteria1, kriteria2, kriteria3, kriteria4, 
    kriteria5, kriteria6, kriteria7, kriteria8, 
    kriteria9, kriteria10, kriteria11, kriteria12,
    kriteria13, 
    analisis_akhir
)

def process_data(data, data_id=None):
    hasil = {}
    
    if isinstance(data["data"], dict):
        if data_id is None or data_id == data["data"]["id"]:
            hasil[str(data["data"]["id"])] = {
                "Kriteria 1": kriteria1(data["data"]),
                "Kriteria 2": kriteria2(data["data"]),
                "Kriteria 3": kriteria3(data["data"]),
                "Kriteria 4": kriteria4(data["data"]),
                "Kriteria 5": kriteria5(data["data"]),
                # "Kriteria 6": kriteria6(data["data"]),
                "Kriteria 7": kriteria7(data["data"]),
                "Kriteria 8": kriteria8(data["data"]),
                "Kriteria 9": kriteria9(data["data"]),
                "Kriteria 10": kriteria10(data["data"]),
                # "Kriteria 11": kriteria11(data["data"]),
                # "Kriteria 12": kriteria12(data["data"]),
                "Kriteria 13": kriteria13(data["data"]),
                "Hasil Analisis": analisis_akhir(data["data"])
            }
    else:
        for entry in data["data"]:
            if data_id is None or data_id == entry["id"]:
                hasil[str(entry["id"])] = {
                    "Kriteria 1": kriteria1(entry),
                    "Kriteria 2": kriteria2(entry),
                    "Kriteria 3": kriteria3(entry),
                    "Kriteria 4": kriteria4(entry),
                    "Kriteria 5": kriteria5(entry),
                    # "Kriteria 6": kriteria6(entry),
                    "Kriteria 7": kriteria7(entry),
                    "Kriteria 8": kriteria8(entry),
                    "Kriteria 9": kriteria9(entry),
                    "Kriteria 10": kriteria10(entry),
                    # "Kriteria 11": kriteria11(entry),
                    # "Kriteria 12": kriteria12(entry),
                    "Kriteria 13": kriteria13(entry),
                    "Hasil Analisis": analisis_akhir(entry)
                }
    return hasil
