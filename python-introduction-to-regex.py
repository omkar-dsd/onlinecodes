import sys
import re

x = raw_input()
x = int(x)

for i in range(0,x):
    y = raw_input()
    print bool(re.match(r'^[+-]?\d*\.\d+$', y))