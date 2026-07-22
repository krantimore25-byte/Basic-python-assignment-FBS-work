n = int(input("Enter number of students: "))
total_percentage = 0

for i in range(1, n + 1 ):
    total = 0
    print("\nStudent", i)

    for j in range(1, 6):
        marks = int(input(f"Enter marks of subject {j}: "))
        total += marks

        percentage = total/ 5
        print("percentage =", percentage)
        total_percentage += percentage
avg = total_percentage / n
print("\nAverage precentage =", Avg)
