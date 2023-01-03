#Letter grade to grade points.

dic={"A+":4.0,"A":4.0,"A-":3.7,"B+":3.3,"B":3.0,"B-":2.7,"C+":2.3,"C":2.0,"C-":1.7,"D+":1.3,"D":1.0,"F":0}

letter=input("Enter the grade please: ")
sum=0
counter=0
while letter!="":  
    for i in dic.keys():
        if letter==i:
            sum+=dic[i]
            counter+=1
    letter = input("Enter the grade please: ")
print(f"The average is: {sum/counter}")



