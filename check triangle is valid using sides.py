a = int(input("enter a first side:"))
b = int(input("enter a second side"))
c = int(input("enter a third side"))

if a + b > c and a + c > b and b + c > a:
    print("valid triangle")
else:
    print("invalid triangle")