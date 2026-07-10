# Swap two numbers
## With third variable 
a = int(input("Enter a:" ))
b = int(input("Enter b" ))

temp = a
a = b
b = temp
print("a =", a)
print("b =", b)



# without third variable
a = int(input("enter a: "))
b = int(input("enter b: "))
a, b = b, a
print("a =", a)
print("b =", b)