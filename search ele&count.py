n = int (input("enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))

x = int(input("enter element to search: "))

count = 0

for i in lst:
    if i == x:
        count += 1

if count > 0:
    print("present")
    print("count =", count)

else:
    print("not present")