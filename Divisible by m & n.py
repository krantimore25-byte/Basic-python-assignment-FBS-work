size = int(input("enter number of elements: "))
lst = []

for i in range(size):
    lst.append(int(input()))

m = int(input("enter m : "))
n = int(input("enter n:  "))

for i in lst:
    if i % m == 0 and i % n == 0:
        print(i, end= " ")