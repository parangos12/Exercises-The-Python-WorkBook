#Richter Scale

mag=float(input("Enter the Ritcher Scale: "))
message=""
if mag<2:
    message="Micro"
elif 2<=mag<3:
    message="Very Minor"
elif 3<=mag<4:
    message="Minor"
elif 4<=mag<5:
    message="Light"
elif 5<=mag<6:
    message="Moderate"
elif 6<=mag<7:
    message="Strong"
elif 7<=mag<8:
    message="Major"
elif 8<=mag<10:
    message="Great"    
elif mag>=10:
    message = "Meteoric"
else:
    message="Dont recognized"
print(message)