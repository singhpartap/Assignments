
#QUESTION:1 Create a dict with name and mobile number.
#           Define a GUI interface using tkinter and pack the label
#           and create a scrollbar to scroll the list of keys in the dictionary. 
#SOLUTION:
import tkinter
from tkinter import *

d={'Partap':6316222,'Nitesh':1177346,'Vivek':6316094,'sandy':631629,'dqd':6316234,'Rkmcj':456789,'hj':6316234,'Rhdgj':456789,'aafs':6316234}
root=Tk()
s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)
l=Listbox(root,yscrollcommand=s.set)
for line in d:
    l.insert(END,'this is ' +str(line))
l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview())
root.mainloop()
		   
		   
#QUESTION:2 In the same tkinter file as created above, create a function to insert items into the dictionary.
#SOLUTION:
import tkinter
from tkinter import *

root=Tk()

def show():
    a=entry.get()
    b=entry1.get()
    mylist.insert(END,a)
    dict[a]=b
    print(dict)

name=False
Mobile=False

def name(event):
    entry.delete(0,END)
    name=True

def Mobile(event):
    entry1.delete(0,END)
    Mobile=True

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
d={'Partap':6316222,'Nitesh':1177346,'Vivek':6316094,'sandy':631629,'dqd':6316234,'Rkmcj':456789,'hj':6316234,'Rhdgj':456789,'aafs':6316234}
mylist=Listbox(root,yscrollcommand=scrollbar.set)
for i in d:
    mylist.insert(END,i)
mylist.pack(fill=BOTH)


entry=Entry(root)
entry.insert(0,'name')
entry.bind("<Button>",name)
entry.pack()

entry1=Entry(root)
entry1.insert(0,'Mobile No.')
entry1.bind("<Button>",Mobile)
entry1.pack()


b=Button(root,text='Submit',command=show)
b.pack()

Scrollbar(mylist,orient="vertical")
scrollbar.config(command=mylist.yview)

#OR

scrollbar['command']=mylist.yview
root.geometry("100x100")
root.minsize(50,50)
root.maxsize(250,250)
root.mainloop()