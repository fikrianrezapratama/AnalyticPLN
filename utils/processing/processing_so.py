#processing SO
import datetime

#sisa KWH tidak wajar (diatas>1000kwH)
def kriteria1(data):
    if float(data["energy_kredit"]) > 1000:
        return {"status": "SO", "message": "Sisa KWH tidak wajar"}
    else:
        return {"status": "Normal", "message": "Sisa KWH normal"}

#Tegangan = 0, Arus>0,1
def kriteria2(data):
    if float(data["tegangan"]) == 0 and (data["arus"]) > 0.1:
        return {"status": "SO", "message": "Tegangan tidak normal"}
    else:
        return {"status": "Normal", "message": "Tegangan normal"}

#Arus = 0, Tegangan>180V, Faktor Daya = 0,1 - 0.9
def kriteria3(data):
    
    return data["Tegangan rms (V)"] > 180 and data["Arus rms"] >= 0 and 0.05 <= data["Faktor data (cos phi)"] <= 0.95

#LCD Rusak, Error, Blank
def kriteria4(data):
    if float(data["lcd_condition"]) == 1:
        return {"status": "Normal", "message": "LCD normal"}
    else:
        return {"status": "SO", "message": "LCD rusak"}

#Keypad Rusak
def kriteria5(data):
    if float(data["keypad_condition"]) == 1:
        return {"status": "Normal", "message": "Keypad normal"}
    else:
        return {"status": "SO", "message": "Keypad rusak"}

# #Kondisi rumah berpenghuni tetapi arus = 0
# def kriteria6(data):
#     return data["Kondisi Rumah"] == "Berpenghuni" and data["Arus rms"] == 0

# #Frekuensi input CT yang tinggi
# def kriteria7(data):
#     return data["Jumlah token teknikal"] > 1

# #Tutup terminal dibuka
# def kriteria8(data):
#     return data["Jumlah tutup terminal dibuka"] > 0

#status Tampering (1, 2, 4, 5)
def kriteria9(data):
    tampering_status = data.get("status_tampering" , "")
    statuses = tampering_status.split("_")
    
    valid_statuses = [1, 2, 4, 5]
    result_statuses = [int(status) for status in statuses if status.isdigit() and int(status) in valid_statuses]
    
    if result_statuses:
        return {
            "status": "SO",
            "message": f"status tampering {', '.join(map(str, result_statuses))}"
        }
    else:
        return {"status": "Normal", "message": "Tidak ada masalah tampering"}

# #Arus netral > arus fasa
# def kriteria10(data):
#     return data["Arus netral"] > data["Arus fase"]

# #Arus > 0, Terakhir beli token lebih dari 3 bulan, kondisi LCD "Periksa"
# def kriteria11(data):
#     last_token_date = datetime.datetime.strptime(data["Waktu last token kredit"], '%Y-%m-%d')
#     current_date = datetime.datetime.strptime(data["Tanggal saat ini"], '%Y-%m-%d')
#     return data["Arus rms"] > 0 and (current_date - last_token_date).days > 90

# #Energi kumulatif tetap, jumlah input token tinggi
# def kriteria12(data):
#     return data["Energi kWh kumulatif"] == 0 and data["Jumlah token kredit kWh diterima"] > 10
