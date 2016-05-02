## ------------------------------------- ##
## Purpose: to test if a number is prime ##
## ------------------------------------- ##
import math
def is_prime(n):
    for i in range(2, int(math.floor(n**0.5)+1)):
        if n % i == 0:
            return False
    return True
