def apicua(numero1):
    numero=str(numero1)
    alreves=""
    for i in range(1,len(numero)+1):
        alreves+=numero[-i]
    if numero==alreves:

        return True
    else:

        return False

print(apicua(13))

apicuas=[]

for i in range(1,1000):
    if apicua(i)==True:
        apicuas.append(i)
print(apicuas)