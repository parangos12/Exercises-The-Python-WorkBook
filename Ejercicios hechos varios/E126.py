""" Exercise 126:Generate All Sublists of a List"""
 
def isSublist(lista):
    all_lists=[]
    for i in range(0,len(lista)+1):
        for j in range(0,len(lista)+1):
            if lista[i:j] not in all_lists:
                all_lists.append(lista[i:j])

    return all_lists
isSublist([1,2,3,4,5,6])


