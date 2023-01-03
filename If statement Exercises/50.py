#Roots of a quadratic Function
import math
from cmath import sqrt


coeficients=input("Ingrese los coeficientes por favor de laf (x) = ax2 + bx + c: ")

list_coeficients=coeficients.split(",")
a = int(list_coeficients[0])
b=int(list_coeficients[1])
c=int(list_coeficients[-1])

if b**2-4*a*c>0:
    root1=(-b+math.sqrt(b**2-4*a*c))/2*a
    root2=(-b-math.sqrt(b**2-4*a*c))/2*a
    print("LA FUNCIÓN TIENE:"+str(root1)+" y "+str(root2))
elif b**2-4*a*c==0:
    root1=(-b)/(2*a)
    print("LA FUNCIÓN TIENE:"+str(root1))
else:
    root1="Doesn have real roots"
    print(root1)

