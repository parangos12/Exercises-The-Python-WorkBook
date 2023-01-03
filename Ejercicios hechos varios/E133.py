def translate():
    number=int(input("Plz enter the number between 0-999: "))

    individual={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}

    decenas={20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}

    centenas={100:"one hundred",200:"two hundred",300:"three hundred",400:"four hundred",500:"five hundred",600:"six hundred",700:"seven hundred",800:"eight hundred",900:"nine hundred",}

    definitive=""

    if 0<=number<=19:
        for i in individual.keys():
            if i==number:
                definitive+=individual[i]

    elif 20<=number<=99:
        for j in decenas.keys():
            if 0<=number-j<=9:
                definitive+=decenas[j]+" "+individual[number-j]

    elif 100<=number<=999:
        for k in centenas.keys():
            if 0<=number-k<=99:
                if 0<=number-k<=19:
                    definitive+=centenas[k]+" "+ individual[number-k]
                elif 20<=number-k<=99:
                    number_string=str(number)
                    position=int(number_string[-1])
                    definitive+=centenas[k]+" "+decenas[number-k-position]+" "+ individual[position]
    
    return definitive

print(translate())



