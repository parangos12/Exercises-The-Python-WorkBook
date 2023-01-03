def cell(text1):

    cell={1:[".",",","?","!",":"],2:["A","B","C"],3:["D","E","F"],4:["G","H","I"],5:["J","K","L"],6:["M","N","O"],7:["P","Q","R","S"],8:["T","U","V"],9:["W","X","Y","Z"],0:[" "]}

    text2=text1.upper()
    final=""

    for k in range(0,len(text1)):
        for i in range(0,10):
            for j in range(0,len(cell[i])):
                if text2[k]==cell[i][j]:
                    final+=str(i)*(j+1)
    return final

print(cell("Hello, World!"))