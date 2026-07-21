n = int(input("enter limit: "))
d = int(input("enter dividor: "))

for i in range(1, n + 1):
    if i % d == 0:
        print(i, end=" ")