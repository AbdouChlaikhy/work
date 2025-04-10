from tkinter import *
import tkinter

window = Tk()
window.title("Serie 10 BY Abdou ^_^")
window.geometry('400x400')

a = Label(window ,text = "Numero :").grid(row = 0,column = 0)
b = Label(window ,text = "Propritaire :").grid(row = 1,column = 0)
c = Label(window ,text = "Sold initial").grid(row = 2,column = 0)
s=Label(window,text="Euro").grid(row=2,column=2)
d = Label(window ,text = "Type").grid(row = 3,column = 0)
e=Label(window,text="Taux Interêt").grid(row=4,column=0)
e2= Label(window ,text = "%").grid(row = 4,column = 2)
f = Label(window ,text = "M.Découvert :").grid(row = 5,column = 0)


a1=Entry(window,state=tkinter.DISABLED,background="grey").grid(row=0,column=1)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
r1=Radiobutton(window,text="Courant",value=1).grid(row=3,column=1)
r2=Radiobutton(window,text="Epargne",value=2).grid(row=3,column=2)
e1= Entry(window ).grid(row = 4,column = 1)
f1=Entry(window).grid(row=5,column=1)
g=Button(window,text="Creation Compte",bg="grey").grid(row=6,column=1)


window.mainloop()