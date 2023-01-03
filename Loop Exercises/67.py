def charge(age):
    if age<=2:
        charge=0
    elif 3<=age<=12:
        charge=14
    elif age>=65:
        charge=18
    else:
        charge=23
    return charge

list=[]
age=input("Enter each age of the group(finish with blank space):")
while age!="":
    list.append(int(age))
    age=input("Enter each age of the group(finish with blank space):")

print(list)

total=0
for i in list:
    total+=charge(i)
print(f"The total amount to zoo's entrance is: {total}")
