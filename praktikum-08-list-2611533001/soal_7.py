menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below
for d in range(number_of_days):
    row = []
    for menu in menus:
        row.append(int(input(f"Day {d + 1}, {menu}: ")))
    sales.append(row)

print("Total per day:")
for d in range(number_of_days):
    print(f"Day {d + 1}: {sum(sales[d])}")

menu_totals = []
for c in range(len(menus)):
    total = 0
    for d in range(number_of_days):
        total += sales[d][c]
    menu_totals.append((menus[c], total))

print("Total per menu:")
for name, total in menu_totals:
    print(f"{name}: {total}")

best_name, best_total = menu_totals[0]
for name, total in menu_totals:
    if total > best_total:
        best_name, best_total = name, total
print(f"Best seller: {best_name} ({best_total})")