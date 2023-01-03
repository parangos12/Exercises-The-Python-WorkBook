def password(contraseña):

    lista=list(contraseña)

    if len(lista)<=8:
        c=0
        d=0
        e=0
        mayuscula=contraseña.upper()
        minuscula=contraseña.lower()
        lista_mayuscula=list(mayuscula)
        lista_minuscula=list(minuscula)
        
        
        for i in lista_mayuscula:
            for j in lista:
                if i==j:
                    c=1

        for k in lista_minuscula:
            for l in lista:
                if k==l:
                    d=1
        for p in lista:
            if p.isdigit()==True:
                e=1

        if c+d+e==3:
            return "password okey"
        else:
            return "password is wrong"                    
               
    else:
        return "password is wrong"

print(password("dasdaD4"))

        
