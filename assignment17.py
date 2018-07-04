#Q1
#Solution:

import tkinter
from tkinter import *

def display():
	print("Hello World")
	root.destroy()
	
root=Tk()
root.geometry("500x500")
root.minsize(200,200)
root.maxsize(700,700)
b=Button(root,text="It's a Button",command=display)
b.pack()
root.mainloop()

#Q2
#Solution:
import tkinter
from tkinter import *

def display():
	print("Hello World")
	
root=Tk()
root.geometry("500x500")
root.minsize(200,200)
root.maxsize(700,700)
b=Button(root,text="It's a Button",command=display)
b.pack()
root.mainloop()

#Q3
#Solution:
import tkinter
from tkinter import *


root=Tk()
root.geometry("500x500")
root.minsize(200,200)
root.maxsize(700,700)
def display():
	print("Hello World")
	l.config(text="world")
	l.pack()
	
def show():
	root.destroy()

	
f1=Frame(root)
f1.pack(side=TOP)

f2=Frame(root)
f2.pack(side=BOTTOM)
l=Label(f1,text="Hello",width=30)
b1=Button(f2,text="It's a Button",command=display)
b2=Button(f2,text="exit",command=show)
l.pack()
b1.pack()
b2.pack()
root.mainloop()


#Q4
#Solution:

import tkinter
from tkinter import *

def show():
	print(entry.get())

root=Tk()
root.geometry("500x500")
root.minsize(200,200)
root.maxsize(700,700)

entry=Entry(root,width=30)
entry.pack()
b=Button(root,text="click it",command=show)
b.pack()
root.mainloop()