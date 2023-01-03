""" Exercise 90: Does a String Represent an Integer?
(Solved—30 Lines) In this exercise you will write a function named isInteger that determines whether or not the characters in a string represent a valid integer. When determining if a string represents an integer you should ignore any leading or trailing white space. Once this white space is ignored, a string represents an integer if its length is at least 1 and it only contains digits, or if its first character is either + or - and the first character is followed by one or more characters, all of which are digits. Write a main program that reads a string from the user and reports whether or not it represents an integer. Ensure that the main program will not run if the file containing your solution is imported into another program. """

def isInteger(a):
    a_final=str(a)
    if a_final.isdigit()==False:
        return "No es un entero"
    else:
        return "Es un entero"

print(isInteger(7838883.2))