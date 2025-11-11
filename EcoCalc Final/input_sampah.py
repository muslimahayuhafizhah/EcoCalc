from validasi import validasi_input

def input_sampah():
    print("\n🗑️ SAMPAH")
    while True:
        sampah = input("Sampah (kg per minggu): ")
        nilai = validasi_input(sampah)
        if nilai is not None:
            return nilai
