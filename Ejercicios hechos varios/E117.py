#Line of best fit

def equation():
    string=input("Enter the coordinate pair like this: 3,2 or 14,90 ")
    listax=[]
    listay=[]   

    while string!="":

        lista=string.split(",")
        listax.append(float(lista[0]))
        listay.append(float(lista[-1]))

        string=input("Enter the coordinate pair like this: 3,2 or 14,90 ")
    
    sumx=0
    sumx2=0
    sumy=0
    sumxsumy=0
    for i in listax:
        sumx+=i
        sumx2+=i**2
    for j in listay:
        sumy+=j
    for k in range(0,len(listax)):
        sumxsumy+=(listax[k]*listay[k])
    n=len(listax)
    m=round((sumxsumy-(sumx*sumy)/n)/(sumx2-((sumx)**2)/n),2)
    b=round((sumy/n)-m*(sumx/n),2)

    return "y= "+ str(m) + "x" + "+ "+str(b)




    
    
        


print(equation())

