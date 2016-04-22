## ------------------------------------- ##
## Purpose: to test if a number is prime ##
## ------------------------------------- ##

def is_prime(n):
    for i in range(2, int(math.floor(n**0.5))):
        if n % i == 0:
            return False
    return True
