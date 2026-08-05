n = int(input("enter number of elements: "))
lst = []
for i in range(n):
    num = int(input("enter element: "))
    lst.append(num)

largest = lst[0]
second = lst[0]

for i in lst:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("list =", lst)
print("second largest =", second)
