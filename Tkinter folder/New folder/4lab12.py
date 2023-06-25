from tkinter import *
from tkinter import messagebox

root =Tk()
root.title('Registration Form')
root.geometry('250x300')
root.configure(bg='#dddddd')


frame1 = Label(root, bg='#dddddd')
frame1.pack()
frame2 = LabelFrame(frame1, text='Gender', padx=30, pady=10)

var =IntVar()
cb = IntVar()

Label(frame1, text='Full Name').grid(row=0, column=0, padx=5, pady=5)
Label(frame1, text='Email').grid(row=1, column=0, padx=5, pady=5)
Label(frame1, text='Password').grid(row=2, column=0, padx=5, pady=5)
Radiobutton(frame2, text='Female', variable=var, value=1).pack()
Radiobutton(frame2, text='Male', variable=var, value=2).pack(anchor=W)
Radiobutton(frame2, text='Others', variable=var, value=3).pack()
name_Tf = Entry(frame1)
name_Tf.grid(row=0, column=2)
Entry(frame1).grid(row=1, column=2)
Entry(frame1, show="*").grid(row=2, column=2)
frame2.grid(row=3, columnspan=3,padx=30)
Checkbutton(frame1, text='Accept the terms & conditions', variable=cb, onvalue=1, offvalue=0).grid(row=4, columnspan=4, pady=5)
submit_btn = Button(frame1, text="Submit", padx=50, pady=5, state=DISABLED)
submit_btn.grid(row=5, columnspan=4, pady=2)

root.mainloop()