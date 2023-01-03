f = open("doc1.txt", "r")

list = []
list.append(f.read().split())
          
list_mayus=[]

for j in list[0]:
    list_mayus.append(j.upper())

list2=[]
for i in list_mayus:
    if i not in list2:
        list2.append(i.lower())
        list2.append(i)
        x=list_mayus.count(i)+list.count(i.lower)+list.count(i.capitalize())
        print("The word: "+i+" appears "+ str(x)+" times")