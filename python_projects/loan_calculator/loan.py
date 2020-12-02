from tkinter import *
class LoanCalculator():
    def __init__(self):
        window=Tk()
        window.title("Loan Calculator Application")
        window.configure(background="light blue")
        window.geometry("450x350")
        window.resizable(width=False,height=False)

        #Declaring Variables
        self.annual_ir = StringVar()
        self.years = StringVar()
        self.loan_amt = StringVar()
        self.monthly_pay = StringVar()
        self.total_pay = StringVar()
        
        #labels and Entries
        Label(window,font= "Helvetica 12 bold",text="Annual Interest Rate",bg="light blue",fg="black",width=15).grid(column=0,row=0,padx=15,pady=10)
        Entry(window,textvariable = self.annual_ir, width=25).grid(column=2,row=0,padx=15,pady=10)
        Label(window,font= "Helvetica 12 bold",text="Number of years",bg="light blue",fg="black",width=15).grid(column=0,row=1,padx=15,pady=10)
        Entry(window,textvariable = self.years, width=25).grid(column=2,row=1,padx=15,pady=10)
        Label(window,font= "Helvetica 12 bold",text="Loan Amount",bg="light blue",fg="black",width=15).grid(column=0,row=2,padx=15,pady=10)
        Entry(window,textvariable = self.loan_amt, width=25).grid(column=2,row=2,padx=15,pady=10)
        Label(window,font= "Helvetica 12 bold",text="Monthly Payment",bg="light blue",fg="black",width=15).grid(column=0,row=3,padx=15,pady=10)
        Entry(window,textvariable = self.monthly_pay, width=25).grid(column=2,row=3,padx=15,pady=10)
        Label(window,font= "Helvetica 12 bold",text="Total Payment",bg="light blue",fg="black",width=15).grid(column=0,row=4,padx=15,pady=10)
        Entry(window,textvariable = self.total_pay, width=25).grid(column=2,row=4,padx=15,pady=10)

        #Buttons
        compute_btn = Button(window,font="Helvetica 12 bold",text="Compute",bg="brown",fg="white",width=12,command=self.calculate)
        compute_btn.grid(column=0,row=6,padx=15,pady=10)
        
        clear_btn = Button(window,font="Helvetica 12 bold",text="Clear",bg="brown",fg="white",width=12,command=self.clear)
        clear_btn.grid(column=0,row=7,padx=15,pady=10)
        
        window.mainloop()

    def calculate(self):
        '''
        Calculates the total payment
        '''
        monthlyPayment = self.getMonthlyPayment(float(self.loan_amt.get()),float(self.annual_ir.get())/1200, int(self.years.get()))
        self.monthly_pay.set(format(monthlyPayment,'2.3f'))
        total = float(self.monthly_pay.get())*12* int(self.years.get())
        self.total_pay.set(format(total,'2.3f'))

    def getMonthlyPayment(self,loan,monthly_ir,n_years):
        '''
        Calculate monthly payment
        '''
        month = loan*monthly_ir/(1-1/(1+monthly_ir)**(n_years*12))
        return month

    def clear(self):
        '''
        Clears all the fields in the application
        '''
        self.annual_ir.set('')
        self.years.set('')
        self.loan_amt.set('')
        self.monthly_pay.set('')
        self.total_pay.set('')


        
LoanCalculator()
