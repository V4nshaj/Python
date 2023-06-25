# Gui based program to add and show billing details using tkinter


from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Billing")
root.geometry("500x500")
frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
nameLabel = ttk.Label(frame, text="Name")
nameLabel.grid(column=0, row=0, sticky=N)
name = ttk.Entry(frame)
name.grid(column=1, row=0, sticky=(W, E))
productsLabel = ttk.Label(frame, text="Products")
productsLabel.grid(column=0, row=1, sticky=(N,S))
productsText = Text(frame, width=30, height=5)
productsText.grid(column=1, row=1, sticky=(W, E))
quantityLabel = ttk.Label(frame, text="Quantity")
quantityLabel.grid(column=0, row=2, sticky=N)
quantity = ttk.Entry(frame)
quantity.grid(column=1, row=2, sticky=(W, E))
addButton = ttk.Button(frame, text="Add")
addButton.grid(column=1, row=3, sticky=(W, E))
showDetailsText = Text(frame, width=50, height=5)
showDetailsText.grid(column=0, row=4, columnspan=2, sticky=(N, W, E, S))
clearItemsButton = ttk.Button(frame, text="Clear Items")
clearItemsButton.grid(column=0, row=5, sticky=(W, E))
totalButton = ttk.Button(frame, text="Total")
totalButton.grid(column=1, row=5, sticky=(W, E))
root.mainloop()