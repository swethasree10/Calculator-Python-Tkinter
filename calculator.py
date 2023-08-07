#GUI CALCULATOR:
from tkinter import *
cal=Tk()
cal.title("Calculator")

op=""
temp=""
text_inp = StringVar()

def ButtonClick(n):
    global op
    op += n
    text_inp.set(op)

def ButtonClear():
    global op
    op=' '
    text_inp.set(op)

def ButtonOp(n):
    global op
    global temp
    temp += op
    temp += n
   # print(op, temp)
    op=' '
    text_inp.set(op)
    
def ButtonEq():
    global op
    global temp
    temp += op
    print(op,temp)
    ans=str(eval(temp))
    text_inp.set(ans)
    op=""
    temp=""
    
txtDisp = Entry(cal, font=('arial', 20,'bold'), textvariable = text_inp, bd=30, insertwidth=4, bg="powder blue", justify = "right").grid(row=0,column=0,columnspan=4)

b7=Button(cal, fg="black", bg="powder blue", font=('arial', 20,'bold'),padx=16, bd=8, text='7', command = ButtonClick('7')).grid(row=1, column=0)
b8=Button(cal, fg="black", bg="powder blue",  font=('arial', 20,'bold'),padx=16, bd=8, text='8', command = lambda:ButtonClick('8')).grid(row=1, column=1)
b9=Button(cal, fg="black", bg="powder blue",  font=('arial', 20,'bold'),padx=16, bd=8, text='9', command = lambda:ButtonClick('9')).grid(row=1, column=2)
Add=Button(cal, fg="black", bg="powder blue",  font=('arial', 20,'bold'),padx=16, bd=8, text='+', command = lambda:ButtonOp('+')).grid(row=1, column=3)

b4=Button(cal, fg="black", bg="powder blue", font=('arial', 20,'bold'),padx=16, bd=8, text='4', command = lambda:ButtonClick('4')).grid(row=2, column=0)
b5=Button(cal, fg="black", bg="powder blue",  font=('arial', 20,'bold'),padx=16, bd=8, text='5', command = lambda:ButtonClick('5')).grid(row=2, column=1)
b6=Button(cal, fg="black", bg="powder blue",  font=('arial', 20,'bold'),padx=16, bd=8, text='6', command = lambda:ButtonClick('6')).grid(row=2, column=2)
Sub=Button(cal, fg="black", bg="powder blue",  font=('arial', 20,'bold'),padx=16, bd=8, text='-', command = lambda:ButtonOp('-')).grid(row=2, column=3)

b1=Button(cal, fg="black", bg="powder blue", font=('arial', 20,'bold'),padx=16, bd=8, text='1', command = lambda:ButtonClick('1')).grid(row=3, column=0)
b2=Button(cal, fg="black", bg="powder blue",  font=('arial', 20,'bold'),padx=16, bd=8, text='2', command = lambda:ButtonClick('2')).grid(row=3, column=1)
b3=Button(cal, fg="black", bg="powder blue",  font=('arial', 20,'bold'),padx=16, bd=8, text='3', command = lambda:ButtonClick('3')).grid(row=3, column=2)
Mul=Button(cal, fg="black", bg="powder blue",  font=('arial', 20,'bold'),padx=16, bd=8, text='*', command = lambda:ButtonOp('*')).grid(row=3, column=3)

b0=Button(cal, fg="black", bg="powder blue",  font=('arial', 20,'bold'),padx=16, bd=8, text='0', command = lambda:ButtonClick('0')).grid(row=4, column=0)
Clr=Button(cal, fg="black", bg="powder blue",  font=('arial', 20,'bold'),padx=16, bd=8, text='C',command=ButtonClear).grid(row=4, column=1)
Eq=Button(cal, fg="black", bg="powder blue",  font=('arial', 20,'bold'),padx=16, bd=8, text='=',command = ButtonEq).grid(row=4, column=2)
Div=Button(cal, fg="black", bg="powder blue",  font=('arial', 20,'bold'),padx=16, bd=8, text='/', command = lambda:ButtonOp('/')).grid(row=4, column=3)



cal.mainloop()

