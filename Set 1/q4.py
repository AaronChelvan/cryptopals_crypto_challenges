#!/usr/bin/python3
#Set 1 Challenge 4 - Detect single-character XOR

import binascii

with open('q4_input.txt') as f: #A text file containing the input
	inputText = f.readlines()

formattedInput = []
for i in range(len(inputText)):
	#Remove the newline character from the end of each line
	inputText[i] = inputText[i].rstrip()
	#Convert from hex to raw bytes and append to the array
	formattedInput.append(binascii.unhexlify(inputText[i]))

for i in range(len(formattedInput[0])):
	#Loop through all possible 8-bit characters
	for j in range(256):
		result = ""
		nonEnglishChar = False
		#For each character, use it to XOR every byte in inputText
		for k in range(len(formattedInput[i])):
			resultChar = chr(formattedInput[i][k]^j)
			if ord(resultChar) >= 128 and ord(resultChar) <= 237:
				nonEnglishChar = True
			result += resultChar
		if nonEnglishChar == False:
			print(str(j) + ":  " + result) #Print the result
