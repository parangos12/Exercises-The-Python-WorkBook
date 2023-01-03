def split(sentence):

    lista = []
    word = ""
    for i in range(0,len(sentence)):
        
        if sentence[i]!=" " and sentence[i]!="." and sentence[i]!="," and sentence[i]!="!":
            word+=sentence[i]
        else:
            lista.append(word)
            word=""
   
    return lista

print(split("crack ombre eavemaria dsadsad dsa."))
