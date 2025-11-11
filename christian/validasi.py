def validasi_input(nilai_str, batas_maks=10000):
    try:
        nilai = float(nilai_str)
        if nilai < 0:
            raise ValueError("Nilai tidak boleh negatif.")
        if nilai > batas_maks:
            raise ValueError(f"Nilai terlalu besar (maksimum {batas_maks}).")
        return nilai
    except ValueError as e:
        print("Input tidak valid:", e)
        return None