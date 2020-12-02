from tkinter import *
#strftime retrieves the computer's time to display on the application
from time import strftime

root = Tk()
root.title("Digital Computer Clock")

def time():
    string = strftime("%H:%M:%S %p")
    lbl.config(text = string)
    lbl.after(1000, time)

lbl = Label(root, font = "arial 100 bold",bg="yellow",fg = "black")
lbl.pack(anchor ="center",fill="both",expand=1)

time()
mainloop()
