f=open("doc1.txt","r")

list=[]
list.append(f.read().split())

lens=[]
for i in range(0,len(list[0])):
    lens.append(len(list[0][i]))
lens.sort()

max=lens[-1]
for j in range(0,len(list[0])):
    if len(list[0][j])==max:
        print("La palabra "+str(list[0][j])+" tiene "+ str(max) )





