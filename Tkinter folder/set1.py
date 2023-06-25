from tkinter import *
import tkinter as tk
from setuptools import Command
from tkcalendar import *
from tkcalendar import DateEntry
from tkinter import Tk

root=Tk()#or root = Tk()
root.configure(bg='purple')
root.title("STUDENT REGISTER FORM")
#first name

label=Label(root, text="FIRST NAME", fg='white', bg='purple') 
label.grid(row=0, column=0)
label=Label(root, text=("(max 30 characters a-z and A-Z)"), fg='white', bg='purple').grid(row=0,column=2)
name=Entry(root, width=35, borderwidth=5)
name.grid(row=0, column=1)
#last name
Label(root, text="LAST NAME", fg='white', bg='purple').grid(row=1, column=0)
Label(root, text=("(max 30 characters a-z and A-Z)"), fg='white', bg='purple').grid(row=1,column=2)
lastname=Entry(root, width=35, borderwidth=5).grid(row=1, column=1, pady=10)
# Calendar

Label(root, text=("DATE OF BIRTH"), fg='white', bg='purple').grid(row=2,column=0)
cal = Calendar(root,selectmode='day',width=30).grid(row=2,column=1, padx=30)
#emailid

Label(root, text=("EMAIL ID"), fg='white', bg='purple').grid(row=3,column=0)
emailid=Entry(root, width=35, borderwidth=5).grid(row=3, column=1, padx=10, pady=10)
#mobile

mobile=Entry(root, width=35, borderwidth=5).grid(row=4, column=1, pady=10)
Label(root, text=("MOBILE NUMBER"), fg='white', bg='purple').grid(row=4,column=0)
Label(root, text=("(10 digit number)"), fg='white', bg='purple').grid(row=4,column=2)

#Radiobuttons

v = tk.IntVar()

tk.Label(root, text="GENDER", fg='white', bg='purple').grid(row=5, column=0, padx = 20)
tk.Radiobutton(root, text="Male", variable=v, value=1, fg='white', bg='purple').grid(row=5, column=1)

tk.Radiobutton(root, text="Female", variable=v, value=2, fg='white', bg='purple').place(x=330, y=354)
#address

Label(root, text=("ADDRESS"), fg='white', bg='purple').grid(row=6,column=0)
address=Entry(root, width=50, borderwidth=5).grid(row=6, column=1,padx=20, pady=10, ipady=30)
#city

Label(root, text="CITY", fg='white', bg='purple').grid(row=7, column=0)
Label(root, text=("(max 30 characters a-z and A-Z)"), fg='white', bg='purple').grid(row=7,column=2)
city=Entry(root, width=35, borderwidth=5).grid(row=7, column=1, pady=10)

#pincode

Label(root, text=("PIN CODE"), fg='white', bg='purple').grid(row=8,column=0)
Label(root, text=("(6 digit number)"), fg='white', bg='purple').grid(row=8,column=2)
pincode=Entry(root, width=35, borderwidth=5).grid(row=8, column=1, pady=10)
#state 

Label(root, text="STATE", fg='white', bg='purple').grid(row=9, column=0)
Label(root, text=("(max 30 characters a-z and A-Z)"), fg='white', bg='purple').grid(row=9,column=2)
state=Entry(root, width=35, borderwidth=5).grid(row=9, column=1, pady=10)

#country
Label(root, text="COUNTRY", fg='white', bg='purple').grid(row=10, column=0)
country=Entry(root, width=35, borderwidth=5).grid(row=10, column=1, pady=10)
#checkbox

Label(root, text="HOBBIES", fg='white', bg='purple').grid(row=11, column=0)
var1 = IntVar()
Checkbutton(root, text="Drawing", variable=var1, fg='white', bg='purple').grid(row=11,column=1 )
var2 = IntVar()
Checkbutton(root, text="Singing", variable=var2, fg='white', bg='purple').place(x=330, y=674)
var3 = IntVar()
Checkbutton(root, text="Dancing", variable=var2, fg='white', bg='purple').place(x=400, y=674)
var4 = IntVar()
Checkbutton(root, text="Sketching", variable=var2, fg='white', bg='purple').place(x=480, y=674)
var4 = IntVar()
Checkbutton(root, text="Others", variable=var2, fg='white', bg='purple').grid(row=12,column=1)
state=Entry(root, width=35, borderwidth=5).place(x=325, y=704)

#radiobuttons

Label(root, text="QUALIFICATION", fg='white', bg='purple').grid(row=13, column=0, pady=30)
Label(root, text="SLNo.", fg='white', bg='purple').grid(row=13, column=1, pady=15)
Label(root, text="1", fg='white', bg='purple').grid(row=14, column=1)
Label(root, text="2", fg='white', bg='purple').grid(row=15, column=1)
Label(root, text="3", fg='white', bg='purple').grid(row=16, column=1)
Label(root, text="4", fg='white', bg='purple').grid(row=17, column=1)
Label(root, text="EXAMINATION", fg='white', bg='purple').grid(row=13, column=2)
Label(root, text="Class X", fg='white', bg='purple').grid(row=13, column=2)
Label(root, text="Class XII", fg='white', bg='purple').grid(row=13, column=2)
Label(root, text="", fg='white', bg='purple').grid(row=13, column=2)
Label(root, text="BOARD", fg='white', bg='purple').grid(row=13, column=3)
Label(root, text="PERCENTAGE", fg='white', bg='purple').grid(row=13, column=4)
Label(root, text="YEAR OF PASSING", fg='white', bg='purple').grid(row=13, column=5)
# Entry(root, width=35, borderwidth=5).grid(row=13, column=1, pady=10)

'''
v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [("Python", 101), ("Perl", 102), ("Java", 103), ("C++", 104), ("C", 105)]

def ShowChoice():
    print(v.get())

tk.Label(root, text="Choose your favourite programming language:", justify = tk.LEFT, padx = 20).pack()

for language, val in languages:
    tk.Radiobutton(root, text=language, padx = 20, variable=v, command=ShowChoice, value=val).pack(anchor=tk.W)

'''
#output

def submit():
    print("First Name: %s\nLast Name: %s" % (name.get(), lastname.get()))
    if v.get()==1:
        print("Gender: Male")
    else:
        print("Gender: Female")

#show

# root.Button(root, text='Submit', command=printInput).grid(row=3, column=1, sticky=root.W, pady=4)

root.mainloop()