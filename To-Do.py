import tkinter
from tkinter import *

root=Tk()
root.title("To-Do List")
root.geometry("600x600")
root.resizable(FALSE,FALSE)
root.configure(background='#f9fe77')

list1 = []
f=StringVar()

#######################     functions      ##################################
def add():
    global f,serial,list1
    serial=len(list1)
    f=e.get()
    if not f=="":
        list1.append(f)
        Lb.insert(END,' '.join((str(serial + 1),list1[-1])))
        e.delete(0, END)
    else:
        pass


def delete_all():
    Lb.delete(0, END)
    list1.clear()


def delete():
    f=e.get()
    for i in list1:
        if i==f:
            Lb.delete(0, END)
            list1.remove(f)
            for j in range (len(list1)):
                Lb.insert(END,' '.join((str(j+1),list1[j])))
            e.delete(0,END)
        else:
            pass

def sort_asc():
    list1.sort()
    Lb.delete(0, END)
    for i in range (len(list1)):
        Lb.insert(END,' '.join((str(i+1),list1[i])))
    e.delete(0,END)


def sort_dsc():
    list1.sort()
    list1.reverse()
    Lb.delete(0,END)
    for i in range (len(list1)):
        Lb.insert(END,' '.join((str(i+1),list1[i])))
    e.delete(0,END)


def search():
    f=e.get()
    Lb.delete(0,END)
    for i in range (len(list1)):
        if f==list1[i] :
            Lb.insert(END,' '.join((str(i+1),list1[i])))
        else :
            pass

def show():
    Lb.delete(0,END)
    for i in range(len(list1)):
        Lb.insert(END,' '.join((str(i+1),list1[i])))
        e.delete(0,END)

#################     buttons     ##############3###################

L1=Label(root,text="To-Do", bg='#f9fe77')
L1.grid(row=0,column=0)
L1.config(pady=10,font="bold",width=17)
e= Entry(root, width=40,textvariable=f,font=("bold",13))
e.place(x=200, y=50)


b1=Button(root, text="Add Task",font=("bold",13),width=16, height=2, command=add)
b1.grid(row=1, column=0,)

b2=Button(root, text="Search Task", font=("bold",13),width=16, height=2, command=search)
b2.grid(row=2, column=0)

b3=Button(root, text="Remove Task", font=("bold",13),width=16, height=2, command=delete)
b3.grid(row=3, column=0)

b4=Button(root, text="Clear all Tasks",font=("bold",13),width=16, height=2, command=delete_all)
b4.grid(row=4, column=0)

b5=Button(root, text="Sort(Ascending)",font=("bold",13),width=16, height=2, command=sort_asc)
b5.grid(row=5, column=0)

b6=Button(root, text="Sort(Descending)",font=("bold",13),width=16, height=2, command=sort_dsc)
b6.grid(row=6, column=0)

b7=Button(root, text="Show All", font=("bold",13),width=16, height=2, command=show)
b7.grid(row=7, column=0)

b8=Button(root, text="Exit",font=("bold",13),width=16, height=2, command=root.destroy)
b8.grid(row=8, column=0)

Lb=Listbox(root, width=40, height=20)
Lb.place(x=200,y=120)
Lb.config(font=("bold",13))

root.mainloop()
