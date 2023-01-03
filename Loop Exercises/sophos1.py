cantpositivos=0
cantnegativos=0
sumapositivos=0

for i in range(0,10):
    number=int(input("Type your number: "))
    if number>0:
        cantpositivos+=1
        sumapositivos=sumapositivos+number
    else:
        if number<0:
            cantnegativos+=1
        else:
            continue

print("La cantidad positivos fue: ", cantpositivos)
print("La cantidad negativos fue: ", cantnegativos)
print("La suma positivos fue: ", sumapositivos)

    