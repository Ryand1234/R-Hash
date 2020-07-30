#!/usr/bin/env python3

import binary

def enc_data(data):
	print("String to be encrypted is {0}".format(data))

	enc_str = ''
	j = 0;
	for i in data:
		enc_str = enc_str + binary.encrypt(i, j)
		j = j + 1

	print("encrypted String is {0}".format(enc_str))




def dec_data(data):
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
	print("	Only encrypt decrypt Operations are available");
	exit(1)



if __name__ == "__main__":
	operation = input("Type the Operation you want to use:(encrypt/decrypt) ?");
	if(operation == "encrypt"):
		data = input("Enter String to encrypt: ");
		enc_data(data);
	elif (operation == "decrypt"):
		data = input("Enter String to decrypt: ");
		dec_data(data);
	else:
		usage();
