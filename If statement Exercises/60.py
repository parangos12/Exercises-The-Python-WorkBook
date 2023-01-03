from random import randint

red=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black=[]
for i in range(0,36):
    if i not in red and i!=0:
        black.append(i)

number=randint(0,36)

if number in red:
    if 1 <= number <= 18:
        if number%2==0:
            print(f"The spin resulted in {number}\n Pay {number}\n Pay red\n Pay Even\n Pay 1 to 18")
        elif number % 2 != 0:
                print(f"The spin resulted in {number}\n Pay {number}\n Pay red\n Pay odd\n Pay 1 to 18")

    if 19 <= number <= 36:
        if number % 2 == 0:
            print(f"The spin resulted in {number}\n Pay {number}\n Pay red\n Pay Even\n Pay 19 to 36")
        elif number % 2 != 0:
            print(f"The spin resulted in {number}\n Pay {number}\n Pay red\n Pay odd\n Pay 19 to 36")

        
if number in black:
    if 1 <= number <= 18:
        if number%2==0:
            print(f"The spin resulted in {number}\n Pay {number}\n Pay black\n Pay Even\n Pay 1 to 18")
        elif number % 2 != 0:
            print(f"The spin resulted in {number}\n Pay {number}\n Pay black\n Pay odd\n Pay 1 to 18")

    if 19 <= number <= 36:
        if number % 2 == 0:
            print(f"The spin resulted in {number}\n Pay {number}\n Pay black\n Pay Even\n Pay 19 to 36")
        elif number % 2 != 0:
            print(f"The spin resulted in {number}\n Pay {number}\n Pay black\n Pay odd\n Pay 19 to 36")