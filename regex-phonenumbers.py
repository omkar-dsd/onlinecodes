#https://www.hackerrank.com/challenges/validating-the-phone-number

import sys
import re

loops = raw_input()
loops = int(loops)
for i in range(0,loops):
	phone_number = raw_input()

	if (len(phone_number)==10):
		if(re.match(r'^[789]\d{9}', phone_number)):
			print "YES"

		else:
			print "NO"
	else:
		print "NO"