import random

def dice():

    probably=[2,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,9,9,9,9,10,10,10,11,11,12]
    resultados=[]
    for i in range(0,1000):
        resultados.append(random.randint(1,6)+random.randint(1,6))
    for j in range(2,13):
        print(f"Total     Simulated Percent     Expected Percent")
        print(f"{j:5}{(resultados.count(j)/10):15}{round(((probably.count(j)/36)*100),2):20}")
    
print(dice())
