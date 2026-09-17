a1_3001 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_3001 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_3001)
print("A2 =", a2_3001)

# Konjungsi: bernilai True jika keduanya true
hasil = a1_3001 and a2_3001
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil)

# Disjungsi: bernilai true jika salah satunya True
hasil = a1_3001 or a2_3001
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil)

# Negasi A1: membalik nilai A1
hasil = not a1_3001
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil)

# Negasi A2: membalik nilai A2
hasil = not a2_3001
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil)

# XOR: bernilai true jika kedua nilai berbeda
hasil = a1_3001 != a2_3001
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil)
