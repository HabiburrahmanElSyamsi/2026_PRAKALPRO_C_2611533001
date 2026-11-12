# Name: Habiburrahman El Syamsi
# NIM: 2611533001
# Question 7

name = "habiburrahman el syamsi"
nim = "2611533001"

# Username dari Soal 6
clean = name.strip()
space = clean.find(" ")
if space == -1:
    first = clean
else:
    first = clean[:space]
username = first.lower() + nim[-3:]

# Angkatan dari NIM (slicing)
intake = "20" + nim[:2]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print("Name".ljust(10) + ": " + name.title())
print("NIM".ljust(10) + ": " + nim)
print("Username".ljust(10) + ": " + username)
print("Intake".ljust(10) + ": " + intake)
print("=" * 30)