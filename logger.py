import datetime

def log(pesan):
    """Catat aktivitas ke file log."""
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log_eco.txt", "a") as file:
        file.write(f"[{waktu}] {pesan}\n")
