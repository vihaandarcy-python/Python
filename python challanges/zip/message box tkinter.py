from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")

def msg():
    messagebox.showwarning( "Alert", "Alert, Stop! Virus Found")

warn_btn = Button(root, text="Scan for Virus", command=msg)
warn_btn.place(x=40, y=50)



def info():
    messagebox.showinfo("Fun Fact", "Did you know that an octopus has 3 hearts!")

info_btn = Button(root, text="Wanna know a Fun Fact?", command=info, bg="#3895d3")
info_btn.place(x=40, y=100)



def question():
    messagebox.askquestion("Important!", "Are you above the age of 25?")

question_btn = Button(root, text="Get asked that..", command=question, bg='black', fg="white")
question_btn.place(x=40, y=150)


def confirmation():
    messagebox.askokcancel("Double check your Answer!", "Are you sure you are above 25?")

confirm_btn = Button(root, text="confirmation!", command=confirmation, bg='white')
confirm_btn.place(x=40, y=200)
root.mainloop()

