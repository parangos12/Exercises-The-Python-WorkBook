date=input("Enter the date please, like this September 05: ")

day=int(date[-2:])
month1=(date[0:-3]).upper()
print(day)
print(month1)

if month1=="MARCH" and day==20:
    print("Spring")
elif month1 == "JUNE" and day == 21:
    print("Summer")
elif month1 == "SEPTEMBER" and day == 22:
    print("Fall")
elif month1 == "DECEMBER" and day == 21:
    print("Winter")
