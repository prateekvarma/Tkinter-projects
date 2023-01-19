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
timer = None  # The variable storing the current timer, globally created to provide access to the reset function

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel()  # stops the timer
    title_label.config(text="Timer", fg=GREEN)  # reset the label
    canvas.itemconfig(timer_text, text="00:00")  # reset the timer
    check_marks.config(text="")  # reset the checkmarks label
    global reps
    reps = 0  # reset the number of current reps

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # 8 done, time for a long break
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        # it's the 2nd/4th/6th rep, which are the short breaks
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        # it's the 1st/3rd/5th/7th rep, a standard work count
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:  # optional
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # Countdown timer label
    else:
        # count is 0
        start_timer()
        marks = ""  # The string with checkmarks
        work_sessions = math.floor(reps/2)  # reps/2 in the sense, for 4 sessions - 2 will be work and 2 will be breaks
        for _ in range(work_sessions):
            marks += "✅"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)  # Adding padding & color to the window

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # Extract the image from filesystem
canvas.create_image(100, 112, image=tomato_img)  # Create a canvas with half values, so it's in the center
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()
