#calculator

from tkinter import*

def btnClick(numbers):
    global operator
    operator = operator+str(numbers)
    text_input.set(operator)

def btnClear():
    global operator
    operator= ""
    text_input.set("")

def btnEqual():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator= ""

cal = Tk()
cal.title('Calculator')

operator = ""
text_input = StringVar()

text_entry = Entry(cal, font=('arial',20,'bold'), textvariable=text_input, bd=30, bg='powder blue', justify='right').grid(row=0, columnspan=4)

btn7 = Button(cal, bd=2, font=('arial',20,'bold'), padx=16, pady=16, fg='black', bg='powder blue', text='7', command=lambda:btnClick(7)).grid(row=1, column=0)
btn8 = Button(cal, bd=2, font=('arial',20,'bold'), padx=16, pady=16, fg='black', bg='powder blue', text='8', command=lambda:btnClick(8)).grid(row=1, column=1)
btn9 = Button(cal, bd=2, font=('arial',20,'bold'), padx=16, pady=16, fg='black', bg='powder blue', text='9', command=lambda:btnClick(9)).grid(row=1, column=2)

btn4 = Button(cal, bd=2, font=('arial',20,'bold'), padx=16, pady=16, fg='black', bg='powder blue', text='4', command=lambda:btnClick(4)).grid(row=2, column=0)
btn5 = Button(cal, bd=2, font=('arial',20,'bold'), padx=16, pady=16, fg='black', bg='powder blue', text='5', command=lambda:btnClick(5)).grid(row=2, column=1)
btn6 = Button(cal, bd=2, font=('arial',20,'bold'), padx=16, pady=16, fg='black', bg='powder blue', text='6', command=lambda:btnClick(6)).grid(row=2, column=2)

btn1 = Button(cal, bd=2, font=('arial',20,'bold'), padx=16, pady=16, fg='black', bg='powder blue', text='1', command=lambda:btnClick(1)).grid(row=3, column=0)
btn2 = Button(cal, bd=2, font=('arial',20,'bold'), padx=16, pady=16, fg='black', bg='powder blue', text='2', command=lambda:btnClick(2)).grid(row=3, column=1)
btn3 = Button(cal, bd=2, font=('arial',20,'bold'), padx=16, pady=16, fg='black', bg='powder blue', text='3', command=lambda:btnClick(3)).grid(row=3, column=2)

btn0 = Button(cal, bd=2, font=('arial',20,'bold'), padx=16, pady=16, fg='black', bg='powder blue', text='0', command=lambda:btnClick(0)).grid(row=4, column=0)
equal = Button(cal, bd=2, font=('arial',20,'bold'), padx=16, pady=16, fg='black', bg='powder blue', text='=', command=btnEqual).grid(row=4, column=1)
clear = Button(cal, bd=2, font=('arial',20,'bold'), padx=16, pady=16, fg='black', bg='powder blue', text='C', command=btnClear).grid(row=4, column=2)

add = Button(cal, bd=2, font=('arial',20,'bold'), padx=16, pady=16, fg='black', bg='powder blue', text='+', command=lambda:btnClick("+")).grid(row=1, column=3)
sub = Button(cal, bd=2, font=('arial',20,'bold'), padx=16, pady=16, fg='black', bg='powder blue', text='-', command=lambda:btnClick("-")).grid(row=2, column=3)
mul = Button(cal, bd=2, font=('arial',20,'bold'), padx=16, pady=16, fg='black', bg='powder blue', text='*', command=lambda:btnClick("*")).grid(row=3, column=3)
div = Button(cal, bd=2, font=('arial',20,'bold'), padx=16, pady=16, fg='black', bg='powder blue', text='/', command=lambda:btnClick("/")).grid(row=4, column=3)

cal.mainloop()
