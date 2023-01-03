
doc=open("grades.txt","r")
result=open("result.txt","w")
grades={"A+":"4","A":"4","A-":"3.7","B+":"3.3","B":"3","B-":"2.7","C+":"2.3","C":"2","D+":"1.3","F":"0"}

for grade in doc.readlines():
    grade1=grade.rstrip("\n")
    if grade1 not in grades.keys() and grade1 not in grades.values():
        grade1="No existo"

    for i in grades.keys():
        
        if grade1==i:
            result.write(str(grades[i])+"\n")
        elif grade1==str(grades[i]):
            result.writelines(i+"\n")
        elif grade1=="No existo":         
            result.writelines("No existe la nota"+"\n")
            break


        

