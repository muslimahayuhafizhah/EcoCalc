def input_angka(prompt):
    """Validasi input angka agar tidak negatif dan tidak huruf."""
    while True:
        try:
            nilai = float(input(prompt))
            if nilai < 0:
                print("❌ Nilai tidak boleh negatif.")
                continue
            return nilai
        except ValueError:
            print("❌ Masukkan angka yang valid!")
