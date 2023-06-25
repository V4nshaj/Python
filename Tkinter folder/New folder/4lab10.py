# gui application using tkinter to show, add, update and delete phone records

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Phone List")
root.geometry("600x400")
frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=1, row=0, sticky=(N, W, E, S))
nameLabel = ttk.Label(frame, text="Name")
nameLabel.grid(column=0, row=0, sticky=N)
name = ttk.Entry(frame)
name.grid(column=1, row=0, sticky=(W, E))
phoneLabel = ttk.Label(frame, text="Phone")
phoneLabel.grid(column=0, row=1, sticky=N)
phone = ttk.Entry(frame)
phone.grid(column=1, row=1, sticky=(W, E))
addButton = ttk.Button(frame, text="Add")
addButton.grid(column=0, row=2, sticky=(W, E))
updateButton = ttk.Button(frame, text="Update")
updateButton.grid(column=1, row=2, sticky=(W, E))
deleteButton = ttk.Button(frame, text="Delete")
deleteButton.grid(column=2, row=2, sticky=(W, E))

phoneListTable = ttk.Treeview(frame,columns=("name", "phone"),show="headings")

phoneListTable.heading("name", text="Name")
phoneListTable.heading("phone", text="Phone")
phoneListTable.column("name", width=100)
phoneListTable.column("phone", width=100)
phoneListTable.insert("", 0, text="First", values=("John", "123-456-7890"))
phoneListTable.insert("", 1, text="Second", values=("Mary", "123-456-7890"))
phoneListTable.insert("", 2, text="Third", values=("July", "123-456-7890"))
phoneListTable.grid(column=0, row=3, columnspan=3, sticky=(N, W, E, S))
root.mainloop()