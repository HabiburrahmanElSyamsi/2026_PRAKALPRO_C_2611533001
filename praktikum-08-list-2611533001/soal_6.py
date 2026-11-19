LAST_DIGIT = 1  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below
for d in range(1, 8):
    expenses.append(int(input(f"Day {d}: ")))

total = 0
highest_day = 1
highest = expenses[0]
days_above = 0
for i in range(len(expenses)):
    total += expenses[i]
    if expenses[i] > highest:        # '>' agar hari pertama menang saat sama
        highest = expenses[i]
        highest_day = i + 1
    if expenses[i] > daily_limit:
    	days_above += 1

average = total / len(expenses)

print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: Day {highest_day}")
print(f"Days above limit: {days_above}")