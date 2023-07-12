from tkinter import *

root=Tk()
root.title("Financial Calculator")
root.geometry("500x300")

Label(root,text="Simple Interest",font="monospace 15",fg="dark blue").place(x=50, y=-3)

def Calculate():
    dep=int(Depositentry.get())
    rate=int(Interest_rateentry.get())
    yrs=int(Yearsentry.get())
    amount =dep*(pow((1 + rate / 100),yrs))
    
    Label(text=f"{amount}",font="arial 30 bold").place(x=200,y=240)
    
    


Deposit=Label(root,text="Deposit:",font="cursive 17")
Interest_rate=Label(root,text="Interest rate:",font="cursive 17")
Years=Label(root,text="Years:",font="cursive 17")

Deposit.place(x=50, y=40)
Interest_rate.place(x=50, y=110)
Years.place(x=50,y=180)

Depositvalue=StringVar()
Interest_ratevalue=StringVar()
Yearsvalue=StringVar()

Depositentry=Entry(root, textvariable=Depositvalue, font="cursive 23",width=10)
Interest_rateentry=Entry(root, textvariable=Interest_ratevalue, font="cursive 23",width=10)
Yearsentry=Entry(root, textvariable=Yearsvalue, font="cursive 23",width=10)

Depositentry.place(x=200, y=40)
Interest_rateentry.place(x=200, y=110)
Yearsentry.place(x=200, y=180)

Button(text="Calculate",font="cursive 15",command=Calculate).place(x=390,y=40)


root.mainloop()