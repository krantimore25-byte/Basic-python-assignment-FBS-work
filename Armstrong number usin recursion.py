def armstrong(num, power):
    if num == 0:
        return 0
    digit = num % 10
    return digit ** power + armstrong(num// 10, power)

n = int(input("enter number: "))
power = len(str(n))

if armstrong(n,power) ==n:
    print("armstrong number")
else:
    print("not armstrong number")