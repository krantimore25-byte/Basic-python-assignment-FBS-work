a = int(input("enter a first side: "))
b = int(input("enter a second side: "))
c = int(input("enter a third side: "))
if a == b == c:
    print("equilateral triangle")
elif a == b or b == c or a == c:
    print("isosceles triangle")
else:
    print("scalene triangle")
