n = int(input("enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))


even = []
odd = []

for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("even =", even)
print("odd =", odd)