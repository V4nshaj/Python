import tkinter as tk#refer tkinter as tk
from tkinter import *#to install and import tkinter library
from tkinter import ttk#import ttk package which used to style the widget property and its look and feel
win=tk.Tk()#Create an instance of tkinter frame or window
#win variable
win.geometry('500x250')#window will open at this size
def change_text():
    label.configure(text="Welcome")

label=tk.Label(win, text='Click')
label.grid(column=0,row=0)

win.mainloop()