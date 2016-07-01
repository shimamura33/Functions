## ------------------------------------------------------------- ##
## This function calculates the sum of the digits of an integer  ##
## ------------------------------------------------------------- ##

def sum_of_digits(n):
  r = 0
	while n:
	  r, n = r + n % 10, n // 10
	return r
