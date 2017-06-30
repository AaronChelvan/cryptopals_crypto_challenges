#!/usr/bin/python3
#Set 1 Challenge 3 - Single-byte XOR cipher

import binascii

inputText = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
inputText = binascii.unhexlify(inputText) #Convert from hex to raw bytes

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

resultsWithScore = []

#Loop through all possible 8-bit combinations
for i in range(256):
	result = ""

	#For each character, use it to XOR every byte in inputText
	for j in range(len(inputText)):
		resultChar = chr(inputText[j]^i)
		result += resultChar

	#Append the resulting text to its score, and push that to the resultsWithScore list
	resultsWithScore.append(str(wordScore(result)) + ": " + result)

resultsWithScore.sort() #Sort the list, so that the result with the highest score is at the end

#Print out the sorted list
for i in range(len(resultsWithScore)):
	print(resultsWithScore[i])
