position=input("Enter your position please: ")

letter=position[0]
number=int(position[-1])

if letter == "a" or letter == "c" or letter == "e" or letter == "g":
    if number%2==0: 
        print("WHITE")
    else:
        print("BLACK")
elif letter == "b" or letter == "d" or letter == "f" or letter == "h":
    if number%2!=0:
        print("WHITE")
    else:
        print("BLACK")
else:
    print("Position doesnt recognized")

