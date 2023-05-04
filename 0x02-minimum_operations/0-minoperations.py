#!/usr/bin/python3
'''
In a text editor that can execute only two opertations COPY ALL and PASTE
Calculated the fewest number of operations needed to result n H characters
in the file
'''
def minOperations(n):
	'''
	Function that takes argument n and calculates the minimun number of
	operations needed to achieve n H characters in the file
	Implements the concept of prime factorization
	'''
	prime_factor = 2
	operations = 0
	if n > 1:
		while (prime_factor ** 2) <= n:
			while n % prime_factor == 0:
				operations += prime_factor
				n = n // prime_factor
			prime_factor += 1
		if n > 1:
			operations += n
		return operations
	return 0
