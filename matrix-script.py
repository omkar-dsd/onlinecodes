#https://www.hackerrank.com/challenges/matrix-script

from __future__ import print_function
import sys
import re


r,c = raw_input().split()
r = int(r)
c = int(c)

neo_matrix = [[0 for x in range(c)] for x in range(r)]
matrix_neo = []
symbols = []
for i in range(0,r):

	temp = raw_input()
	neo_matrix[i] = list(temp)

for i in range(0,c):
	for j in range (0,r):
		matrix_neo.append(neo_matrix[j][i])

sentence = ''.join(matrix_neo)
#re.sub(r'[\w\d][!@#\$%&\s]+[\w\d]'," ", sentence)
#for i in re.findall(r'(?<=[\w\d])[!@#\$%&\s]+(?=[\w\d])', sentence):
	#print i
    #symbols.append(''.join(re.findall(r'[!@#\$%&]+', i)))

asi = re.split('(?<=[\w\d])[!@#\$%&\s]+(?=[\w\d])', sentence)
for i in asi:
    print(i, end='')
    print(" ", end='')
