tinggi_3001 = int(input("Masukkan tinggi segitiga: "))

for i_3001 in range(1, tinggi_3001 + 1):
    print(" " * (tinggi_3001 - i_3001), end="")
    for j_3001 in range(1, i_3001 + 1):
        print("* ", end="")
    print()