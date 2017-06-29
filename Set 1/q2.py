#!/usr/bin/python3
#Set 1 Challenge 2 - Fixed XOR

import binascii

input1 = "1c0111001f010100061a024b53535009181c"
input1 = bytearray(binascii.unhexlify(input1)) #Convert from hex to raw bytes

input2 = "686974207468652062756c6c277320657965"
input2 = bytearray(binascii.unhexlify(input2)) #Convert from hex to raw bytes

result = ""

for i in range(len(input1)):
	resultChar = chr(input1[i]^input2[i])
	result += resultChar

# 'result' now contains (input1 XOR input2) in an array of raw bytes
print(result) #This prints "the kid don't play"
print(binascii.hexlify(b"the kid don't play")) #Converted to hex
