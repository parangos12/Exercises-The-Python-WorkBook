import random

def bingo():
    dic={"B":[],"I":[],"N":[],"G":[],"O":[]}
    dic2 = {0: [], 1: [], 2: [], 3: [], 4: []}
    lista=[]

    c=0
    while c<=4:
        dic2[0].append(random.randint(1,15))
        dic2[1].append(random.randint(16,30))
        dic2[2].append(random.randint(31,45))
        dic2[3].append(random.randint(46,60))
        dic2[4].append(random.randint(61, 75))
        c+=1

    for k in range(0,5):

        dic["B"]=dic2[k]
        dic["I"]=dic2[k+1]
        dic["N"]=dic2[k+2]
        dic["G"]=dic2[k+3]
        dic["O"]=dic2[k+4]
        break

    x=print(f'{"B":10}{"I":10}{"N":10}{"G":10}{"O":10}')
    print(x)
    for i in range(0,5):
        for j in range(0,5):

            print(f'{dic2[i][j]}{dic2[i+1][j]:10}{dic2[i+2][j]:10}{dic2[i+3][j]:10}{dic2[i+4][j]:10}')
        break

    return dic

     
print(bingo())        

        
        

        
