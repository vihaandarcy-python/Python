from tkinter import *
import datetime

root = Tk()
root.title('Age Calculator App')
root.geometry('400x400')

frame = Frame(master=root, height=200, width=360, bg='#fab072')

lbl1 = Label(frame, text = "Name:", bg='#3895d3', fg='white', width = 12)
lbl2 = Label(frame, text = "Year:", bg='#3895d3', fg='white', width = 12)
lbl3 = Label(frame, text = "Month:", bg='#3895d3', fg='white', width = 12)
lbl4 = Label(frame, text = "Date:", bg='#3895d3', fg='white', width = 12)

name_entry = Entry(frame)
year_entry = Entry(frame)
month_entry = Entry(frame)
date_entry = Entry(frame)

def calculate():
    name = name_entry.get()
    year = int(year_entry.get())
    today = datetime.date.today()
    age = today.year - year
    greet = "Hey " + name
    message = "\nYour age is: " + str(age)
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(bg='gray', fg="#d0efff")

btn = Button(text="calculate", command=calculate, bg="red")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=50)
year_entry.place(x=150, y=50)
lbl3.place(x=20, y=80)
month_entry.place(x=150, y=80)
lbl4.place(x=20, y=110)
date_entry.place(x=150, y=110)
btn.place(x=155, y=210)
textbox.place(y=250)


root.mainloop()

