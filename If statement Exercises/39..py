sound=int(input("Ingrese número decibeles por favor: "))

if 106<=sound<=130:
    if sound==130:
        print("Jachammer")
    elif sound==106:
        print("Gas lawnmower")
    else:
        print("Between Jackhammer or gas lawnmower")
elif 70 <= sound < 106:
    if sound == 70:
        print("Alarm clock")
    else:
        print("Between Alarm clock or gas lawnmower")

elif 40 <= sound < 70:
    if sound==40:
        print("Quiet room")
    else:
        print("Between Alarm clock or Quiet room")
elif sound>130 or 0<sound<40:
    print("Out of range")
else:
    print("You entered a negative value")

