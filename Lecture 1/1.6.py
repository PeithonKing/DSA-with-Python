# squares of all the numbers from 1 to 10
print([x**2 for x in range(1,11)])
print("\n")

# Trying min(), max(), sum()
from math import sin
val = [sin(x) for x in range(10)] # range(10) is equivalent to range(0,10)
print(min(val))
print(max(val))
print(sum(val))
print("\n")

# Trying print(networks[-1:])
networks = ["Jio", "Airtel", "Vodafone", "Idea", "BSNL"]
print(networks[-1:])
# This makes a list containing only the last element from the
# list of networks and prints it.
