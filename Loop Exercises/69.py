pi=3
signo=""
counter=1
for i in range(2,31,2):
    print(i)

    if counter%2==0:   
        denominador=(i)*(i+1)*(i+2)
        pi=pi-4/denominador
        print(pi)
        counter+=1
    else:
        denominador=(i)*(i+1)*(i+2)
        pi=pi+4/denominador
        print(pi)
        counter+=1

