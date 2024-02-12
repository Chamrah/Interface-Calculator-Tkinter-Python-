# IMPORTATION THE LIBRARY
from tkinter import *

root = Tk()
root.geometry("320x320")
root.title("Calculator")


entr1 = Entry(root,bg="#D7E4C0")
entr1.grid(row=0,column=0,sticky="we",columnspan=4,ipady=10,padx=3)

# BUTTON NUMBERS AND OPERATIONS 
# ROW1
btn1 = Button(root,text="MC",bg="#A9A9A9",fg="white",font="arial")
btn1.grid(row=1,column=0,ipadx=20,sticky="W",padx=3,pady=8,ipady=7)


btn2 = Button(root,text="MC+",bg="#A9A9A9",fg="white",font="arial")
btn2.grid(row=1,column=1,ipadx=18,padx=3,ipady=7)



btn3 = Button(root,text="/",bg="#A9A9A9",fg="white",font="arial")
btn3.grid(row=1,column=2 ,sticky="ew",ipadx=20,padx=3,ipady=7)

btn4 = Button(root,text="x",bg="#A9A9A9",fg="white",font="arial")
btn4.grid(row=1,column=3,ipadx=20,padx=3,ipady=7)

# ROW2
btn5 = Button(root,text="7",bg="#A9A9A9",fg="white",font="arial")
btn5.grid(row=2,column=0,ipadx=27,sticky="W",padx=3,ipady=7)


btn6 = Button(root,text="8",bg="#A9A9A9",fg="white",font="arial")
btn6.grid(row=2,column=1,ipadx=30,padx=3,ipady=7)



btn7 = Button(root,text="9",bg="#A9A9A9",fg="white",font="arial")
btn7.grid(row=2,column=2 ,sticky="ew",ipadx=20,padx=3,ipady=7)

btn8 = Button(root,text="-",bg="#A9A9A9",fg="white",font="arial")
btn8.grid(row=2,column=3,ipadx=20,padx=3,ipady=7)

# ROW3
btn9 = Button(root,text="6",bg="#A9A9A9",fg="white",font="arial")
btn9.grid(row=3,column=0,ipadx=27,sticky="W",padx=3,ipady=7,pady=8)


btn10 = Button(root,text="5",bg="#A9A9A9",fg="white",font="arial")
btn10.grid(row=3,column=1,ipadx=30,padx=3,ipady=7)



btn11 = Button(root,text="4",bg="#A9A9A9",fg="white",font="arial")
btn11.grid(row=3,column=2 ,sticky="ew",ipadx=20,padx=3,ipady=7)

btn12 = Button(root,text="+",bg="#A9A9A9",fg="white",font="arial")
btn12.grid(row=3,column=3,ipadx=20,padx=3,ipady=7)

# ROW4
btn13 = Button(root,text="3",bg="#A9A9A9",fg="white",font="arial")
btn13.grid(row=4,column=0,ipadx=27,sticky="W",padx=3,ipady=7)


btn14 = Button(root,text="2",bg="#A9A9A9",fg="white",font="arial")
btn14.grid(row=4,column=1,ipadx=30,padx=3,ipady=7)


btn15 = Button(root,text="1",bg="#A9A9A9",fg="white",font="arial")
btn15.grid(row=4,column=2 ,sticky="ew",ipadx=20,padx=3,ipady=7)

btn16 = Button(root,text="=",bg="orangered",fg="white",font="arial")
btn16.grid(row=4,column=3,ipadx=20,padx=3,ipady=35,rowspan=2)


# ROW5
btn17 = Button(root,text=".",bg="#A9A9A9",fg="white",font="arial")
btn17.grid(row=5,column=0,ipadx=28,sticky="W",padx=3,ipady=7,pady=8,columnspan=2)


btn18 = Button(root,text="0",bg="#A9A9A9",fg="white",font="arial")
btn18.grid(row=5,column=1,ipadx=66,padx=3,ipady=7,columnspan=2)

root.mainloop()