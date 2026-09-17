print("\n=================================")
print("3. OPERATOR BITWISE")
print("=================================")

angka1_3001 = int(input("Masukkan angka bitwise-1: "))
angka2_3001 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1_3001 =", angka1_3001, "| biner =", bin(angka1_3001))
print("angka2_3001 =", angka2_3001, "| biner =", bin(angka2_3001))

# Bitwise AND
hasil = angka1_3001 & angka2_3001
print("\nBitwise AND (&)")
print(angka1_3001, "&", angka2_3001, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise OR
hasil = angka1_3001 | angka2_3001
print("\nBitwise OR (|)")
print(angka1_3001, "|", angka2_3001, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))