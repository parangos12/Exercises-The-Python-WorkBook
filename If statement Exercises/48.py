#CHINESE ZODIAC

year=int(input("Enter the year you want to know its zodiac year: "))
zodiac={8:"Dragon",9:"Snake",10:"Horse",11:"Sheep",0:"Monkey",1:"Rooster",2:"Dog",3:"Pig",4:"Rat",5:"Ox",6:"Tiger",7:"Hare"}

c=year
while 12<=c>=0:
    c-=12

for i in zodiac.keys():
    if c==i:
        print(zodiac[i])
print(c)