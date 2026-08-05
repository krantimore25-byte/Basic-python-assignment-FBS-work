n = int(input("enter number of elements:"))
lst = []

for i in range(n):
    lst.append(int(input()))

new = []

for i in lst:
    found = False
    for j in new:
        if i == j:
            found = True
            break
    if not found:
        new.append(i)

print(new)