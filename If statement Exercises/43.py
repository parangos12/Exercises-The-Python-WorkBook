number=int(input("Ingrese denominación del dolar por favor: "))
dic = {1: "George Washington", 2: "Tomas Jefferson", 5:"Abraham lincoln",10:"Alexaneder hamilton",20:"Andrew Jackson",50:"Ulysses S.Grant",100:"Benjamin Franklin"}

for i in dic.keys():
    if i==number:
        print(dic[i])