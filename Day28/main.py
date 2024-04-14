
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
def reset():
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks.config(text="")
    label.config(text="Timer", fg=GREEN)
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 is not 0:
        label.config(text="Work", fg=GREEN)
        tick(work_sec)
    else:
        if reps == 8:
            label.config(text="Break", fg=RED)
            tick(long_break_sec)
        else:
            label.config(text="Break", fg=PINK)
            tick(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def tick(count):
    global reps
    minutes = math.floor(count / 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    seconds = math.floor(count % 60)
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, tick, count - 1)
    else:
        start()
        marks = ''.join(["✔" for count in range(math.floor(reps / 2))])
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.config(bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)

label = Label(text="Timer")
label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
label.grid(column=1, row=0)

# highlightthickness does nothing here =(
start_btn = Button(text="Start", command=start, highlightthickness=0)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", command=reset, highlightthickness=0)
reset_btn.grid(column=2, row=2)

checkmarks = Label(text="")
checkmarks.config(bg=YELLOW, fg=GREEN)
checkmarks.grid(column=1, row=3)

window.mainloop()