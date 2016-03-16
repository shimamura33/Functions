## ---------------- ##
## Method 1 (fast)  ##
## Taken from http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188 ##
## ---------------- ##

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]


## ---------------- ##
## Method 2 (slow)  ##
## ---------------- ##

def primes(n):
    prime = []
    k = range(2,n)
    while len(k)>0:
    	i = k[0]
	k = [g for g in k if g%k[0] != 0]
    	prime.append(i)
	    if i**2 > a:
		    break
