string=input("Ingrese los 3 lados del triangulo separados por comas: ")

list=string.split(",")
a=list[0]
b=list[1]
c=list[-1]

if a==b and b==c:
    print("Equilatero")
elif a==b and b!=c:
    print("Isosceles")
else:
    print("Escaleneo")
