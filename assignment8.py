
#QUESTION:1
#SOLUTION:

#Many of Python's time functions handle time as a tuple of 9 numbers, as shown below −
# Index	Field	Values
# 0	4-digit year	2008
# 1	Month	1 to 12
# 2	Day	1 to 31
# 3	Hour	0 to 23
# 4	Minute	0 to 59
# 5	Second	0 to 61 (60 or 61 are leap-seconds)
# 6	Day of Week	0 to 6 (0 is Monday)
# 7	Day of year	1 to 366 (Julian day)
# 8	Daylight savings	-1, 0, 1, -1 means library determines DST
 

#QUESTION:2 
#SOLUTION:
import time
print(time.asctime(time.localtime(time.time())))


#QUESTION:3  
#SOLUTION:



from datetime import datetime
print(datetime.now().strftime("%m"))



#QUESTION:4 
#SOLUTION:

from datetime import datetime
print(datetime.now().strftime("%a"))

#QUESTION:5 
#SOLUTION:

from datetime import datetime
print(datetime.now().strftime("%d"))

#QUESTION:6  
#SOLUTION:
import time 
print(time.localtime())


#QUESTION:7
#SOLUTION:
import math
print(math.factorial(int(input("enter any number: "))))


#QUESTION:8 
#SOLUTION:
x=int(input("enter a number: "))
y=int(input("enter an another number: "))
import math
print(math.gcd(x,y))


#QUESTION:-+63
 
#1. Get current working directory.
#SOLUTION:
import os
print(os.getcwd)

#2. Get the user environment.
#SOLUTION:
import os
print(os.environ)