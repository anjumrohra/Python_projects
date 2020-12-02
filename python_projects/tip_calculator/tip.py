from tkinter import Tk, Radiobutton, Button, Label, StringVar, IntVar, Entry
class TipCalculator():
    def __init__(self):
        window = Tk()
        window.title("Tip Calculator Application")
        window.configure(background="sky blue")
        window.geometry("370x270")
        window.resizable(width=False,height=False)

        
        #Declaring Variables
        self.meal_cost = StringVar()
        self.tip_percent = IntVar()
        self.tip = StringVar()
        self.total_cost = StringVar()

        #Labels & Entries
        tip_percents = Label(window,text="Tip Percentages",bg="black",fg="white")
        tip_percents.grid(column=0,row=0,padx=15,pady=10)

        bill_amount = Label(window,text="Bill Amount",fg="black",width=12)
        bill_amount.grid(column=1,row=0,padx=15,pady=10)

        bill_amount_entry = Entry(window,textvariable=self.meal_cost,width=14)
        bill_amount_entry.grid(column=2,row=0,padx=15,pady=10)

        tip_amount = Label(window,text="Tip Amount",fg="black",width=12)
        tip_amount.grid(column=1,row=1,padx=15,pady=5)

        tip_amount_entry = Entry(window,textvariable=self.tip,width=14)
        tip_amount_entry.grid(column=2,row=1,padx=15,pady=5)

        total_amount = Label(window,text="Total Amount",fg="black",width=12)
        total_amount.grid(column=1,row=2,padx=15,pady=5)

        total_amount_entry = Entry(window,textvariable=self.total_cost,width=14)
        total_amount_entry.grid(column=2,row=2,padx=15,pady=5)

        #Radio Buttons
        five_percent = Radiobutton(window,text="5%",variable=self.tip_percent,value=5,bg="sky blue")
        five_percent.grid(column=0,row=1,padx=15,pady=5)

        ten_percent = Radiobutton(window,text="10%",variable=self.tip_percent,value=10,bg="sky blue")
        ten_percent.grid(column=0,row=2,padx=15,pady=5)

        fifteen_percent = Radiobutton(window,text="15%",variable=self.tip_percent,value=15,bg="sky blue")
        fifteen_percent.grid(column=0,row=3,padx=15,pady=5)

        twenty_percent = Radiobutton(window,text="20%",variable=self.tip_percent,value=20,bg="sky blue")
        twenty_percent.grid(column=0,row=4,padx=15,pady=5)

        twenty_five_percent = Radiobutton(window,text="25%",variable=self.tip_percent,value=25,bg="sky blue")
        twenty_five_percent.grid(column=0,row=5,padx=15,pady=5)

        thirty_percent = Radiobutton(window,text="30%",variable=self.tip_percent,value=30,bg="sky blue")
        thirty_percent.grid(column=0,row=6,padx=15,pady=5)

        #Buttons
        calculate_btn = Button(window,text="Calculate",bg="purple",fg="white",width=14,command=self.calculate)
        calculate_btn.grid(column=1,row=6)
        
        clear_btn = Button(window,text="Clear",bg="purple",fg="white",width=14,command=self.clear)
        clear_btn.grid(column=2,row=6)

        window.mainloop()

    def calculate(self):
        pre_tip = float(self.meal_cost.get())
        percentage = self.tip_percent.get()/100
        tip_amount_entry = pre_tip * percentage
        self.tip.set(tip_amount_entry)

        final_bill = pre_tip + tip_amount_entry
        self.total_cost.set(final_bill)

    def clear(self):
        self.meal_cost.set("")
        #self.tip_percent.set("")
        self.tip.set("")
        self.total_cost.set("")
        
        
TipCalculator()
