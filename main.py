#!/usr/bin/env python3

import sys
import binary

data = ''

for ele in sys.argv[2:]:
	data = data + ele + ' '

data = data.strip(' ')

def enc_data():
	print("String to be encrypted is {0}".format(data))

	enc_str = ''
	j = 0;
	for i in data:
		enc_str = enc_str + binary.encrypt(i, j)
		j = j + 1

	print("encrypted String is {0}".format(enc_str))

def dec_data():
	print("String to be decrypted is {0}".format(data))

	dec_str = ''
	j = 0;
	for i in data:
		dec_str = dec_str + binary.decrypt(i, j)
		j = j + 1

	print("decrypted String is {0}".format(dec_str))

def usage():
	print("R-Hash Encrypter Decrypter")
	print("Syntax: ")
	print("	./main encrypt/decrypt <String to be encrypt or decrypt>");
	exit(1)



if __name__ == "__main__":
	if(sys.argv[1] == "encrypt"):
		enc_data();
	elif (sys.argv[1] == "decrypt"):
		dec_data();
	else:
		usage();