import tkinter
from tkinter import *

#window
window = tkinter.Tk()
window.title("Mile to Km converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)
def miles_km():
    miles = float(input.get())
    miles *= 1.609
    label3.config(text=f"{round(miles)}")
#Entry Box1
input = Entry(width=7)
input.grid(column=1, row=0)

#label1
label =Label(text=f"is equal to")
label.grid(column=0, row=1)

#label2
label2 = Label(text="Miles")
label2.grid(column=2, row=0)

#label3  ( converter answer )
label3 = Label(text="0")
label3.grid(column=1, row=1)

#label4
label4 = Label(text="Km")
label4.grid(column=2 , row=1)

#button
button = Button(width=10, text="Calculate", command=miles_km)
button.grid(column=1, row=2)

window.mainloop()