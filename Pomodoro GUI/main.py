import tkinter
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    timer_label.config("Timer")
    check_mark.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(num):
    count_minutes = math.floor(num / 60)
    count_seconds = num % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if num > 0:
        global timer
        timer = window.after(1000, count_down, num - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✓"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

#window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#canvas
canvas = Canvas(height=224, width=220, bg= YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


#Label
timer_label = Label(text="Timer", bg= YELLOW,fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column= 1, row=0)

#Start Button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column= 0, row=2)

#Reset Button
reset_button = Button(text="Reset", highlightthickness=0, command= reset_timer)
reset_button.grid(column= 2, row=2)

#checkmark
check_mark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_mark.grid(column= 1, row=3)

window.mainloop()