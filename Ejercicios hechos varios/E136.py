def anagrams(word1, word2):
    word3=word1.upper()
    word4=word2.upper()

    a = set(word3)
    b = set(word4)

    a.remove(" ")
    a.discard(",")
    a.discard(".")

    b.remove(" ")
    b.discard(",")
    b.discard(".")
    
    if a-b == set():
        return "es un anagrama"
    else:
        return "no es un anagrama"


print(anagrams("William Shakespeare", "I am a weakish speller"))
