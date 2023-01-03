def order():
    number=input(" Ingresa número porfavor: ")
    lists=[]

    while number!="":
        lists.append(int(number))
        number=input(" Ingresa número porfavor: ")

    suma=0
    for i in lists:
        suma+=i
    promedio=suma/len(lists)
    lists.sort()
    lista_copy=lists.copy()
    for j in range(0,len(lists)):
        if lists[j]<promedio<lists[j+1]:
            lista_copy.insert(j,promedio)  
    
    return lista_copy


print(order())
