word_forward=input("Is your word a palindrome? ")
word_backward=""
for i in range(len(word_forward)-1,-1,-1):
    word_backward=word_backward+word_forward[i]
if word_forward==word_backward:
    print(f"the word {word_forward} is a palydrom")
else:
    print(f"the word {word_forward} isn't a palydrom")
    print(word_backward) 

#METODO MÁS RAPIDO
word_forward=input("Is your word a palindrome? ")
word_backward=word_forward[::-1]
if word_forward == word_backward:
    print(f"the word {word_forward} is a palydrom")
else:
    print(f"the word {word_forward} isn't a palydrom")
    print(word_backward)