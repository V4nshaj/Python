import pprint
from tkinter import *
import tkinter as tk
from setuptools import Command
from tkinter import Tk
from tkinter import ttk

c = 'white'
m = Tk()
m.title('Form')
m.configure(bg=c)

Label(m, text="Registration Form",bg='grey', font=("Arial", 15)).grid(row=0,column=1, sticky = 'e')

reg_label = Label(m, text='Registeration Period(check one):', bg=c)
reg_label.grid(row=1,column=0)
regNames = ["One year", "two year($2 discount)", "three year($3 discount)"]
regVar = [IntVar() for  p in range(len(regNames))]
regchecks = []
for i in range(len(regNames)):
    regchecks.append(Checkbutton(m, text=regNames[i], variable=regVar[i],
                 onvalue=1, offvalue=0, bg=c))
    regchecks[i].grid(row=2, column=i+1,sticky = 'w')

Label(m, text="Registration Form",bg='grey', font=("Arial", 15)).grid(row=0,column=1, sticky = 'e')
j=0
l=0
s=0
regtyp_label = Label(m, text='Registeration Type(check one):', bg=c)
regtyp_label.grid(row=15,column=0)
regtypNames = ["Original", "Renewel", "Private", "Reissue(Platters & Decal)", 
                "Reissue(Decals)", "Rental Vechile", "Transfer Liscence Plate no.",
                "for Hire", "Ride Sharing","Amatuer_radio", 'other']
regtypVar = [IntVar() for  p in range(len(regtypNames))]
regtypchecks = []
for i in range(len(regtypNames)):
    regtypchecks.append(Checkbutton(m, text=regtypNames[i], variable=regtypVar[i],
                 onvalue=1, offvalue=0, bg=c))
    if i<=3:
        regtypchecks[i].grid(row=15, column=i+1, sticky = 'w')
    elif i<=6:
        
        regtypchecks[i].grid(row=16, column=j+1, sticky = 'w')
        if i==6:
            a=Entry(m,width=30, borderwidth=5)
            a.insert(0, "Plate no.")
            a.grid(row=16, column=j+1+1, sticky = 'w')
        j+=1
    elif i<=8:
        regtypchecks[i].grid(row=17, column=l+1, sticky = 'w')
        if i==8:
            Label(m, text='Seating capacity', bg=c).grid(row=17,column=l+2)
            Entry(m,width=30, borderwidth=5).grid(row=17, column=l+3, sticky = 'w')
        l+=1

    else:
        regtypchecks[i].grid(row=18, column=s+1, sticky = 'w')
        if i==10:
            b=Entry(m,width=30, borderwidth=5)
            b.insert(0, "Specify")
            b.grid(row=18, column=s+2, sticky = 'w')
        s+=1
Label(m, text="Owner Information",bg='grey', font=("Arial", 15)).grid(row=19,column=1, sticky = 'e')
names = ['Owner Name',
         'Telephone No.',
         'Customer no.']
labels = []
entry = []
k=0
for i in range(19,22):
    labels.append(Label(m, text=names[k], bg=c))
    labels[k].grid(row=20, column=k)
    entry.append(Entry(m,width=25, borderwidth=5))
    entry[k].grid(row=21, column=k, padx=5, sticky='e')
    k+=1
nam = ['Owner resd address',
         'City',
         'State',
         'Zipcode']
label = []
entry1 = []
k=0
for i in range(4):
    label.append(Label(m, text=nam[k], bg=c))
    label[k].grid(row=22, column=k)
    entry1.append(Entry(m,width=25, borderwidth=5))
    entry1[k].grid(row=23, column=k, padx=5, sticky='e')
    k+=1
nam = ['Co-owner resd address',
         'City',
         'State',
         'Zipcode']
label = []
entry1 = []
k=0
for i in range(4):
    label.append(Label(m, text=nam[k], bg=c))
    label[k].grid(row=24, column=k)
    entry1.append(Entry(m,width=25, borderwidth=5))
    entry1[k].grid(row=25, column=k, padx=5, sticky='e')
    k+=1
nam = ['Owner email address','Co-owner email address',]
label = []
entry1 = []
k=0
j=0
for i in range(2):
    label.append(Label(m, text=nam[k], bg=c))
    label[k].grid(row=26, column=j)
    j+=1
    entry1.append(Entry(m,width=25, borderwidth=5))
    entry1[k].grid(row=26, column=j, padx=5, sticky='e')
    j+=1
    k+=1
Label(m, text="Additional Information",bg='grey', font=("Arial", 15)).grid(row=27,column=1, sticky = 'e')
reg_label = Label(m, text='Location vechile is garaged:', bg=c)
reg_label.grid(row=28,column=0)
regNames = ["City", "Country", "Town of"]
regVar = [IntVar() for  p in range(len(regNames))]
regchecks = []
for i in range(len(regNames)):
    regchecks.append(Checkbutton(m, text=regNames[i], variable=regVar[i],
                 onvalue=1, offvalue=0, bg=c))
    regchecks[i].grid(row=29, column=i+1,sticky = 'w')
    if i==2:
        Entry(m,width=25, borderwidth=5).grid(row=29, column=i+2, pady=5)
ownerLabel = Label(m, text='Owner on active military duty', bg=c)
ownerLabel.grid(row=30, column=0,sticky = 'w')
ownerVar = IntVar()
yes = Radiobutton(m, text="Yes", variable=ownerVar, value=1,bg=c)
yes.grid(row=30, column=1,sticky = 'w')
no = Radiobutton(m, text="No", variable=ownerVar, value=0,bg=c)
no.grid(row=30, column=2,sticky = 'w')

nam = ['Registration mailing address',
         'City',
         'State',
         'Zipcode']
label = []
entry1 = []
k=0
for i in range(4):
    label.append(Label(m, text=nam[k], bg=c))
    label[k].grid(row=31, column=k)
    entry1.append(Entry(m,width=25, borderwidth=5))
    entry1[k].grid(row=32, column=k, padx=5, sticky='e')
    k+=1
Button(m, text='Apply', bg='grey').grid(row=225, column=2, pady=20)
m.mainloop()