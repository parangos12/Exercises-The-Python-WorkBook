m=int(input("Enter your first number: "))
n=int(input("Enter your second number: "))
d=min(m,n)

while m%d!=0 or n%d!=0:   #SE PUEDE PONER VARIAS CONDCIONES EN EL CICLO.
    d-=1
print(d)