from faktor_emisi import FAKTOR_EMISI
from validator import input_angka
from logger import log

def hitung_sampah():
    kg = input_angka("Masukkan berat sampah (kg): ")
    emisi = kg * FAKTOR_EMISI["sampah"]
    print(f"Emisi sampah: {emisi:.2f} kg CO2")
    log(f"Menghitung emisi sampah: {kg} -> {emisi}")
    return emisi
