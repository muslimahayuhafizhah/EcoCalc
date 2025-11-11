from datetime import datetime

def simpan_hasil(data, hasil, status, persen):
    with open("hasil.txt", "a", encoding="utf-8") as f:
        f.write("="*50 + "\n")
        f.write(f"Waktu: {datetime.now()}\n")
        f.write("-"*50 + "\n")
        for k, v in hasil.items():
            if k != "total":
                f.write(f"{k.capitalize():15}: {v:,.2f} kg CO2/tahun\n")
        f.write("-"*50 + "\n")
        f.write(f"Total: {hasil['total']:,.2f} kg CO2/tahun\n")
        f.write(f"Status: {persen:.1f}% {status}\n")
        f.write("="*50 + "\n\n")
