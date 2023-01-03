""" midicionario={"Colombia":"Bogotá","Antioquia":"Medellin","Ecuador":"Quito"}
print(midicionario.keys())
print(len(midicionario)) """

def morse(text1):

    dic = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "- -.", "H": "....", "I": "..", "J": ".- - -", "K": "-.-", "L": ".-..", "M": "- -",
           "N": "-.", "O": "- - -", "P": ".- -.", "Q": "- -.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".- -", "X": "-..-", "Y": "-.- -", "Z": "- -.." }
    morse=""
    text2=text1.upper()
    for i in text2:
        for j in dic.keys():
            if i==j:
                morse+=dic[j]+" "
    return morse

print(morse("Pedro"))

        
