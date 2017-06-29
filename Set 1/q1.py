#!/usr/bin/python3
#Set 1 Challenge 1 - Convert hex to base64

import binascii
import base64

inputText = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
decodedInput = binascii.unhexlify(inputText) #Convert from hex to raw bytes
decodedInput = base64.b64encode(decodedInput) #Convert from raw bytes to base64
print(decodedInput)
