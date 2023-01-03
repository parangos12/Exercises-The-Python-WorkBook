def anagrams(word1,word2):
    a=set(word1)
    b=set(word2)

    if a-b==set():
        return "es un anagrama"
    else:
        return "no es una anagrama"

print(anagrams("lamina","animal"))

