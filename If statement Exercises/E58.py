def leap(year):
    leap=False
    if year%400==0:
        leap=True
    elif year%4==0:
        leap=True
    return leap

date=input("Enter the day you want to know next day date DD/MM/AAAA: ")
list=date.split("/")
DD=int(list[0])
MM=list[1]
AAAA=int(list[-1])

dates_dic={"01":31,"02":28,"03":31,"04":30,"05":31,"06":30,"07":31,"08":31,"09":30,"10":31,"11":30,"12":31}

if DD==31 and MM==12:
    print(f"01/01/{AAAA+1}")
    exit()
elif leap(AAAA)==True:
    if DD==28 and MM=="02":
        print(f"29/02/{AAAA}")
        exit()

for i in dates_dic.keys():  
    if MM==i:
        if DD == dates_dic[i]:
            print(f"01/{int(MM)+1}/{AAAA}")
        else:
            print(f"{DD+1}/{MM}/{AAAA}")
        
print(MM)
print(dates_dic.keys())
print(type(leap(1904)))
