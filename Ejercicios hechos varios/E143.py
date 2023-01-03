import os

name=input("Ingrese el nombre del archivo con su resp extensión: ")
while name==""or os.path.isfile(name)==False:
    name = input("Ingrese por favor del archivo con su resp extensión: ")
f=open(name,"r")

count=0
for line in f.readlines():
    count+=1
print(count)

f.seek(0)
count2=0
for line2 in f.readlines():
    count2+=1
    if count-10<=count2<=count:
        print(line2, end=" ")




