raise_p=2400
rating=float(input("Enter the rating please: "))

if rating==0:
    print("Unacceptable performance, your raise is ",raise_p*rating)
elif rating == 0.4:
    print("Acceptable performance, your raise is ", raise_p*rating)
elif rating>=0.6:
    print("Meritorious performance, your raise is ", raise_p*rating)
else:
    print("Doesnt recognized!")
