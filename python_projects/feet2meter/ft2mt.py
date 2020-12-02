from tkinter import Tk, Button, Label, DoubleVar, Entry
window = Tk()
window.title("Feet to meter conversion app")
window.configure(background = "yellow")
window.geometry("320x220")
window.resizable(width=False,height=False)

def convert():
    value = float(ft_value.get())
    meter = value * 0.3048  # 1 feet = 0.3048 meter
    mt_value.set("%.4f" % meter)    

def clear():
    ft_value.set("")
    mt_value.set("")

ft_lbl = Label(window,text="Feet",bg="purple",fg="white",width=14)
ft_lbl.grid(column=0,row=0,padx=15,pady=15)

ft_value = DoubleVar()
ft_entry = Entry(window,textvariable=ft_value,width=14)
ft_entry.grid(column=1,row=0)
ft_entry.delete(0,'end')

mt_lbl = Label(window,text="Meter",bg="brown",fg="white",width=14)
mt_lbl.grid(column=0,row=1,padx=15,pady=15)

mt_value = DoubleVar()
mt_entry = Entry(window,textvariable=mt_value,width=14)
mt_entry.grid(column=1,row=1)
mt_entry.delete(0,'end')

convert_btn = Button(window,text="Let's convert!",bg="black",fg="white",width=16,command=convert)
convert_btn.grid(column=0,row=3,padx=15,pady=15)

clear_btn = Button(window,text="Erase!",bg="black",fg="white",width=16,command=clear)
clear_btn.grid(column=1,row=3,padx=15,pady=15)


window.mainloop()
