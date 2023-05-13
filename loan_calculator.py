from tkinter import *
from tkinter import messagebox

#initialize the main window
root = Tk()
root.title('Loan Calculator')

#delete entry
def delEntry():
    entLoanAmount.delete(0,'end')
    entTax.delete(0,'end')
    entYears.delete(0,'end')
    
def messageBox():
    root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())
    #root.withdraw()
    messagebox.showerror('Invalid Input')
    root.deiconify()
    root.destroy()
    #root.quit()

#get data from Loan entry
def getDataFromLoanAmount():
    loanValue = float(entLoanAmount.get()) 
    taxValue = float(entTax.get())
    yearsValue = float(entYears.get())
#computation formulas
    totalInterest = loanValue * taxValue * yearsValue / 100
    totalLoanAmount = loanValue + totalInterest
    monthlyPay = round(totalLoanAmount / (yearsValue* 12),2)
    
    entShowTotalLoan.configure(state=NORMAL)
    entShowTotalLoan.delete(0,'end')
    entShowTotalLoan.insert(0,totalLoanAmount)
    entShowTotalLoan.configure( state=DISABLED)

#get data from Tax entry
    taxValue = entTax.get()
    entTotalTax.configure(state=NORMAL)
    entTotalTax.delete(0,'end')
    entTotalTax.insert(0,totalInterest)
    entTotalTax.configure(state=DISABLED)

#get data from year entry
    yearsValue = entYears.get()
    entMonthlyPay.configure(state=NORMAL)
    entMonthlyPay.delete(0,'end')
    entMonthlyPay.insert(0, monthlyPay)
    entMonthlyPay.configure(state=DISABLED)
        
    entShowTotalLoan.configure(state=NORMAL)
    entShowTotalLoan.delete(0,'end')
    entShowTotalLoan.insert(0,totalLoanAmount)
    entShowTotalLoan.configure(state=DISABLED)

#get data from Tax entry
    taxValue = entTax.get()
    entTotalTax.configure(state=NORMAL)
    entTotalTax.delete(0,'end')
    entTotalTax.insert(0,totalInterest)
    entTotalTax.configure(state=DISABLED)

#get data from year entry
    yearsValue = entYears.get()
    entMonthlyPay.configure(state=NORMAL)
    entMonthlyPay.delete(0,'end')
    entMonthlyPay.insert(0, monthlyPay)
    entMonthlyPay.configure(state=DISABLED)

# # widget
entLoanAmount = Entry(root, borderwidth = 5, width = 50)
lblLoan = Label(root, text='Loan Amount')
entTax = Entry(root, borderwidth = 5, width = 50)
lblTax = Label(root, text='Tax')
entYears = Entry(root, borderwidth = 5, width = 50)
lblYears = Label(root, text='Years to Pay')
Compute = Button(root, padx=30, text = 'Compute', command=getDataFromLoanAmount)
Clear = Button(root, padx=30, text='Delete', command=delEntry)
entShowResult = Entry(root, borderwidth=10, state=DISABLED)
lblTotalLoan = Label(root, text='--Total Loan--')
entShowTotalLoan = Entry(root, borderwidth = 5, width = 50,state=DISABLED)
lblTotalTax = Label(root, text='--Total Tax--')
entTotalTax = Entry(root, borderwidth = 5, width = 50,state=DISABLED)
lblMonthlyPay = Label(root, text='--Monthly pay--')
entMonthlyPay = Entry(root, borderwidth = 5, width = 50,state=DISABLED)

#labels and entry widget
lblLoan.pack()
entLoanAmount.pack()
lblTax.pack()
entTax.pack()
lblYears.pack()
entYears.pack()

#Just to seperate the button form labels and entry
Compute.pack()
Clear.pack()

#widget Pack
lblTotalLoan.pack()
entShowTotalLoan.pack()
lblTotalTax.pack()
entTotalTax.pack()
lblMonthlyPay.pack()
entMonthlyPay.pack()


#run the window
root.mainloop()

edit
