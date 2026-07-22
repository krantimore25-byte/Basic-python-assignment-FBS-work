x = int(input("enter x: "))
n = int(input("enter number of terms: "))
sum = 0
sign = 1
den = 1

for i in range( 1, n + 1):
    sum += sign *(x ** i) / den
    sign *= -1
    den += 2

print("sum=", sum)
