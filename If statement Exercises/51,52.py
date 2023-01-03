#Letter grade to grade points.

dic={"A+":4.0,"A":4.0,"A-":3.7,"B+":3.3,"B":3.0,"B-":2.7,"C+":2.3,"C":2.0,"C-":1.7,"D+":1.3,"D":1.0,"F":0}

""" letter=input("Enter the grade please: ")

for i in dic.keys():
    if letter==i:
        print("The grade for "+letter+" is",dic[i]) """

#Letter points to letter grade.

grade = float(input("Enter the grade please: "))

list=[]
letter=""
if grade>4:
    letter="A+"
    print(letter)
    exit()                      #PARA TERMINAR UN PROGRAMA EN PYTHON exit()
elif grade==4:
    letter="A"
    print(letter)
    exit()

for i in dic.values():
    list.append(abs(grade-i))

list.sort()
nearest=round(list[0],2)
final_grade1=round(nearest+grade,2)
final_grade2=round(grade-nearest,2)

for j in dic.keys():
    if final_grade1==dic[j] or final_grade2==dic[j]:
        print("The grade is:",j)