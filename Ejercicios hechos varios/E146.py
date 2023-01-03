f=open("doc1.txt","r")

list=[]
for letter in f.read():
    list.append(letter.rstrip())

list3=[]
list2=[]
for j in list:
    list3.append(j.upper())

for i in list3:
    if i not in list2:
        list2.append(i.lower())
        list2.append(i)
        x=list3.count(i)+list.count(i.lower)
        print("The word: "+i+" appears "+ str(x)+" times")




