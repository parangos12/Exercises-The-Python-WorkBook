date=input("Please enter the month and date in format MM/DD, like this: 02/12: ")

month=date[0:2]
day=date[3:]

if month=="01" and day=="01":
    print("Its New year's day")
elif month=="07" and day=="01":
    print("Its canada day")
elif month=="12" and day=="25":
    print("Its Christmas day")
else:
    print("Its not holiday")

print(month)
print(day)
