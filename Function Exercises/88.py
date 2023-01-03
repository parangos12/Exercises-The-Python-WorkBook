def valid(l1,l2,l3):
    maximum=max(l1,l2,l3)
    suma=abs(sum([l1,l2,l3])-maximum)
    if maximum>=suma:
        return False
    else:
        return True
print(valid(6,5,2))