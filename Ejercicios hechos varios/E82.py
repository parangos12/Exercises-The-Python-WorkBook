""" Exercise 82:Taxi Fare
(22 Lines) In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters traveled. Write a function that takes the distance traveled (in kilometers) as its only parameter and returns the total fare as its only result. Write a main program that demonstrates the function. """

def taxi_fare(distancia_km):
    base_fare=4
    change_fare=0.25
    change_meters=140
    distancia_metros=distancia_km*1000

    final_fare=base_fare+(distancia_metros//change_meters)*change_fare

    return final_fare

print(taxi_fare(2.8))



