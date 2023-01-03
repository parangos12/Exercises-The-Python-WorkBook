import os

#print(os.path.isfile("E139e.py"))  #solo funciona para los archivos que estén dentro carpeta

name=input("Ingrese el nombre del archivo con su resp extensión: ")
while name==""or os.path.isfile(name)==False:
    name = input("Ingrese por favor del archivo con su resp extensión: ")
f=open(name,"r")
c=0
while c<=9:
    for line in f.readlines(10):
        print(line.rstrip())
        c+=1


