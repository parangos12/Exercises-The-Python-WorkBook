

def primo(a):
    c=""
    while c=="es primo":

        if a==2:
            c="es primo"
            return a
        
        for i in range(2,a):
            if a%i==0:
                c="no es primo"
                a+=1
            else:
                c="es primo"
                return a
    return a


print(primo(20))