start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end + 1):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        rem = temp % 10
        total += rem ** digits
        temp //= 10

    if num == total:
        print(num)



