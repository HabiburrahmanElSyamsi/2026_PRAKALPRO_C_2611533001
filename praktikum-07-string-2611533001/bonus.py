# Name: Habiburrahman El Syamsi
# NIM: 2611533001
# Question bonus

kalimat = input("Kalimat: ")

bersih = kalimat.replace(" ", "").lower()

if bersih == bersih[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")