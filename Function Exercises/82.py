def taxi(d):
    base=4
    plus=0.25
    fare=4+(d//140)*plus
    return fare

taxi1=taxi(2170)
print(taxi1)
