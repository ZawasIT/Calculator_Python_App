import tkinter as tk
from tkinter import ttk
from tkinter import *
import math 

# global variables
equation_text = ""

# def check_int(num):
#     if num - int(num) == 0:
#         return True
#     else:
#         return False

def check_int(num):
    l = len(num)
    if num[:l-3:-1]== "0.":
        num = num[:-2]

    return num
    
def find(string,char):
    pom = 0
    for letter in string:
        if letter == char:
            pom+=1
            break
    if(pom>0):
        return True
    else:
        return False

def press(num):
    global equation_text
    signs = ['*','/','+','-','.','%']
    equation_text = equation_text + str(num)

    l = len(equation_text)
    if l == 1 and equation_text[l-1] =='-':
        equation_text = equation_text
    elif((equation_text[l-2] in signs) and (equation_text[l-1] in signs)):
        equation_text = equation_text[:-1]
    
    equation_label.set(equation_text)
    

def equal():
    global equation_text

    if(find(equation_text,'%')):
        equation_text = equation_text.replace('%','*')
        equation_text+="/100"

    try:
        total = str(eval(equation_text))
        total = check_int(total)
        
        equation_label.set(total)
        equation_text = total

    except ZeroDivisionError:

         equation_label.set("arithmetic error")
         equation_text = ""

    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""

def sqrt():
    global equation_text
    
    total = math.sqrt(float(equation_text))
    total = check_int(str(total))

    equation_label.set(total)
    equation_text = str(total)

def absolute():
    global equation_text
    total = abs(float(equation_text))
    total = check_int(str(total))

    equation_label.set(total)
    equation_text = str(total)

def clear():
    global equation_text 

    equation_label.set("")
    equation_text = ""

# program view
win = tk.Tk()
win.title('Calculator')
equation_label = StringVar()

label = Label(win, textvariable=equation_label, font=('consolas',20),bg="white", width=24, height=2)
label.grid(columnspan=4,row=0)

clear = Button(win,text="C", width=9, height=4, font=35, command= clear)
clear.grid(column=0,row=1)
procent = Button(win, text="%", width=9, height=4, font=35, command= lambda: press('%')) # command
procent.grid(column=1,row=1)
sqrt = Button(win, text="Sqrt", width=9, height=4, font=35, command= sqrt)
sqrt.grid(column=2,row=1)
divide = Button(win, text="/", width=9, height=4, font=35, command= lambda: press('/'))
divide.grid(column=3,row=1)

# row 1
button7 = Button(win,text="7", width=9, height=4, font=35, command=lambda: press(7))
button7.grid(column=0,row=2)
button8 = Button(win,text="8", width=9, height=4, font=35, command=lambda: press(8))
button8.grid(column=1,row=2)
button9 = Button(win,text="9", width=9, height=4, font=35, command=lambda: press(9))
button9.grid(column=2,row=2)
multiply = Button(win, text="*", width=9, height=4, font=35, command=lambda: press('*'))
multiply.grid(column=3,row=2)

# row 2
button4 = Button(win,text="4", width=9, height=4, font=35, command=lambda: press(4))
button4.grid(column=0,row=3)
button5 = Button(win,text="5", width=9, height=4, font=35, command=lambda: press(5))
button5.grid(column=1,row=3)
button6 = Button(win,text="6", width=9, height=4, font=35, command=lambda: press(6))
button6.grid(column=2,row=3)
minus = Button(win, text="-", width=9, height=4, font=35, command=lambda: press('-'))
minus.grid(column=3,row=3)

# row 3
button1 = Button(win, text="1", width=9, height=4, font=35, command=lambda: press(1))
button1.grid(column=0,row=4)
button2 = Button(win, text="2", width=9, height=4, font=35, command=lambda: press(2))
button2.grid(column=1,row=4)
button3 = Button(win, text="3", width=9, height=4, font=35, command=lambda: press(3))
button3.grid(column=2,row=4)
plus = Button(win, text="+", width=9, height=4, font=35, command=lambda: press('+'))
plus.grid(column=3,row=4)

# row 4
button0 = Button(win, text="0", width=9, height=4, font=35, command=lambda: press(0))
button0.grid(column=0,row=5)
dot = Button(win, text=".", width=9, height=4, font=35, command=lambda: press('.'))
dot.grid(column=1,row=5)
button_abs = Button(win, text="+/-", width=9, height=4, font=35, command= absolute)
button_abs.grid(column=2,row=5)
equal = Button(win, text="=", width=9, height=4, font=35, command= equal)
equal.grid(column=3,row=5)


win.mainloop()
