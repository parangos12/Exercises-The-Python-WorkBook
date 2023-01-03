number=float(input("Enter the numbers. Finish with zero 0: "))
list=[]
while number!=0:
    list.append(int(number))
    number = float(input("Enter the numbers. Finish with zero 0: "))
sum=0
for i in list:
    sum+=i

print(list), print(sum)

print(f"The average is: {sum/len(list)}")