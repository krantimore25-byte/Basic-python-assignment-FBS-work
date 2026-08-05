n = int(input("enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))

cube = []

for i in lst:
    cube.append(i*i*i)

print(cube)