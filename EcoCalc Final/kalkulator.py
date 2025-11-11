class KalkulatorKarbon:
    FAKTOR = {
        "listrik": 0.85,
        "gas": 3.0,
        "motor": 0.09,
        "mobil_bensin": 0.18,
        "mobil_diesel": 0.21,
        "bus": 0.08,
        "kereta": 0.05,
        "sampah": 1.2,
        "air": 0.003
    }

    def __init__(self, data):
        self.data = data

    def hitung_detail(self):
        hasil = {}

        hasil["listrik"] = self.data["energi"]["listrik"] * 12 * self.FAKTOR["listrik"]
        hasil["gas"] = self.data["energi"]["gas"] * 12 * self.FAKTOR["gas"]

        total_transport = 0
        for item in self.data["transportasi"]:
            jenis = item["jenis"]
            km = item["km"]
            total_transport += km * 365 * self.FAKTOR.get(jenis, 0)
        hasil["transportasi"] = total_transport

        hasil["sampah"] = self.data["sampah"] * 52 * self.FAKTOR["sampah"]

        hasil["total"] = sum(hasil.values())
        return hasil
