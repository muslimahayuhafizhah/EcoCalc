from listrik import hitung_listrik
from air import hitung_air
from gas import hitung_gas
from bensin import hitung_bensin
from sampah import hitung_sampah
from lpg import hitung_lpg
from logger import log #ini buat apa?

def tampilkan_menu():
    print("\n===== ECO CALCULATOR =====")
    print("1. Hitung Emisi Listrik")
    print("2. Hitung Emisi Air")
    print("3. Hitung Emisi Gas")
    print("4. Hitung Emisi Bensin")
    print("5. Hitung Emisi Sampah")
    print("6. Hitung Emisi LPG")
    print("7. Keluar")

def main():
    total_emisi = {
        "listrik": 0,
        "air": 0,
        "gas": 0,
        "bensin": 0,
        "sampah": 0,
        "lpg": 0
    }

    log("Program eco calculator dimulai.")

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-7): ")

        if pilihan == "1":
            total_emisi["listrik"] = hitung_listrik()

        elif pilihan == "2":
            total_emisi["air"] = hitung_air()

        elif pilihan == "3":
            total_emisi["gas"] = hitung_gas()

        elif pilihan == "4":
            total_emisi["bensin"] = hitung_bensin()

        elif pilihan == "5":
            total_emisi["sampah"] = hitung_sampah()

        elif pilihan == "6":
            total_emisi["lpg"] = hitung_lpg()

        elif pilihan == "7":
            print("✅ Keluar dari program.")
            log("Program dihentikan.")
            break

        else:
            print("❌ Pilihan tidak valid!")
            log("User memasukkan pilihan salah.")

        # Ringkasan sementara
        total = sum(total_emisi.values())
        print(f"\n🌍 Total Emisi Sementara: {total:.2f} kg CO2")

if __name__ == "__main__":
    main()
