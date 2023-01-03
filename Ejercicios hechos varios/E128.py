""" midicionario={"Colombia":"Bogotá","Antioquia":"Medellin","Ecuador":"Quito"}

x=midicionario.items()

y=list(x)

print(y[0][0]) """

def reverseLookup(dic,value):
    keys=[]
    Lista=list(dic.items())

    for i in Lista:
        if i[-1]==value:
            keys.append(i[0])

    return keys

datos_edad={"pedro":22,"jose":22,"juan":23,"carlos":24,"jesus":22}
value=22

print(reverseLookup(datos_edad,value))
