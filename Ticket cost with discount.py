n = int(input("Enter number of passengers: "))
ticket = int(input("Enter ticket cost: "))

total = 0

for i in range(1, n + 1):
    age = int(input(f"Enter age of passenger {i}: "))

    if age < 12:
        amount = ticket * 0.70
    elif age > 59:
        amount = ticket * 0.50
    else:
        amount = ticket

        total += amount
print("Total ticket amount =", total)