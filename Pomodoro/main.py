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
REPS = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text = "TIMER")
    checkmark_label.config(text = "")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    REPS += 1
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    work_sec = WORK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text = "BREAK", fg = PINK , bg = YELLOW)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="BREAK", fg=RED, bg=YELLOW)
    else:
        count_down(work_sec)
        title_label.config(text="WORK", fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10 :
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0 :
        global timer
        timer = window.after(1000, count_down , count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(REPS / 2)):
            mark += TEXT
        checkmark_label.config(text = mark)


# ---------------------------- UI SETUP ------------------------------- #
FG = GREEN
TEXT = "✔"
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130 , text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)

title_label = Label(text ="TIMER", fg = FG, bg = YELLOW, font = (FONT_NAME, 40, "bold"))
title_label.grid(row = 0, column = 1)

start_button = Button(text = "START", fg =RED, font = (FONT_NAME, 12 , "bold"), highlightthickness = 0, command = start_timer)
start_button.grid(row = 2, column = 0)

reset_button = Button(text = "RESET" , fg = RED, font = (FONT_NAME, 12 , "bold"), highlightthickness = 0, command = reset_timer)
reset_button.grid(row = 2, column = 2)

checkmark_label = Label(text = "", fg = FG, bg = YELLOW)
checkmark_label.grid(row = 3, column = 1)

window.mainloop()