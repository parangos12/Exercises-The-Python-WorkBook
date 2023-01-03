def days(month):
    dic={"JANUARY":31,"FEBRUARY":"28 or 29","MARCH":31,"APRIL":30,"MAY":31,"JUNE":30,"JULY":31,"AGOUST":31,"SEPTEMBER":30,"OCTOBER":31,"NOVEMBER":30,"DECEMBER":31}
    mont_ok=month.upper()

    for i in dic.keys():
        if i==mont_ok:
            return("Ese mes tiene "+str(dic[i])+" days.")

print(days("february"))
