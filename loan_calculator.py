import tkinter as tk
import tkinter.font as font
from tkinter import *


#click the CLEAR Button
def clearButton(root):    
    for widget in root.winfo_children():
        if not isinstance(widget,tk.Entry):
            clearButton(widget)
        elif isinstance(widget,tk.Entry):
            widget.delete(0, tk.END)


#click the COMPUTE Button
def computeButton():
    pass

#Compute the Monthly Payment
def computeMonthlyPayment():
    pass

#Compute the Total Payment
def computeTotalPayment():
    pass       


#Initialize the main window    
root = tk.Tk()
root.title("Loan Calculator")
root.resizable(False,False)
root.geometry("284x497")

#icon beside the title
image_icon = tk.PhotoImage(file="C:\images\profit.png")
root.iconphoto(False,image_icon)

#top image (Loan Calculator)
logo_image = tk.PhotoImage(file="C:\images\imagetop1.png")
Label(root,image=logo_image).place(x=0, y=-2)

#loan amount
Label(root, text="Loan Amount").place(x=20, y=99)

#Interest Rate
Label(root, text="Annual Interest Rate").place(x=20, y=149)

#years to pay
Label(root,text="Years to Pay").place(x=20, y=199)

#Monthly Payment
Label(root, text="Monthly Payment").place(x=20, y=328)

#Total Payment
Label(root, text="Total Payment").place(x=20, y=368)

#Total Interest
Label(root, text="Total Interest").place(x=20, y=409)

#footer
Label(root, text="Created by: SoftDev TM", bg='light blue').place(x=71, y=457)

#create clear button
Button(root, text="CLEAR", bg='#676767', fg='white', command=lambda:clearButton(root)).place(x=30, y=250, width=100, height=30)

#create compute button
Button(root, text="COMPUTE", bg='#676767', fg='white').place(x=150, y=250, width=100, height=30)

#Line Separator
line_between = tk.PhotoImage(file="C:\images\Group3.png" )
Label(root, image=line_between).place(x=0, y=300, width=284)

#taking inputs for loan
#loanVar =  StringVar()
Entry(root, bd=2, font="bold", justify=LEFT).place(x=140, y=90, width=126, height=30)

#taking inputs for interest rate
#annualInterestVar = StringVar()
Entry(root, bd=2, font="bold", justify=LEFT).place(x=140, y=140, width=81, height=30)

#taking inputs for Years to pay
#yearsPayVar = StringVar()
Entry(root, bd=2, font="bold", justify=LEFT).place(x=140, y=189, width=81, height=30)

#output for Monthly payment
monthlyPaymentVar = StringVar()
Label(root, font="bold", textvariable=monthlyPaymentVar, justify=LEFT).place(x=141, y=322)

#output for total Payment
totalPaymentVar = StringVar()
Label(root, font="bold", textvariable=monthlyPaymentVar, justify=LEFT).place(x=141, y=362)

#output for total interest
totalInterestVar = StringVar()
Label(root, font="bold", textvariable=totalInterestVar, justify=LEFT).place(x=141, y=402)

root.mainloop()


    





        