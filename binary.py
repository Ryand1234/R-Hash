#!/usr/bin/env python3

import prime

def encrypt(data, number):
	prime_num = prime.get_prime(number)
	
	new_data = chr(ord(data) + prime_num) 

	return new_data

def decrypt(data, number):
	prime_num = prime.get_prime(number)

	cur_data = ord(data) - prime_num

	new_data = chr(cur_data%128) 

	return new_data

