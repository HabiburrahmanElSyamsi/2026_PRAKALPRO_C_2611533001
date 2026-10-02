tinggi_3001 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3001 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_3001 = tinggi_3001
    c_3001 = a_3001
    lebar_3001 = (2 * tinggi_3001) - 2

    for i_3001 in range(1, tinggi_3001 + 1):
        b_3001 = c_3001 + 1

        for j_3001 in range(1, lebar_3001 + 1):

            if i_3001 == 1 or i_3001 == tinggi_3001:
                if  j_3001 == 1 or j_3001 == lebar_3001:
                    print("#", end="")
                else:
                    print("=", end="")
            else:
                if j_3001 == 1 or j_3001 == lebar_3001:
                    print("|", end="")
                else:
                    if j_3001 == c_3001:
                        print("<", end="")
                    elif j_3001 == b_3001:
                        print(">", end="")
                    elif j_3001 == (lebar_3001 - c_3001):
                        print("<", end="")
                    elif j_3001 == (lebar_3001 - c_3001 + 1):
                        print(">", end="")
                    elif j_3001 > b_3001 and j_3001 < (lebar_3001 - c_3001):
                        print(".", end="")
                    else:
                        print(" ", end="")

    print()

    a_3001 -= 2
    if a_3001 <= 0:
        c_3001 = (-a_3001) + 2
    else:
        c_3001 = a_3001