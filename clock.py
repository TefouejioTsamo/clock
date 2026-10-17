from tkinter import *
from time import *

def update():
    time_string = strftime("%H:%M:%S")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d,%Y")
    date_label.config(text=date_string)

    window.after(1000,update)


window = Tk()
window.title('clock program')

time_label = Label(window, font=("Arial", 50), fg="lightgreen", bg="black")
time_label.pack()
day_label = Label(window, font=("consolas", 25))
day_label.pack()
date_label = Label(window, font=("consolas", 30))
date_label.pack()

update()

window.mainloop()
