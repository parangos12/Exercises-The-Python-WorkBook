human=int(input("Ingrese la edad a convertir: "))

if 2>=human>=0:
    print("La conversión da "+str(human*10.5))
elif human>2:
    print("La conversión da "+str((human-2)*4+2*10.5))
else:
    print("Haz ingresado un numero negativo")

