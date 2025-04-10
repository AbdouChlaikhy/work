from cgitb import text

from tkinter import *

window = Tk()
window.title("Serie 10 BY Abdou ^_^")
window.geometry('400x400')

a = Label(window ,text = "Numero :").grid(row = 0,column = 0)
b = Label(window ,text = "Propritaire :").grid(row = 1,column = 0)
c = Label(window ,text = "Sold initial").grid(row = 2,column = 0)
s=Label(window,text="Euro").grid(row=2,column=2)
d = Label(window ,text = "Type").grid(row = 3,column = 0)

b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
aa=StringVar()
r1=Radiobutton(window,text="Courant",variable=aa).grid(row=3,column=1)
r2=Radiobutton(window,text="Epargne",variable=aa).grid(row=3,column=2)


window.mainloop()



















