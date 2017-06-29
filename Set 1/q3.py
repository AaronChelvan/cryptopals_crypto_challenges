#!/usr/bin/python3
#Set 1 Challenge 3 - Single-byte XOR cipher

import binascii

inputText = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
inputText = bytearray(binascii.unhexlify(inputText))

#Loop through all possible 8-bit characters
for i in range(256):
	result = ""

	#For each character, use it to XOR every byte in inputText
	for j in range(len(inputText)):
		resultChar = chr(inputText[j]^i)
		result += resultChar
	print(str(i) + ":  " + result) #Print the result

#When i = 88, the result is "Cooking MC's like a pound of bacon"
