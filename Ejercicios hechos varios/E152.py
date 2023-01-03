def kemistry(string):

    f=open("elements.txt","r")
    dic={}

    for line in f.readlines():
        list=[]

        x=(line.rstrip("\n")).split(",")
        list.append(x[1])
        list.append(x[2])

        dic[int(x[0])]=list
        list=[]

    for i in dic.keys():
        if dic[i][0]==string or dic[i][-1]==string:
            print(i)
        if str(string)==str(i):
            print(dic[i])

print(kemistry(11))

    




