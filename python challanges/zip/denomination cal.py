from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTK

root = Tk()
root.geometry("650x400")
root.gonfigure(bg="blue")
root.title("Quick denomination calculator!")

upload = Image.open("----")
upload = upload.rezise((300, 300))
image = ImageTK.Photo(upload)

label1 = Label(root, image=image, bg="light blue")
label1.place(x=180, y=20)

label1 = Label(root, text="hey User! welcome to denomination counter Application.", bg="light blue")
label1.place(relx=0.5, y=340, anchor=CENTER)



def msg():
    MsgBox = messagebox.showinfo("Alert", "Do you want to calculate the denomination count?")

    if MsgBox == "ok":
        topwind()

#------------------------------
# Adding Button In Main Window
#------------------------------

button1 = Button(root, text="Let's get started", command=msg, bg="brown", fg='white')
button1.place(x=260, y=360)

def topwind():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")

    labeltop = Label(top, text="Enter total amount", bg="light grey")
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg="light grey")

    topl1 = Label(top, text="2000", bg="light grey")
    topl2 = Label(top, text="500", bg="light grey")
    topl3 = Label(top, text="100", bg="light grey")
    