import random
list=[]
list_multiplos=[]
#Generating 50 random numbers
for i in range(0,50):
    list.append(random.randint(1,50))

#Body's programm    
contador=0
for i in list:
    if i%7==0:
        contador=contador+1
        if contador<=5:
            list_multiplos.append(i)
        elif contador==7:
            break

print(list_multiplos)
