def points(word):
    word2=word.upper()
    letters = {1: ["A", "E", "I", "L", "N", "O", "R",
                   "S", "T", "U"], 2: ["D", "G"], 3: ["B", "C","M","P"], 4: ["F", "H","V","W","Y"], 5: ["K"], 8: ["J", "X"],10:["Q","Z"]}
    points=0
    for i in word2:
        for j in letters.keys():
            for k in range(0,len(letters[j])):
                if i==letters[j][k]:
                    points+=j
    return points

print(points("JOSE"))
            
