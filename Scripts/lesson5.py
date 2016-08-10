# lesson5 in the tutorial

import sys			# used to parse command-line arduments and opitions
import os
import time
import math


def norm(x1=0,y1=0,x2=0,y2=0):
	dx=x2-x1
	dy=y2-y1
	n=math.sqrt((dx**2)+(dy**2))
	return n


# in python, argument are passed by reference
print norm(0,0,3,4)

# keyword argument (order doesn't matter)
print norm(x1=0,x2=3,y2=4,y1=0)

# default arguments
print norm()




# wait kep input, clear screen after
raw_input("\n\nPress the enter key to exit")
os.system('clear')
