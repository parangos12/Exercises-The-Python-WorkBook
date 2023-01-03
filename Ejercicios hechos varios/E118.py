import random

def createdeck():
    suits=["s","h","d","c"]
    chs=["T","J","Q","K","A","2","3","4","5","6","7","8","9"]

    baraja=[]

    for i in suits:
        for j in chs:
            baraja.append(j+i)

    return baraja
lista_baraja=createdeck()

def shuffle(lista):
    
    desordenada=[]

    for i in range(0,len(lista)):
        pos_random=random.randint(0,10)
        desordenada.insert(pos_random,lista[i])

    return desordenada

print(shuffle(lista_baraja))
