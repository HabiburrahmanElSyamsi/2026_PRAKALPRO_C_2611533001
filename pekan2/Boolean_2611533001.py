is_lulus = True
is_cumlaude = True

nilai_3001 = 85
batas_lulus = 75

status_kelulusan = nilai_3001 >= batas_lulus

print("=== Check Kelulusan ===")
print("Nilai:", nilai_3001)
print("Apakah Lulus?:", status_kelulusan)
if is_lulus and is_cumlaude:
    print("Selamat, Anda lulus dengan predikat Cum Laude!")
