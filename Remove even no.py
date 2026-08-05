n = int (input("enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))

odd = []


for i in lst:
    if i % 2 != 0:
        odd.append(i)

print("After removing even numbers =", odd)