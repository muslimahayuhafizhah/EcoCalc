from faktor_emisi import FAKTOR_EMISI
from validator import input_angka
from logger import log

def hitung_listrik():
    kwh = input_angka("Masukkan penggunaan listrik (kWh): ")
    emisi = kwh * FAKTOR_EMISI["listrik"]
    print(f"✅ Emisi listrik: {emisi:.2f} kg CO2")
    log(f"Menghitung emisi listrik: {kwh} -> {emisi}")
    return emisi

