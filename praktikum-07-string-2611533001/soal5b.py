# Name: Habiburrahman El Syamsi
# NIM: 2611533001
# Question 5b

nim = input("NIM: ")

if len(nim) == 10 and nim.isdigit():
    print("Valid, intake year 20" + nim[:2])
else:
    print("Invalid NIM")