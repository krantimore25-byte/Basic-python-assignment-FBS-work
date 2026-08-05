n = 5
for i in range(n, 0,-1):
    print(i, end= "")
    for j in range(2,n+1):
        if j==i:
            print(1, end=" ")
        else:
            print(" ", end=" ")
    print()      