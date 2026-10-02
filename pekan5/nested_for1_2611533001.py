batas_3001 = int(input("Masukkan nilai batas: "))
for line_3001 in range(1, batas_3001 + 1):
    for j in range(1, (-1 * line_3001 + batas_3001) + 1):
        print(".", end="")
    print(line_3001)