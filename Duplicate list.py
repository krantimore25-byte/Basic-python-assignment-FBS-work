n = int(input("enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))

copy = []
for i in lst:
    copy.append(i)

print("origional =", lst)
print("copy =", copy)