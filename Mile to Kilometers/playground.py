def add(*args):
    sum = 0
    for n in args:
        sum += int(n)
    return sum

add(6, 5, 4,3 ,2 ,1 ,3 ,4,5)

from tkinter import *


def button_clicked():
    print("i got clicked")
    new_text = input.get()
    my_label.config(text=new_text)
def button2_command():
    my_label.config(text=input.get())
window = Tk()
window.title("My first GUI program")
window.minsize(height=300, width=500)
window.config(padx=20, pady=20)


#label
my_label = Label(text="I am a label",font=("Arial", 24, "bold"))
my_label.config(text="New text")
my_label.grid(column = 0, row= 0)

#Button
button = Button(text= "click me", command=button_clicked)
button.grid(column=1, row=1)
#button 2
button2 = Button(text="new button", command=button2_command)
button2.grid(column= 2, row=0)
#entry component
input = Entry(width= 10)
print(input.get())
input.grid(column= 3, row=3)


window.mainloop()