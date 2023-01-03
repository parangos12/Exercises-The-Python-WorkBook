def primo(a):
    contador=0
    for i in range(2,a):
        if a%i!=0:
            contador+=1
    if contador==(a-2):
        return "es primo"

counter=0
list=[]
i=3
while counter<100:
    if primo(i)=="es primo":
        list.append(i)
        counter+=1
        i+=1
    else:
        i+=1
print(len(list))

print(list)





