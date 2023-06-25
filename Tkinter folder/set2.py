import pprint
from tkinter import *
import tkinter as tk
from setuptools import Command
from tkinter import Tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import sys

sys.stdout = open('reg.txt', 'w')
c = 'white'
m = Tk()
m.title('Job Application')
m.configure(bg=c)
a=Label(m, text="Education", bg=c)

edVar=StringVar()
education = ["X",
    "XII",
    "Btech",
    'Mtech',
    'CA',
    'BBA',
    'MBA']

def OpenFile():
    name = askopenfilename()
o=Button(text="Choose file", command=OpenFile)
r=Label(m, text="Resume", bg=c)

edDrop=OptionMenu(m, edVar, *education)
edVar.set('Please Choose')
edDrop.configure(bg=c)
Label(m, text="Job Application", font=("Arial", 20), fg='black'
, bg=c).grid(row=0, column=0, sticky = 'e')
Label(m, text="Personal Information", font=("Arial", 10), fg='red'
, bg=c).grid(row=1, column=0, sticky = 'w')
# list for contents
names = ['Name',
         'Email ID ',
         'Address',
         'Phone no.',
         'Hobbies',
         'Company name',
         'Job title',
         'How long were you here',
         'Name',
         'Phone',
         'Name',
         'Phone']
n = len(names)+5
labels = []
entry = []
k=0

for i in range(n):
    if i==2:
        a.grid(row=i+4, column=0, sticky = 'w')
        edDrop.grid(row=i+4, column=1,padx=50)
    elif i==3:
        r.grid(row=i+4, column=0, sticky = 'w')
        o.grid(row=i+4, column=1,padx=50,pady=15)
    elif i==7:
        Label(m, text="Precious/Current Employment Details", font=("Arial", 10), fg='red'
, bg=c).grid(row=i+4, column=0, sticky = 'w')
    elif i==11:
        Label(m, text="Reference #1", font=("Arial", 10), fg='red'
, bg=c).grid(row=i+4, column=0, sticky = 'w')
    elif i==14:
        Label(m, text="Reference #2", font=("Arial", 10), fg='red'
, bg=c).grid(row=i+4, column=0, sticky = 'w')
    else:
        labels.append(Label(m, text=names[k], bg=c))
        labels[k].grid(row=i+4, column=0, sticky = 'w')
        entry.append(Entry(m,width=30, borderwidth=5))
        entry[k].grid(row=i+4, column=1, pady=5)
        if i==1:
            entry[k].insert(0, "user@example.com")
        k+=1

values = {}



Button(m, text='Apply', bg='red').grid(row=225, column=0, padx=5, pady=20, sticky = 'e')
m.mainloop()
