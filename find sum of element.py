n = int(input('enter number of element: '))
lst = []
for i in range(n):
    num = int(input('enter element:'))
    lst.append(num)

total = 0
for i in lst:
    total = total + i

print('list =', list)
print('sum =', total)

