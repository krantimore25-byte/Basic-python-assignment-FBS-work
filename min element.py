list = [45, 34, 81, 77, 53,34,26, 82]
min = list[0]
for ind in range (1, len(list)):
    if (list[ind]<min):
        min = list[ind]
print("min element:", min)