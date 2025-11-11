from input_energi import input_energi
from input_transportasi import input_transportasi
from input_sampah import input_sampah
from kalkulator import KalkulatorKarbon
from perbandingan import bandingkan_dengan_rata
from tips import beri_tips
from log_user import simpan_hasil

def main():
    print("="*50)
    print("EcoCalc")
    print("="*50)

    data = {
        "energi": input_energi(),
        "transportasi": input_transportasi(),
        "sampah": input_sampah()
    }

    kalkulator = KalkulatorKarbon(data)
    hasil = kalkulator.hitung_detail()

    print("\nRincian Emisi (kg CO2/tahun):")
    for k, v in hasil.items():
        if k != "total":
            print(f"- {k.capitalize():15}: {v:,.2f}")
    print("-"*50)
    print(f"Total Emisi Anda   : {hasil['total']:,.2f} kg CO2/tahun")

    status, persen = bandingkan_dengan_rata(hasil["total"])
    print(f"Status dibanding rata-rata Indonesia: {persen:.1f}% {status}")

    print("\nTips:")
    for t in beri_tips(data, hasil):
        print("-", t)

    simpan_hasil(data, hasil, status, persen)
    print("\n📁 Hasil disimpan ke 'hasil.txt'")

if __name__ == "__main__":
    main()