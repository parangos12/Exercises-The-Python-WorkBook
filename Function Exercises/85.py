list=["primero","segundo","tercero","cuarto","quinto","sexto","septimo","octavo","noveno","decimo","undecimo","decimo segundo"]
dic={}
for i in range(1,13):
    dic[i]=list[i-1]

def ordinal(*ordinal):
    for valor in dic:     #  por defecto toma los valores keys().
        for i in ordinal:    #  *ordinal es la lista.
            if valor==i:
                print(f"{i} is {dic[valor]}")
prueba=ordinal(1,3,4,5,10)