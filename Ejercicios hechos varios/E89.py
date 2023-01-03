def capitalize():
    text=input("Ingrese texto: ")
    
    text_capitalized=text.capitalize()

    for i in range(0,len(text_capitalized)):
        if text_capitalized[i]=="." or text_capitalized[i]=="?" or text_capitalized[i]=="!":
            cap=text_capitalized[i+2].capitalize()

            text_capitalized.replace(text_capitalized[i+2],cap)

    return text_capitalized

print("Hello world")

