#https://www.hackerrank.com/challenges/re-findall-re-finditer

import sys
import re

minion = raw_input()



minion_list = re.findall(r'(?<=[^aeiouAEIOU])[AEIOUaeiou]{2,}[^AEIOUaeiou]',minion)

#minion_list = map(lambda x: x.group(), re.finditer(r'(?<=[^aeiouAEIOU])[AEIOUaeiou]{2,}[^AEIOUaeiou]',minion))
if not minion_list:
	print "-1"
else:
	for i in minion_list:
		for j in re.findall(r'[AEIOUaeiou]{2,}',i):
			print j



