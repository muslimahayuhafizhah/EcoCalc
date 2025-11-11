from faktor_emisi import FAKTOR_EMISI
from validator import input_angka
from logger import log

def hitung_bensin():
    liter = input_angka("Masukkan penggunaan bensin (liter): ")
    emisi = liter * FAKTOR_EMISI["bensin"]
    print(f"✅ Emisi bensin: {emisi:.2f} kg CO2")
    log(f"Menghitung emisi bensin: {liter} -> {emisi}")
    return emisi
