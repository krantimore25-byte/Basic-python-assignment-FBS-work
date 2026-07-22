a = int(input("enter a: "))
sum = 0

for i in range(1, 11):
    sum +=(a **i) / i
    print("sum =", sum)
