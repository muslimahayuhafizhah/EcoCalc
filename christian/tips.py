def beri_tips(data, hasil):
    tips = []
    if hasil["listrik"] > 1000:
        tips.append("Gunakan alat elektronik hemat energi.")
    if hasil["transportasi"] > 1000:
        tips.append("Gunakan transportasi umum atau sepeda bila memungkinkan.")
    if hasil["sampah"] > 200:
        tips.append("Pisahkan dan daur ulang sampah rumah tangga.")
    if not tips:
        tips.append("Kebiasaan Anda sudah cukup ramah lingkungan.")
    return tips
