def magic_dates():
    fecha=input("Ingrese la fecha en formato DD/MM/AAAA: ")
    lista_fecha=list(fecha)
    dia=int(lista_fecha[0]+lista_fecha[1])
    mes=int(lista_fecha[3]+lista_fecha[4])
    año=int(lista_fecha[8]+lista_fecha[9])

    if dia*mes==año:
        return "Its a magic date"

    else:
        return "Its not a magic date"

print(magic_dates())
