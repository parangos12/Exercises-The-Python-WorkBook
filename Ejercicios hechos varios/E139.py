def bingowin():
    B=input("Escribe los números de la letra B, separados por , : ")
    I=input("Escribe los números de la letra I, separados por , : ")
    N=input("Escribe los números de la letra N, separados por , : ")
    G=input("Escribe los números de la letra G, separados por , : ")
    O=input("Escribe los números de la letra O, separados por , : ")

    dic = {"B": B.split(","), "I": I.split(","), "N": N.split(","), "G": G.split(","), "O": O.split(",")}
    
    resultado=False

    for i in range(0,5):  #Horizontal
        sum=int(dic["B"][i])+int(dic["I"][i])+int(dic["N"][i])+int(dic["G"][i])+int(dic["O"][i])
        if sum==0:
            resultado=True
    
    for j in dic.keys():   #vertical
        sum=int(dic[j][0])+int(dic[j][1])+int(dic[j][2])+int(dic[j][3])+int(dic[j][4])
        if sum==0:
            resultado=True

    if int(dic["B"][0])+int(dic["I"][1])+int(dic["N"][2])+int(dic["G"][3])+int(dic["O"][4])==0:
        resultado==True

    if int(dic["B"][4])+int(dic["I"][3])+int(dic["N"][2])+int(dic["G"][1])+int(dic["O"][0])==0:
        resultado==True
             
    return resultado

print(bingowin())
