#Binary to decimal
number=(input("Enter the number you want to convert to decimal: "))[::-1]
sum=0
for i in range(0,len(number)):
    R=int(number[i])*2**(i)
    sum+=R
print(sum)

#Decimal to Binary
result=""
q = int((input("Enter the number you want to convert to decimal: ")))

while True:
    r=q%2
    result+=str(r)
    q=q//2
    if q==0:
        break

