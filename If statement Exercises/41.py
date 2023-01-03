octave=input("Ingrese la nota musical por favor: ")

number=int(octave[-1])
letter=octave[0]

dic = {"C": 261.63, "D": 293.66, "E": 329.63, "F":349.23,"G":392,"A":440,"B":493.88}

for i in dic.keys():
    if i==letter:
        print("The frecuency of " + octave + " is "+ str(dic[i]/(2**(4-number))))


