from tkinter import ttk
from tkinter import *
import os


bg_color = "#607f75"
green = "#BDE4A7"

def go_off():
    os.system("shutdown /s /t 1")

def stay_on():
    exit()

window = Tk()
window.title('Turn it Off ')

window.configure(background=bg_color)
window.geometry("343x200")

frame = LabelFrame(window, text="Really???")
frame.configure(background=bg_color)
frame.grid(row=1, column=1, pady = 10, padx=10, columnspan=3)

Label(
        frame,
        text="Do you want to turn me off?",
        font=("sans-serif", 15),
        bg=bg_color
    ).grid(
        row=1,
        column= 1,
        pady = 10,
        padx=10,)

ok = Button(
            window,
            text="Yep, go ahead",
            activebackground=green,
            background= bg_color,
            font=("sans-serif", 15),
            command=lambda:go_off()
        )
ok.grid(row=2, column=1, pady = 10, padx=10)


cancel = Button(
                window, 
                text="Nope, Lets wait",
                activebackground=green,
                background= bg_color,
                font=("sans-serif", 15),
                command=lambda:stay_on()
            )
cancel.grid(row=2, column=2, pady = 10, padx=10)





window.mainloop()

