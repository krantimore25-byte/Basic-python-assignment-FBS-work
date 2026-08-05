n = int(input("enter number of elements:  "))
lst = []

for i in range(n):
    num = int(input("enter element:  "))
    lst.append(num)

maximum = lst[0]
minimum = lst[0]

for i in lst:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print("list =", lst)
print("maximum =", maximum)
print("minimum =", minimum)
        