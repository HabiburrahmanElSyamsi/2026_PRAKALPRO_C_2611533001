# Name: Habiburrahman El Syamsi
# NIM: 2611533001
# Question 3b

text = "Habiburrahman El Syamsi"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)