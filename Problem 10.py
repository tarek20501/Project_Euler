'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def isPrime(n):
	if (n==0 or n==1):
		return 0
	if (n==2):
		return 1
	for x in range(2,n):
		if(n%x==0):
			return 0
		else:
			pass
	return 1

def sum_primes_below(n):
    i = 0
    summ = 0
    while (i < n):
        if (isPrime(i)==1):
            summ += i
        i = i + 1
    print(summ)
    return(summ)

sum_primes_below(2000000)