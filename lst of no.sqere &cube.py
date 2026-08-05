n = int(input("enter number of elements: "))

num = []
square = []
cube = []

for i in range(n):
    x = int (input())
    num.append(x)
    square.append(x*x)
    cube.append(x*x*x)

print("numbers =", num)
print("squres =", square)
print("cubes =", cube)
