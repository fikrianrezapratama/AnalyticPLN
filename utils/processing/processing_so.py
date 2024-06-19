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
    if float(data["arus"]) == 0 and float(data["tegangan"]) >= 180 and 0.1 <= float(data["power_factor"]) <= 0.9:
        return {"status": "SO", "message": "Arus tidak normal"}
    else:
        return {"status": "Normal", "message": "Arus normal"}

#LCD Rusak, Error, Blank
def kriteria4(data):
    if float(data["lcd_condition"]) <= 3:
        return {"status": "Normal", "message": "LCD normal"}
    else:
        return {"status": "SO", "message": "LCD rusak"}

#Keypad Rusak
def kriteria5(data):
    if float(data["keyped_condition"]) <= 3: #belum ada data keypad
        return {"status": "Normal", "message": "Keypad normal"}
    else:
        return {"status": "SO", "message": "Keypad rusak"}

#Kondisi rumah berpenghuni tetapi arus = 0
def kriteria6(data):
    if float(data["arus"]) == 0 and float(data["rumah_berpenghuni"]) == 1: #belum ada data rumah berpenghuni
        return {"status": "SO", "message": "Kondisi rumah berpenghuni tetapi arus = 0"}
    else:
        return {"status": "Normal", "message": "Kondisi rumah berpenghuni tetapi arus = 0"}


#Frekuensi input CT yang tinggi
def kriteria7(data):
    if float(data["technical_tokens_received"]) > 1:
        return {"status": "SO", "message": "Frekuensi input CT yang tinggi"}
    else:
        return {"status": "Normal", "message": "Frekuensi input CT normal"}

#Tutup terminal dibuka
def kriteria8(data):
    if float(data["terminal_covers_open"]) > 2:
        return {"status": "SO", "message": "Tutup terminal pernah dibuka"}
    else:
        return {"status": "Normal", "message": "Tutup terminal tertutup"}

#status Tampering (1, 2, 4, 5) perlu konfirmasi
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
def kriteria10(data):
    if float(data["neutral_current_rms"]) > float(data["phase_current_rms"]):
        return {"status": "SO", "message": "Arus netral > arus fasa"}
    else:
        return {"status": "Normal", "message": "Arus netral <= arus fasa"}


#Arus > 0, Terakhir beli token lebih dari 3 bulan, kondisi LCD "Periksa" (data nya ada tetapi belum ditambahkan)
def kriteria11(data):
    last_token_date = datetime.datetime.strptime(data["Waktu last token kredit"], '%Y-%m-%d') #belum ada tanggal terakhir isi token
    current_date = datetime.datetime.strptime(data["created_at"], '%Y-%m-%d')
    return data["arus"] > 0 and (current_date - last_token_date).days > 90

#Energi kumulatif tetap, jumlah input token tinggi
def kriteria12(data):
    # data 2 energy_credit
    # data 25 kwh_credit_tokens_received
    return data["Energi kWh kumulatif"] == 0 and data["Jumlah token kredit kWh diterima"] > 10

#Kondisi Segel
def kriteria13(data):
    if float(data["seal_status"]) == 2:
        return {"status": "Normal", "message": "Segel normal"}
    
    elif float(data["seal_status"]) == 1:
        return {"status": "SO", "message": "Seal rusak"}
    
    else:
        return {"status": "SO", "message": "Seal tidak ada"}

#analisis_akhir
def analisis_akhir(data):
    kriteria_list = [kriteria1, kriteria2, kriteria3, kriteria4, kriteria7, kriteria8, kriteria9, kriteria10]
    messages = []
    
    for kriteria in kriteria_list:
        hasil = kriteria(data)
        if hasil["status"] == "SO":
            messages.append(hasil["message"])
    
    if messages:
        return {"status": "SO", "message": f"{', '.join(messages)}"}
    
    return {"status": "Normal", "message": "Semua parameter normal"}
