#Q1
#Solution:
import time 
import threading
from threading import Thread 

def my_thread():
	print("My thread is ready to go for sleep")
	time.sleep(5)
	print("My thread is woke up")
	
t=Thread(target=my_thread)
t.start()


#Q2
#Solution:

import time
import threading
from threading import Thread


def display():
	for i in range(1,10):
		print(i)
		time.sleep(1)
		
		
t=Thread(target=display)
t.start()



#Q3 
#Solution:

import time
import threading
from threading import Thread

l=[11,'a','e',40,80]
def display(n):
	delay=2
	for i in l:
		time.sleep(delay)
		print(i)
		delay=delay+2

t=Thread(target=display,args=(l,))
t.start()


#Q4
#Solution:


import time
import threading
from threading import Thread
import math
def fact(n):
	print("Factorial of %d is: %d"%(n,math.factorial(n)))
	
l=int(input("Enter the number:"))
t=Thread(target=fact,args=(l,))
t.start()
