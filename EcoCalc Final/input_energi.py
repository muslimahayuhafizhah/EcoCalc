from validasi import validasi_input

def input_energi():
    print("\n KONSUMSI ENERGI")
    data = {}
    while True:
        listrik = input("Listrik (kWh per bulan): ")
        nilai = validasi_input(listrik)
        if nilai is not None:
            data["listrik"] = nilai
            break
    while True:
        gas = input("Gas (kg per bulan): ")
        nilai = validasi_input(gas)
        if nilai is not None:
            data["gas"] = nilai
            break
    while True:
        air = input("Air (Liter per bulan): ")
        nilai = validasi_input(air)
        if nilai is not None:
            data["air"] = nilai
            break
    return data