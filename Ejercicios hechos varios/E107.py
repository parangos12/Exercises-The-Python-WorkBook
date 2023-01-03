
def duplicate():
    lista1 = []

    word=input("Ingrese palabra por favor: ")
    if word!="":
        lista1.append(word)


    while word!="":  

        if (word not in lista1):    
        lista1.append(word)
        word = input("Ingrese palabra por favor: ")

    lista1=list(set(lista1))

    return lista1

print(duplicate())
