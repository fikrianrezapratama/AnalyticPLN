
# utils/data_processing.py
from utils.processing.filter_data import filter_data
from utils.processing.compare_data import compare_data
from utils.processing.average_data import calculate_average_voltage
from utils.processing.processing_so import kriteria1, kriteria2,kriteria3, kriteria4, kriteria5, kriteria6, kriteria7, kriteria8, kriteria9, kriteria10, kriteria11, kriteria12, analisis_akhir

# def process_data(data):
#     """
#     Process the data from the API using various methods.

#     Args:
#         data (dict): The raw data from the API.

#     Returns:
#         dict: Processed data including summaries and filters.
#     """
#     filtered_data = filter_data(data, condition=1)
#     compared_data = compare_data(data, threshold=220.0)
#     average_voltage = calculate_average_voltage(data)
    
#     return {
#         'filtered_data': filtered_data,
#         'compared_data': compared_data,
#         'average_voltage': average_voltage
#     }

def process_data(data):
    hasil = {}
    if isinstance(data["data"], dict):
        hasil["Kriteria 1"] = kriteria1(data["data"])
        hasil["Kriteria 2"] = kriteria2(data["data"])
        hasil["Kriteria 3"] = kriteria3(data["data"])
        hasil["Kriteria 4"] = kriteria4 (data["data"])
        # hasil["Kriteria 5"] = kriteria5 (data["data"])
        # hasil["Kriteria 6"] = kriteria6 (data["data"])
        hasil["Kriteria 7"] = kriteria7 (data["data"])
        hasil["Kriteria 8"] = kriteria8 (data["data"])
        hasil["Kriteria 9"] = kriteria9 (data["data"])
        hasil["Kriteria 10"] = kriteria10 (data["data"])
        # hasil["Kriteria 11"] = kriteria11 (data["data"])
        # hasil["Kriteria 12"] = kriteria12 (data["data"])
        hasil["Hasil Analisis"] = analisis_akhir (data["data"])
        
    else:
        for entry in data["data"]:
            hasil[entry["id"]] = {
                "Kriteria 1": kriteria1(entry), #sisa KWH tidak wajar (diatas>1000kwH)
                "Kriteria 2": kriteria2(entry), #Tegangan = 0, Arus>0,1
                "Kriteria 3": kriteria3(entry), #Arus = 0, Tegangan>180V, Faktor Daya = 0,1 - 0.9
                "Kriteria 4": kriteria4(entry), #LCD Rusak, Error, Blank
                # "Kriteria 5": kriteria5(entry), #Keypad Rusak
                # "Kriteria 6": kriteria6(entry), #Kondisi rumah berpenghuni tetapi arus = 0
                "Kriteria 7": kriteria7(entry), #Frekuensi input CT yang tinggi
                "Kriteria 8": kriteria8(entry), #Tutup terminal dibuka
                "Kriteria 9": kriteria9(entry), #status Tampering (1, 2, 4, 5)
                "Kriteria 10": kriteria10(entry), #Arus netral > arus fasa
                # "Kriteria 11": kriteria11(entry), #Arus > 0, Terakhir beli token lebih dari 3 bulan, kondisi LCD "Periksa"
                # "Kriteria 12": kriteria12(entry), #Energi kumulatif tetap, jumlah input token tinggi
                "Hasil Analisis": analisis_akhir(entry)
            } 
    return hasil