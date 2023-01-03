def shipping(items):
    if items>0:
        FIRST=10.95
        OTHERS=2.95
        charge=10.95+2.95*(items-1)
        return charge
    else:
        print("Hey, enter the number of items plz")

print(shipping(9))