""" Exercise 83: Shipping Calculator
(23 Lines) An online retailer provides express shipping for many of its items at a rate of $10.95 for the first item, and $2.95 for each subsequent item. Write a function that takes the number of items in the order as its only parameter. Return the shipping charge for the order as the function’s result. Include a main program that reads the number of
items purchased from the user and displays the shipping charge. """

#shipping=shepin  (chapas llevan envios gratis)

def shipping():
    items=int(input("Ingrese el número de artículos a enviar: "))
    first_item=10.95
    other_items=2.95
    if items==1:
        cost=first_item
    elif items>1:
        cost=first_item+other_items*(items-1)
    return cost

print(shipping())


        

