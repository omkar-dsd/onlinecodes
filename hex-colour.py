#https://www.hackerrank.com/challenges/hex-color-code

import sys
import re

lines = raw_input()
lines = int(lines)
finalcolours = []
for i in range(0,lines):


	colouring = raw_input()
	
	if(re.match(r'^#',colouring)):
		continue
	else:
		colours = re.findall(r'#[0123456789abcdefABCDEF]{3,}',colouring)
	
		for i in colours:
			print i
