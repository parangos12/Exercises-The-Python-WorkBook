def magic_dates():

    for i in range(1,31):
        for j in range(1,13):
            for k in range(1900,2000):
                añodos=str(k)
                lista_año=list(añodos)
                añotwo=int(lista_año[2]+lista_año[3])
                if i*j==añotwo:
                    print("its a magic date: "+str(i)+"/"+str(j)+"/"+str(k))

print(magic_dates())

