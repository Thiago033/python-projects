from tkinter import *
import math
from time import strftime
from time import gmtime

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20

reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    
    work_sec = int(work_input.get()) * 60
    short_break_sec = int(short_break_input.get()) * 60
    long_break_sec = int(long_break_input.get()) * 60
    
    
    # TESTING VARIABLES
    # work_sec = 2
    # short_break_sec = 2
    # long_break_sec = 2
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = strftime("%M:%S", gmtime(count))
    
    canvas.itemconfig(timer_text, text=count_min)
    
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
            
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1 , row=0)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="projects/pomodoro-timer/tomato.png")
canvas.create_image(100, 111, image=tomato_img)

timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(None, 25))
check_marks.grid(column=1, row=3)


#INPUTS
work_label = Label(text="Work time", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
work_label.grid(column=0 , row=4)
work_input = Entry(width=10)
work_input.insert(0, "25")
work_input.grid(column=0, row=5)


short_break_label = Label(text="Short Break Time", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
short_break_label.grid(column=1 , row=4)
short_break_input = Entry(width=10)
short_break_input.insert(0, "5")
short_break_input.grid(column=1, row=5)


long_break_label = Label(text="Long Break Time", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
long_break_label.grid(column=2 , row=4)
long_break_input = Entry(width=10)
long_break_input.insert(0, "20")
long_break_input.grid(column=2, row=5)

window.mainloop( )
