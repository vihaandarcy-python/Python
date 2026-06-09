from tkinter import *

screen = Tk()
screen.title("Inches to cm")
lbl1 = Label(text="inches to cm")
lbl2 = Label(text='enter inches')
input_ = Entry()

def math():
    sum_ = input_.get()
    sum_ = float(sum_)
    sum_ = sum_ * 2.54
    textbox.insert(END, sum_)

textbox = Text(height=1)
btn=Button(text="convert", command=math, bg="#3895d3")



lbl1.pack()
lbl2.pack()
input_.pack()
btn.pack()
textbox.pack()
screen.mainloop()
