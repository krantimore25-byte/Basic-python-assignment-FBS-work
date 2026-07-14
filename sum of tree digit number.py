num = int(input("enter a tree digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10
print("sum =", a + b + c)