word_forward = "".join((input("Is your word a palindrome? ").split(" ")))
word_backward = "".join((word_forward[::-1].split(" ")))

if word_forward == word_backward:
    print(f"the word {word_forward} is a palydrom")
else:
    print(f"the word {word_forward} isn't a palydrom")
