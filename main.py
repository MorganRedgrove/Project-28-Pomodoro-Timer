from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
REPS = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    global check_list
    REPS = 0
    check_list = []
    check_mark["text"] = check_list

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(rep_check())

def rep_check():
    work_list = [0,2,4,6]
    s_break_list = [1,3,5]
    l_break_list = [7]

    if REPS in work_list:
        title.config(text="Work",fg=GREEN)
        return WORK_MIN
    elif REPS in s_break_list:
        check_list.append("✔")
        check_mark["text"] = check_list
        title.config(text="Break", fg=PINK)
        return SHORT_BREAK_MIN
    elif REPS in l_break_list:
        check_list.append("✔")
        check_mark["text"] = check_list
        title.config(text="Break", fg=RED)
        return LONG_BREAK_MIN

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(secs):
    global REPS

    txt_min = int(secs/60)
    txt_sec = secs%60
    if len(str(txt_sec)) <2:
        txt_sec = f"0{txt_sec}"

    canvas.itemconfig(timer, text=f"{txt_min}:{txt_sec}")

    if secs >0:
        window.after(1000,count_down, secs -1)
    elif REPS == 7:
        print("end")
        canvas.itemconfig(timer, text="00:00")
        title.config(text="Timer", fg=GREEN)
    elif secs == 0:
        REPS += 1
        count_down(rep_check())



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(125, 125, image=tomato_img)
canvas.grid(column=2, row=2)
timer = canvas.create_text(125, 145, text = "00:00", fill="White", font=("Tahoma", 25, "bold"))


title = Label(text="Timer", font=("Tahoma", 35, "bold"), bg=YELLOW, fg=GREEN)
title.grid(column=2, row=1)


check_list = []
check_mark = Label(text=check_list, font=("Tahoma", 15, "bold"), bg=YELLOW, fg=GREEN)
check_mark.grid(column=2, row=4)


start = Button(text="Start", command=start_timer)
start.grid(column=1, row=3)


reset = Button(text="Reset", command=reset_timer)
reset.grid(column=3, row=3)



window.mainloop()