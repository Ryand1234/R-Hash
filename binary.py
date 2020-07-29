#!/usr/bin/env python3

import prime

def encrypt(data, number):
	prime_num = prime.get_prime(number)
	
	new_data = chr(ord(data) + prime_num) 

	return new_data

def decrypt(data, number):
	prime_num = prime.get_prime(number)
	print("Prime number is {0}".format(prime_num))

	new_data = chr(ord(data) - prime_num) 

	print("Dec data is {0}".format(new_data))

	return new_data

