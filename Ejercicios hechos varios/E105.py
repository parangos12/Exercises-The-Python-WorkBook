""" Exercise 105: Reverse Order (20 Lines)
Write a program that reads integers from the user and stores them in a list. Use 0 as a sentinel value to mark the end of the input. Once all of the values have been read your program should display them (except for the 0) in reverse order, with one value appearing on each line. """

def reversa():
    lista=[]
    number=int(input("Ingrese el numero por favor: "))
    while number!=0:
        lista.append(number)
        number=int(input("Ingrese el número por favor: "))
    lista.reverse()
    return lista

print(reversa())