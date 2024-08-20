#CPE-031 Challenge 2 - MAKE A COIN FLIP FUNCTION

import numpy as np

#The function
def coin_flip(n):
    maxflips = []
    while n > 0:
        flips = np.random.randint(0,2)
        maxflips.append(flips)
        n -= 1
    return maxflips

#Main
flipper=int(input("Welcome to coin flipper!\nHow many times do you want to flip the coin?- "))
print(coin_flip(flipper))
