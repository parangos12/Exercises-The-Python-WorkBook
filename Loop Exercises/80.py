#Coin Flip Simulation
import random
letters=["T","H"]
sum=0
for i in range(0,10):
    line=""
    while True:
        if "TTT" in line or "HHH" in line:
            print(f"{line} ({len(line)} flips)")
            sum+=len(line)
            break
        else:
            line+=random.choice(letters)
print(f"On average, {sum/10} flips were needed")