n = int(input("enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))
x  = int(input("enter element to remove: "))

new = []

for i in lst:
    if i != x:
        new.append(i)

print(new)