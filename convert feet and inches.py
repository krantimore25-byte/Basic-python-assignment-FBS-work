feet = float(input("enter feet:"))
inch = float(input("enter inches:"))
total_inches = feet * 12 + inch
cm = total_inches * 2.54
m = cm / 100
print("meters =", m)
print("centimeters =", cm)