date = input("Enter the date please, like this September 05: ")

day = int(date[-2:])
month1 = (date[0:-3]).upper()
print(day)
print(month1)

if (month1 == "DECEMBER" and day >= 22) or (month1 == "JANUARY" and day<=19):
    print("Capricorn")
elif (month1 == "JANUARY" and day >= 20) or (month1 == "FEBRUARY" and day <= 18):
    print("Aquarius")
elif (month1 == "FEBRUARY" and day >= 19) or (month1 == "MARCH" and day <= 20):
    print("Pisces")
elif (month1 == "MARCH" and day >= 21) or (month1 == "APRIL" and day <= 19):
    print("Aries")
elif (month1 == "APRIL" and day >= 20) or (month1 == "MAY" and day <= 20):
    print("Taurus")
elif (month1 == "MAY" and day >= 21) or (month1 == "JUNE" and day <= 20):
    print("Gemini")
elif (month1 == "JUNE" and day >= 21) or (month1 == "JULY" and day <= 22):
    print("Cancer")
elif (month1 == "JULY" and day >= 23) or (month1 == "AUGUST" and day <= 22):
    print("Leo")
elif (month1 == "AUGUST" and day >= 23) or (month1 == "SEPTEMBER" and day <= 22):
    print("Virgo")
elif (month1 == "SEPTEMBER" and day >= 23) or (month1 == "OCTOBER" and day <= 22):
    print("Libra")
elif (month1 == "OCTOBER" and day >= 23) or (month1 == "NOVEMBER" and day <= 21):
    print("Scorpio")
elif (month1 == "NOVEMBER" and day >= 22) or (month1 == "DECEMBER" and day <= 21):
    print("Sagittarius")


