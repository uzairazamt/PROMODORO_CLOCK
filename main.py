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
timer = None
rep = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Work", fg=GREEN)
    global rep
    rep = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
# defining a function that used for start button to work

def start():
    global rep
    rep += 1

    # if rep 8
    # countdown = long_break
    if rep % 8 == 0:
        # print the current break
        label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN)

    # if rep 0,2,4,6  Count = Short_Break
    elif rep % 2 == 0:
        label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN)

    # if rep 1,3,,5 ,7 ,Count= Wort_Time

    elif rep % 2 == 1:
        label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN)

        # print break label


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# defining a function for a countdown that accept seconds in count variables
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(100, count_down, count - 1)
    else:
        start()
        if rep % 2 == 0:
            check_text.config(text="✔")
        else:
            check_text.config(text="")


# ---------------------------- UI SETUP ------------------------------- #

# creating Window by holding Tk class
window = Tk()
window.title("Pomodoro Clock")
window.config(padx=103, pady=112, bg=YELLOW)

# crating label

label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 50), fg=GREEN)

# using Grid Function to show on the screen

label.grid(row=0, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# using Grid Function to show on the screen
canvas.grid(row=2, column=2)

# creating a Button name start

start_button = Button(text="Start", bg=YELLOW, font=FONT_NAME, highlightthickness=0, command=start)
# using Grid Function to show on the screen
start_button.grid(row=3, column=0)

# creating a reset Button
reset_button = Button(text="Reset", bg=YELLOW, font=FONT_NAME, highlightthickness=0, command=reset)
# using Grid Function to show on the screen
reset_button.grid(row=3, column=3)

# creating check_text variable from Label class

check_text = Label(text="", bg=YELLOW, fg=GREEN, highlightthickness=0, font=(FONT_NAME, 19))
check_text.grid(row=4, column=2)

window.mainloop()
