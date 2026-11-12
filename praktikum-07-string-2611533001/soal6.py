# Name: Habiburrahman El Syamsi
# NIM: 2611533001
# Question 6

first_name = " muhammad"
nim = "rafi "
full_name = first_name.strip() + " " + nim.strip()
print(full_name)
print(full_name.title())

full_name = "  Habiburrahman El Syamsi  "
nim = "2611533001"

clean = full_name.strip()
space = clean.find(" ")

if space == -1:
    first = clean
else:
    first = clean[:space]

username = first.lower() + nim[-3:]
print(username)