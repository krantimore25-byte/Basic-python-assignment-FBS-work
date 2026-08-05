ch = 65
for i in range(1,6):
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()

ch = 14 + 65
for i in range(4, 0, -1):
    for j in range(i):
        print(chr(ch), end= " ")
        ch += 1
    print()