# 9'11''
# trebalo je instalirati tkinter s k-dom: sudo apt-get install python3-tk

from tkinter import *

window=Tk()


b1=Button(window, text="Execute")
# b1.pack()     # ili
b1.grid(row=0, column=0)       # kojim imamo vise kontrole nad polozajem button-a 
 
e1=Entry(window)
e1.grid(row=0,column=1)

t1=Text(window)
t1.grid(row=0, column=2) 

window.mainloop() 