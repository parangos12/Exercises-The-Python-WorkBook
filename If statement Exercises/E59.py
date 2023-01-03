w=0
while w!=3:
    plate=input("Enter the plate plz: ")

    if len(plate)==6:
        letters=plate[0:3]
        numbers=plate[3:]
        c=0
        d=0
        for i in letters:
            try:
                x=int(i)+1
            except:
                c+=1
        if c==3:
            print("Letters are right")
        else:
            print("letters are bad!!!")

        for j in numbers:
            try:
                y = int(j)
            except:
                d += 1
        if d >= 1:
            print("numbers are bad")
        else:
            print("numbers are right!!!")
        
        w=c+d
        print(w)



    
