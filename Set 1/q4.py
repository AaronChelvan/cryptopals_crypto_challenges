#!/usr/bin/python3
#Set 1 Challenge 4 - Detect single-character XOR

import binascii

#Given a word, calculate the 'score' for that word.
#Letter frequencies obtained from:
#https://www3.nd.edu/~busiforc/handouts/cryptography/Letter%20Frequencies.html
def wordScore(word):
	letterFreq = {
		"a": 0.08167,
		"b": 0.01492,
		"c": 0.02782,
		"d": 0.04253,
		"e": 0.12702,
		"f": 0.02228,
		"g": 0.02015,
		"h": 0.06094,
		"i": 0.06966,
		"j": 0.00153,
		"k": 0.00772,
		"l": 0.04025,
		"m": 0.02406,
		"n": 0.06749,
		"o": 0.07507,
		"p": 0.01929,
		"q": 0.00095,
		"r": 0.05987,
		"s": 0.06327,
		"t": 0.09056,
		"u": 0.02758,
		"v": 0.00978,
		"w": 0.02360,
		"x": 0.00150,
		"y": 0.01974,
		"z": 0.00074
	}
	word = word.lower() #Conver the word to lowercase
	score = 0
	for i in range(len(word)):
		if word[i] in letterFreq:
			score += letterFreq[word[i]]
	return score

with open('q4_input.txt') as f: #A text file containing the input
	inputText = f.readlines()

#Format the input which has been read in
formattedInput = []
for i in range(len(inputText)):
	#Remove the newline character from the end of each line
	inputText[i] = inputText[i].rstrip()
	#Convert from hex to raw bytes and append to the array
	formattedInput.append(binascii.unhexlify(inputText[i]))

resultsWithScore = []

#For each line in the formattedInput list
for i in range(len(formattedInput[0])):
	#Loop through all possible 8-bit characters
	for j in range(256):
		result = ""
		nonEnglishChar = False
		#For each character, use it to XOR every byte in inputText
		for k in range(len(formattedInput[i])):
			resultChar = chr(formattedInput[i][k]^j)
			result += resultChar
		#Append the resulting text to its score, and push that to the resultsWithScore list
		if wordScore(result) > 0:
			resultsWithScore.append(str(wordScore(result)) + ": " + result)

resultsWithScore.sort() #Sort the list, so that the result with the highest score is at the end

#Print out the sorted list
for i in range(len(resultsWithScore)):
	print(resultsWithScore[i])
