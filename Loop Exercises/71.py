#Square Root

x=float(input("Enter the number you want to calculate its square root: "))
guess=x/2
good_enough=abs(guess*guess-x)
while good_enough>10**-12:
    guess=(guess+x/guess)/2
    good_enough = abs(guess*guess-x)  #ASI SE CALCULA VALOR ABS EN PYTHON.

print(guess)
