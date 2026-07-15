cp = float(input("enter cost of price: "))
sp = float(input("enter selling price: "))

if sp > cp:
    print("profit =", sp - cp)
elif cp > sp:
    print("loss =", cp - sp)
else:
    print("no profit no loss")
