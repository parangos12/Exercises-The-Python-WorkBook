
import random


def contraseña():
    lenght=random.randint(7,10)

    s=""
    for i in range(1,lenght+1):
        aleatorio_number=random.randint(33,126)
        s+=chr(aleatorio_number)

    return s 

print(contraseña())



