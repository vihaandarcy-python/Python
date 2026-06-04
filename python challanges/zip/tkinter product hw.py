from tkinter import *
from datetime import date

root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

lbl = Label(text = "Let's multiply two numbers!", fg="white", bg='#072F5F',
height=1, width=300)

n1_lbl = Label(text="Enter Number 1", bg="#3895d3")
n1_Entry = Entry()

n2_lbl = Label(text="Enter Number 2", bg="#3895d3")
n2_Entry = Entry()

def multiply():

    n1 = int(n1_Entry.get())
    n2 = int(n2_Entry.get())
    product = n1 * n2

    text_box.insert(END, "Here's the final product...\n")
    text_box.insert(END, product)

text_box = Text(height=3)

btn = Button(text='Calculate',
             command=multiply,
             height = 1,
             bg="#1261A0",
             fg='white')

lbl.pack()
n1_lbl.pack()
n1_Entry.pack()
n2_lbl.pack()
n2_Entry.pack()
btn.pack()
text_box.pack()
root.mainloop()

