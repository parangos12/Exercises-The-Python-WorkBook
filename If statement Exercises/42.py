import math as ma

frecuency=float(input("Enter the frecuency please: "))

dic = {"C": 261.63, "D": 293.66, "E": 329.63,
       "F": 349.23, "G": 392, "A": 440, "B": 493.88}

for i in dic.values():
    result=ma.log(16*frecuency/i)/ma.log(2)
    result2=str(result)
    if result2[-1]=="0":
        for j in dic.keys():
            if dic[j]==i:
                print(j+result2[0])
                break
    
    



