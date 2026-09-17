angka1_3001 = int(input("Input angka-1: "))
angka2_3001 = int (input("Input angka-2: "))

print("\nNilai awal angka1_3001 =", angka1_3001)
print("Nilai angka2_3001 =", angka2_3001)

# Assignment biasa
hasil = angka1_3001
print("\nAssignment biasa (=)")
print("Hasil =", hasil)

# Assignment penambahan
hasil = angka1_3001
hasil += angka2_3001
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil)

# Assignment pengurangan
hasil = angka1_3001
hasil -= angka2_3001
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil)

# Assignment perkalian
hasil = angka1_3001
hasil *= angka2_3001
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil)

# Assignment pembagian, pembagian bulat, dan sisa bagi

if angka2_3001 != 0:
    hasil = angka1_3001
    hasil /= angka2_3001
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil)
    # Operator tambahan
    hasil = angka1_3001
    hasil //= angka2_3001
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil)
    hasil = angka1_3001
    hasil %= angka2_3001
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil = angka1_3001
hasil **= angka2_3001
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil)

# Bitwise XOR
hasil = angka1_3001 ^ angka2_3001
print("\nBitwise XOR (^)")
print(angka1_3001, "^", angka2_3001, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise NOT
hasil = ~angka1_3001
print("\nBitwise NOT (~)")
print("~", angka1_3001, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise geser kiri
jumlah_geser = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil = angka1_3001 << jumlah_geser
print("\nBitwise geser kiri (<<)")
print(angka1_3001, "<<", jumlah_geser, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise geser kanan
hasil = angka1_3001 >> jumlah_geser
print("\nBitwise geser kanan (>>)")
print(angka1_3001, ">>", jumlah_geser, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))