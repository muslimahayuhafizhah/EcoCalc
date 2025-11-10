from faktor_emisi import FAKTOR_EMISI
from validator import input_angka
from logger import log

def hitung_gas():
    m3 = input_angka("Masukkan penggunaan gas (m³): ")
    emisi = m3 * FAKTOR_EMISI["gas"]
    print(f"✅ Emisi gas: {emisi:.2f} kg CO2")
    log(f"Menghitung emisi gas: {m3} -> {emisi}")
    return emisi
