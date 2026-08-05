def prime(n,i=2):
    if n <= 2:
        return true if n == 2 else false
    if n % i ==0:
        return false
    if i * i > n:
        return True
    return prime(n, i + 1)

n = int(input("enter number:"))
if prime(n):
    print("prime number")
else:
    print("not prime number")