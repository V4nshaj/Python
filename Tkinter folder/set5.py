import pprint
from tkinter import *
import tkinter as tk
from setuptools import Command
from tkinter import Tk
from tkinter import ttk
import sys

sys.stdout = open('reg.txt', 'w')
c = 'white'
m = Tk()
m.title('Car Rentals')
m.configure(bg=c)

# list for contents
compi = ['Date',
        'Receipt',
        'Company',
         'Representative ',
         'Location',
         'City/State',
         'Phone',
         'Name',
        'Licence',
        'Address',
         'City/State',
         'Phone']
n = len(compi)+2
labels = []
entry = []
k=0
j=2
for i in range(n):
        if i==2:
            Label(m, text="Rental Company Info",  font=("Arial", 13), bg=c).grid(row=i+4, column=0)
        elif i<=7:
            labels.append(Label(m, text=compi[k], bg=c))
            labels[k].grid(row=i+4, column=0)
            entry.append(Entry(m,width=30, borderwidth=5))
            entry[k].grid(row=i+4, column=1, pady=5)
            k+=1
        elif i==8:
            Label(m, text="Lessee",  font=("Arial", 13), bg=c).grid(row=j+4, column=2)
        else:
            j+=1
            labels.append(Label(m, text=compi[k], bg=c))
            labels[k].grid(row=j+4, column=2)
            entry.append(Entry(m,width=30, borderwidth=5))
            entry[k].grid(row=j+4, column=3, pady=5)
            k+=1

vech = ['VIN',
        'Make',
        'Year',
         'Color',
         'Registration',
         'Model',
         'Mileage']
j=8
n = len(vech)+j+1
labels = []
entry = []
k=0
l=j
for i in range(j,n):
        if i==8:
            Label(m, text="Vechile Information",  font=("Arial", 13), bg=c).grid(row=i+4, column=1)
        elif i<=12:
            print("i",i)
            labels.append(Label(m, text=vech[k], bg=c))
            labels[k].grid(row=i+4, column=0)
            entry.append(Entry(m,width=30, borderwidth=5))
            entry[k].grid(row=i+4, column=1, pady=5)
            k+=1
        else:
            l+=1
            labels.append(Label(m, text=vech[k], bg=c))
            labels[k].grid(row=l+4, column=2)
            entry.append(Entry(m,width=30, borderwidth=5))
            entry[k].grid(row=l+4, column=3, pady=5)
            k+=1

Button(m, text='Apply', bg=c).grid(row=225, column=0, padx=5, pady=20)
m.mainloop()
