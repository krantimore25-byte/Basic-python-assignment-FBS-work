n = int(input("enter number: "))
flag = True
if n < 2:
    flag = False
else:
    for i in range( 2, n):
        if n % i == 0:
            flag = False
            break
    if flag:
        print("prime number")
    else:
        print("not prime number")