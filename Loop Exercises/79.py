import random
actual_max=0
counter_max=0

for i in range(0,100):
    x=random.randint(0,99)
    if x>actual_max:
        actual_max=x
        counter_max+=1
    
print("The maximun number was {} and it was overpassed {} times".format(actual_max,counter_max))