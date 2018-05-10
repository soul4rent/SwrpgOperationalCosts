from tkinter import *


#unsure how much of this to use



 


#tk window stuff
window = Tk()
 
window.title("Op Costs")
window.geometry('350x200')
 
lbl = Label(window, text="Astrogation Result")
lbl.grid(column=0, row=0)

lbl2 = Label(window, text="Base Time")
lbl2.grid(column=0, row=1)
 
txt = Entry(window,width=10)
 
txt.grid(column=1, row=0)
 
def AstroCalc():
    res = "Spent Fuel " + txt.get()
    lbl.configure(text=res)
 
btn = Button(window, text="Click Me", command=clicked)
 
btn.grid(column=2, row=0)

 
window.mainloop()
