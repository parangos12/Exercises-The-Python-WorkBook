""" Exercise 125: Does a List contain a Sublist? """

""" def isSublist(larger,smaller):
    a=set(larger)
    b=set(smaller)
    if b.issubset(a): return True
    else: return False

print(isSublist([1,2,3,4,5],[4,5])) """


def isSublist(larger, smaller):
    a = set(larger)
    b = set(smaller)
    if b&a==b:
        return True
    else:
        return False

print(isSublist([1,2,3,4,5],[1,2,3]))