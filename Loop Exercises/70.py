#CAESAR CHIPER.

alphabet={}
lista=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C"]

for i in range(0,len(lista)):
    if i<26:
        alphabet[lista[i]]=lista[i+3]
print(alphabet)

msg=input("Enter the message you want to convert to Caesar Cipher: ")
TEXTO=msg.upper()
cipher=""
for j in TEXTO:
    if j==" ":
        cipher+=" "
        continue
    else:
        for k in alphabet.keys():
            if k==j:
                cipher+=alphabet[k]
print(cipher)