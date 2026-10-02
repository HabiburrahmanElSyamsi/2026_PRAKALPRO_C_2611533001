ulang_3001 = int(input("Masukkan nilai batas: "))

jumlah_3001 = 0
for i in range(1, ulang_3001 + 1):
    if i % 2 == 0:
        print(i, end=" ")
        jumlah_3001 = jumlah_3001 + i

    if i < ulang_3001:
        print(" + ", end="")
    else:
        print(" = ", jumlah_3001, end="")
print()
print("Jumlah =", jumlah_3001)