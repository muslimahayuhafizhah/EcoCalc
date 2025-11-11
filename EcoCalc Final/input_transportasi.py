from validasi import validasi_input

def input_transportasi():
    print("\n🚗 TRANSPORTASI HARIAN")
    data = []
    while True:
        jenis = input("Jenis kendaraan (mobil_bensin/mobil_diesel/motor/kereta/bus, Enter untuk selesai): ").lower()
        if jenis == "":
            break
        if jenis not in ["mobil_bensin", "mobil_diesel", "motor", "kereta", "bus"]:
            print("Jenis kendaraan tidak dikenal.")
            continue
        while True:
            jarak = input(f"Jarak tempuh harian dengan {jenis} (km): ")
            nilai = validasi_input(jarak)
            if nilai is not None:
                data.append({"jenis": jenis, "km": nilai})
                break
    return data
