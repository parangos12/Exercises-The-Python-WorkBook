
def polidromo(word):
    alreves=""
    for i in range(1,len(word)+1):
        alreves+=word[-i]
    if word==alreves:
        return "La palabra " + word + " es palindroma"
    else:
        return "La palabra " + word + " NO es palindroma"

print(polidromo("anna"))