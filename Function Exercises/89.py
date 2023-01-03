def capitalizar(string):
    string1=string.capitalize()
    for i in range(0,len(string1)-2):
        if string1[i]=="!" or string1[i]=="?" or string1[i]==".":
            string1=string1.replace(string1[i+2],string1[i+2].upper())
    return string1

print(capitalizar("what time do i have to be there? what’s the address? pedro eres el mejor"))
