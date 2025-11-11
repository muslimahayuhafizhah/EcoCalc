from faktor_emisi import FAKTOR_EMISI
from validator import input_angka
from logger import log

def hitung_lpg():
    kg = input_angka("Masukkan penggunaan LPG (kg): ")
    emisi = kg * FAKTOR_EMISI["lpg"]
    print(f"✅ Emisi LPG: {emisi:.2f} kg CO2")
    log(f"Menghitung emisi LPG: {kg} -> {emisi}")
    return emisi
