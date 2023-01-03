def number(n):
    n1=n.strip()
    if n1.isdigit():
        print("Its a valid number")
    else:
        print("Itsnt a valid number")

print(number("    2310A2 "))

#EXPLICACIÓN DE STRIP METHODS.
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")   #Strip es al INICIO Y AL FINAL DEL CICLO.
x = txt.rstrip(",.grt")   #Strip es AL FINAL DEL CICLO.
x = txt.istrip(",.grt")  # Strip es al FINAL DEL CICLO.
print(x)
