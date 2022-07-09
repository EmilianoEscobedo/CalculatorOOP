from tkinter import *
root=Tk()
root.title('Laingardo Calculator System')
root.geometry('200x250')
root.iconbitmap('icon.ico')
f1=Frame(root)
f1.pack()
f2=Frame(root)
f2.pack()
operation=""
o1=""
pointer=False
result=0
Ce=0
countinit=0
#---------------------screen-----------------------
number=StringVar()
screen=Entry(f1, width=26, background='black',fg='green', justify='right', textvariable=number)
screen.pack(ipady=5)
#--------------------funtions-----------------------
number.set('Laingardo Calculator System')
def ns(num):
    global Ce
    global operation
    global countinit
    if countinit==0:
        number.set("")
        countinit=1
    if operation!="":
        number.set(num)
        operation=""
    else:
        number.set(number.get()+num)
    if Ce==1:
        number.set("")
        number.set(number.get()+num)
        Ce=0
def erase():
    number.set(number.get()[:-1])
def ce():
    global result
    global ContRest
    global n1r
    global ContMult
    global n1m
    global ContDiv
    global n1d
    global Ce
    number.set(0)
    result=0
    ContRest=0
    n1r=0
    ContMult=0
    n1m=0
    ContDiv=0
    n1d=0
    Ce=1
def point():
    global pointer
    for a in number.get():
        if a==',':
            pointer=True
    if pointer==False:
        number.set(number.get()+'.')
        pointer=True
def sum(n):
    global operation
    global o1
    global result
    global pointer
    o1='sum'
    operation='sum'
    if pointer==True:
        result+=float(n)
    else:
        result+=int(n)
    number.set(result)
    pointer=False
ContRest=0
n1r=0
def rest(n):
    global operation
    global o1
    global result
    global pointer
    global ContRest
    global n1r
    o1='rest'
    operation='rest'
    if pointer==True:
        if ContRest==0:
            result=float(n)-n1r
            n1r=result
            ContRest=1
        elif ContRest==1:
            result=n1r-float(n)
            n1r=result
            ContRest=2
        else:
            result=n1r-float(n)
            n1r=result
            ContRest=1
    else: 
        if ContRest==0:
            result=int(n)-n1r
            n1r=result
            ContRest=1
        elif ContRest==1:
            result=n1r-int(n)
            n1r=result
            ContRest=2
        else:
            result=n1r-int(n)
            n1r=result
            ContRest=1
    number.set(result)
    pointer=False
ContMult=0
n1m=0
def mult(n):
    global operation
    global o1
    global result
    global pointer
    global ContMult
    global n1m
    o1='mult'
    operation='mult'
    if pointer==True:
        if ContMult==0:
            n1m=float(n)
            result=float(n)
            ContMult=1
        elif ContMult==1:
            result=n1m*float(n)
            n1m=result
            ContMult=2
        else:
            result=n1r*float(n)
            n1m=result
            ContMult=1
    else: 
        if ContMult==0:
            n1m=int(n)
            result=int(n)
            ContMult=1
        elif ContMult==1:
            result=n1m*int(n)
            n1m=result
            ContMult=2
        else:
            result=n1m*int(n)
            n1m=result
            ContMult=1
    number.set(result)
    pointer=False
ContDiv=0
n1d=0
resultd=""
def div(n):
    global operation
    global o1
    global result
    global pointer
    global ContDiv
    global n1d
    o1="div"
    operation="div"
    if pointer==True:
        if ContDiv==0:
            n1d=float(n)
            result=float(n)
            ContDiv=1
        elif ContDiv==1:
            result=n1d/float(n)
            n1d=result
            ContDiv=2
        else:
            result=n1d/float(n)
            n1d=result
            ContDiv=1
    else: 
        if ContDiv==0:
            n1d=int(n)
            result=int(n)
            ContDiv=1
        elif ContDiv==1:
            result=n1d/int(n)
            n1d=result
            ContDiv=2
        else:
            result=n1d/int(n)
            n1d=result
            ContDiv=1
    pointer=False
def resu():
    global result
    global o1
    global ContRest
    global n1r
    global ContMult
    global n1m
    global ContDiv
    global n1d
    if o1=='sum':
        sum(number.get())
        result=0
    elif o1=='rest':
        number.set(result-int(number.get()))
        ContRest=0
        n1r=0
    elif o1=='mult':
        number.set(result*int(number.get()))
        ContMult=0
        n1r=0
    elif o1=='div':
        number.set(result/int(number.get()))
        ContDiv=0
        n1d=0
#---------------------row_1------------------------
b7=Button(f2, text='7', pady=2, padx=2, width=4, height=2, command=lambda:ns('7'))
b7.grid(row=1, column=1)
b8=Button(f2, text='8', pady=2, padx=2, width=4, height=2, command=lambda:ns('8'))
b8.grid(row=1, column=2)
b9=Button(f2, text='9', pady=2, padx=2, width=4, height=2, command=lambda:ns('9'))
b9.grid(row=1, column=3)
bx=Button(f2, text='x', pady=2, padx=2, width=4, height=2, command=lambda:mult(number.get()))
bx.grid(row=1, column=4)
#---------------------row_2------------------------
b4=Button(f2, text='4', pady=2, padx=2, width=4, height=2, command=lambda:ns('4'))
b4.grid(row=2, column=1)
b5=Button(f2, text='5', pady=2, padx=2, width=4, height=2, command=lambda:ns('5'))
b5.grid(row=2, column=2)
b6=Button(f2, text='6', pady=2, padx=2, width=4, height=2, command=lambda:ns('6'))
b6.grid(row=2, column=3)
bd=Button(f2, text='/', pady=2, padx=2, width=4, height=2, command=lambda:div(number.get()))
bd.grid(row=2, column=4)
#---------------------row_3------------------------
b1=Button(f2, text='1', pady=2, padx=2, width=4, height=2, command=lambda:ns('1'))
b1.grid(row=3, column=1)
b2=Button(f2, text='2', pady=2, padx=2, width=4, height=2, command=lambda:ns('2'))
b2.grid(row=3, column=2)
b3=Button(f2, text='3', pady=2, padx=2, width=4, height=2, command=lambda:ns('3'))
b3.grid(row=3, column=3)
bm=Button(f2, text='-', pady=2, padx=2, width=4, height=2, command=lambda:rest(number.get()))
bm.grid(row=3, column=4)
#---------------------row_4------------------------
b0=Button(f2, text='0', pady=2, padx=2, width=4, height=2, command=lambda:ns('0'))
b0.grid(row=4, column=1)
bc=Button(f2, text='.', pady=2, padx=2, width=4, height=2, command=lambda:point())
bc.grid(row=4, column=2)
br=Button(f2, text='=', pady=2, padx=2, width=4, height=2, command=lambda:resu())
br.grid(row=4, column=3)
bs=Button(f2, text='+', pady=2, padx=2, width=4, height=2, command=lambda:sum(number.get()))
bs.grid(row=4, column=4)
#--------------------row_5-------------------------
b0=Button(f2, text='CE', pady=2, padx=2, width=4, height=2, command=lambda:ce())
b0.grid(row=5, column=3, columnspan=1)
b0=Button(f2, text='<-', pady=2, padx=2, width=4, height=2, command=lambda:erase())
b0.grid(row=5, column=4, columnspan=1)
name=Label(f2, width=10, height=2, bg='black', fg='white', text='LaingardoⓇ')
name.grid(row=5, column=1, columnspan=2)
root.mainloop()