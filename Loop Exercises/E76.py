n=int(input("Enter the number to get the prime factors: "))
factor=2

while factor<=n:
    if n%factor==0:
        print(factor)
        n=n/factor 
    else:
        factor+=1
