import pprint
from tkinter import *
import tkinter as tk
from setuptools import Command
from tkinter import Tk
from tkinter import ttk

c = 'white'
m = Tk()
m.title('Hotel room accomadation Form')
m.configure(bg=c)

paymentLabel = Label(m, text='Payment method', bg=c)
paymentVar = IntVar()
credit = Radiobutton(m, text="Credit Card", variable=paymentVar, value=1,bg=c)
bank = Radiobutton(m, text="Direct Bank Transfer", variable=paymentVar, value=0,bg=c)
roomLabel = Label(m, text='Room Preference', bg=c)
roomVar = IntVar()
king = Radiobutton(m, text="King Bed", variable=roomVar, value=1,bg=c)
twin = Radiobutton(m, text="Twin-Two single Beds", variable=roomVar, value=0,bg=c)
#list for contents
         
names = ['Title',
         'Last Name',
         'First Name',
         'Share with',
         'Business number',
         'Mobile Number',
         'Email ID ',
         'Date of arrival',
         'Date of departure',
         'Name on credit card',
         'Credit card no.',
         'Expiry Date',
         'CVV no.',
         ]
n = len(names)
labels = []
entry = []
k=0
for i in range(n+3+3):
    if i<n:
        labels.append(Label(m, text=names[k], bg=c))
        labels[k].grid(row=i+4, column=0,sticky='w')
        entry.append(Entry(m,width=30, borderwidth=5))
        entry[k].grid(row=i+4, column=1, pady=5)
        k+=1
    elif i<n+3:
        paymentLabel.grid(row=i+4, column=0,sticky='w')
        king.grid(row=i+4,column=1)
        twin.grid(row=i+4, column=2)
    else:
        roomLabel.grid(row=i+4, column=0,sticky='w')
        credit.grid(row=i+4,column=1)
        bank.grid(row=i+4, column=2)

roomlabel = Label(m, text='Negotiated rates:', bg=c).grid(row=20,column=0,pady=5,sticky='w')
roomVar = IntVar()
roomNames = {"Deluxe room Single": "1"
                , "Deluxe room Double":"3"
                , "Suites room Single":"2"
                , "Suites room Double":"4"}
roomVar = [IntVar() for  _ in range(len(roomNames))]
room = []
z=0
k=0
v = StringVar(m, "1")
for (room_typ, value) in roomNames.items():
    if z<2:
        Radiobutton(m, text=room_typ, variable=v,
                 value=value, bg=c).grid(row=21, column=z+1)
    else:
        Radiobutton(m, text=room_typ, variable=v,
                 value=value, bg=c).grid(row=22, column=k+1)
        k+=1
    z+=1

Label(m, text="Signature").grid(row=223,column=0)
Entry(m,width=30, borderwidth=5).grid(row=223, column=1, pady=5)
Label(m, text="Pant name").grid(row=223,column=2)
Entry(m,width=20, borderwidth=5).grid(row=223, column=3, pady=5)
Label(m, text="Date").grid(row=224,column=0)
Entry(m,width=30, borderwidth=5).grid(row=224, column=1, pady=5)
Button(m, text='Submit', bg=c).grid(row=225, column=1, padx=5, pady=20)
m.mainloop()