#https://www.hackerrank.com/challenges/validating-named-email-addresses?h_r=next-challenge&h_v=zen

import sys
import re
import email.utils

loops = raw_input()
loops = int(loops)

for i in range(0,loops):
	email_id = raw_input()
	emailadd = email.utils.parseaddr(email_id)
	matchobj = re.match(r'^\w[\w\d\._-]*@[\w]+\.\w{1,3}$',emailadd[1])


	if matchobj:
		print email_id
	else:
		continue

