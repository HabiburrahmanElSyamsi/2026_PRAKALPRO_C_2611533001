from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_3001 = float(input('Masukkan nilai jari-jari: '))
luas_3001 = PI * jari_3001 * jari_3001
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f % (jari_3001, luas_3001)")