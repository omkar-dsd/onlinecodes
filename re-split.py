#https://www.hackerrank.com/challenges/re-split
#Re.split function by , .

import re

minion = raw_input()
minion_list = re.split('[,.]', minion)

for i in minion_list:
	if(re.match(r'\d',i)):
		print i