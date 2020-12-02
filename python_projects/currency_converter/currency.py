from tkinter import Tk, Radiobutton, Button, Label, StringVar, DoubleVar, IntVar, Entry
class CurrencyConverter():
    def __init__(self):
        window=Tk()
        window.title("Currency Converter Application")
        window.configure(background="yellow")
        window.geometry("560x350")
        window.resizable(width=False,height=False)

        #Declaring variables
        self.amt_to_convert = StringVar()
        self.conversion_rate = DoubleVar()
        self.conv_amt = StringVar()

        #Labels & Entries
        Label(window,font = 11,text="Conversion Rate (in INR)",bg="dark blue",fg="white",width=20).grid(column=0,row=0,padx=15,pady=10)
        Label(window,font= "Helvetica 12 bold",text="Amount to convert",bg="yellow",fg="black",width=15).grid(column=1,row=1,padx=15,pady=10)
        Entry(window,textvariable = self.amt_to_convert, width=16).grid(column=2,row=1,padx=15,pady=10)
        #Label(window,text="Conversion Rate",bg="purple",fg="white",width=14).grid(column=1,row=1,padx=15,pady=10)
        Label(window,font= "Helvetica 12 bold",text="Converted Amount",bg="yellow",fg="black",width=14).grid(column=1,row=2,padx=15,pady=10)
        Entry(window,textvariable = self.conv_amt, width=16).grid(column=2,row=2,padx=15,pady=10)

        #Radio Buttons
        usd = Radiobutton(window,font = 12,text="USD",variable=self.conversion_rate,value=round(0.01365,4),bg="yellow",width=12)
        usd.grid(column=0,row=1,padx=15,pady=5)
        euro = Radiobutton(window,font = 12,text="EURO",variable=self.conversion_rate,value = round(0.01160,4),bg="yellow",width=12)
        euro.grid(column=0,row=2,padx=15,pady=5)
        cad = Radiobutton(window,font = 12,text="CAD",variable=self.conversion_rate,value = round(0.01808,4),bg="yellow",width=12)
        cad.grid(column=0,row=3,padx=15,pady=5)
        aud = Radiobutton(window,font = 12,text="AUD",variable=self.conversion_rate,value= round(0.01905,4),bg="yellow",width=12)
        aud.grid(column=0,row=4,padx=15,pady=5)
        krw = Radiobutton(window,font = 12,text="KRW",variable=self.conversion_rate, value= round(15.72738,4),bg="yellow",width=12)
        krw.grid(column=0,row=5,padx=15,pady=5)

        #Buttons
        calculate_btn = Button(window,font="bold",text="Calculate",bg="brown",fg="white",width=12,command=self.calculate)
        calculate_btn.grid(column=1,row=6)
        
        clear_btn = Button(window,font="bold",text="Clear",bg="brown",fg="white",width=12,command=self.clear)
        clear_btn.grid(column=2,row=6)
        
        window.mainloop()


    def calculate(self):
        rate = float(self.conversion_rate.get())
        print(rate)
        converted = float(self.amt_to_convert.get())*rate
        self.conv_amt.set(format(converted,'.4f'))

    def clear(self):
        self.amt_to_convert.set('')
        self.conv_amt.set('')
        
CurrencyConverter()
