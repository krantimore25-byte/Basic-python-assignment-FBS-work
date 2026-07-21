n = int(input("enter number: "))

temp = n
digits = len(str(n))
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == n:
    print("Armstrong number")
else:
    print("Not Armstrong number")
    
