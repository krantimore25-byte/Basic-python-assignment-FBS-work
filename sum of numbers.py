def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n-1)

n = int(input("enter n:"))
print("sum =", sum_n(n))