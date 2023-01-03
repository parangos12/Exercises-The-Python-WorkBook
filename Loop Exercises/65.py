from math import sqrt

perimeter=0
xi=int(input("Enter x coordenate please: "))
yi = int(input("Enter y coordenate please: "))

ci=(xi,yi)

xf=1

while xf!=0:
    xf=int(input("Enter x coordenate please(blank to exit): "))
    if xf==0:
        xi=ci[0]
        yi=ci[-1]
        xff=cf[0]
        yff=cf[-1]
        d=sqrt((xff-xi)**2+(yff-yi)**2)
        print(xff,",",yff)
        perimeter+=d
        continue
    yf = int(input("Enter y coordenate please: "))  
    d=sqrt((xf-xi)**2+(yf-yi)**2)
    perimeter+=d
    xi=xf
    yi=yf
    cf = [xf, yf]
    

print(perimeter)
print(cf)


