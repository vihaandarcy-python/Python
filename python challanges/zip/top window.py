from tkinter import *

root = Tk()
root.geometry("480x300")
root.title("main")

def topwind():

    top = Toplevel()
    top.geometry("180x180")
    top.title("Toplevel")

    l2 = Label(top, text="This is toplevel window")
    l2.pack()


l=Label(root, text="This is root window")
btn= Button(root, text="Click here to open another window", command=topwind)

l.pack()
btn.pack()

root.mainloop()