""" Exercise 84: Median of Three Values (Solved—42 Lines) Write a function that takes three numbers as parameters, and returns the median value of those parameters as its result. Include a main program that reads three values from the user and displays their median. """

def media(a,b,c):
    if a > b > c or c>b>a:
        media=b
    elif b>c>a or a>c>b:
        media=c
    else:
        media=a 

    return media 

print(media(9978,1050,4000))

