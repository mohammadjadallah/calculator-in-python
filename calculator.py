from tkinter import *
from tkinter import ttk
import pyperclip as clip

root = Tk()
root.geometry('350x500')
root.title("Calculator")
root.configure(bg="#2D3A3E")
root.resizable(False, False)
largeFont = ('Comic Sans MS', 20)
fontButton = ('Comic Sans MS', 20)
style = ttk.Style()
i = 0


input_text = StringVar()

def press(x):
    global i
    i += 1
    entry.configure(state=NORMAL)
    entry.insert(i, x) 
    entry.configure(state=DISABLED)

def equalResult():
    try:
        gets = entry.get()
        result = str(eval(gets))
        input_text.set(result)

    except(ZeroDivisionError):
        clear()
        entry.configure(state=NORMAL)
        entry.insert(0, "Cannot divide by zero")
        entry.configure(state=DISABLED)

    except(SyntaxError):
        clear()
        entry.configure(state=NORMAL)
        entry.insert(0, "Syntax Error")
        entry.configure(state=DISABLED)


def copyNum():
    getText = entry.get()
    clip.copy(getText)
    clip.paste()
    root.update()


def clear():
    entry.configure(state=NORMAL)
    entry.delete(0, END)
    entry.configure(state=DISABLED)
    #input_text.set("")  # We can use this way or the above way


def remove():
    w = len(entry.get())
    entry.configure(state=NORMAL)
    entry.delete(w - 1)
    entry.configure(state=DISABLED)

#Here you can change the color Buttons 
def color_mode():
    root.configure(bg='#eaeaea')
    style.theme_use('vista')
    style.configure("TButton", foreground="black", font=fontButton, background=('#eaeaea'))
    divide = Button(root, text='/', fg="black", bg="light gray", font=("arial", 30, 'bold'),  command=lambda: press('/'))
    divide.place(width=125, height=60, y=200, x=225)
    equal = Button(root, text='=', fg="black", bg="light gray", font=("Comic Sans MS", 30, 'bold'),
                   command=lambda: equalResult())
    equal.place(width=200, height=60, y=440, x=150)

    plus = Button(root, text='+', fg="black", bg="light gray", font=("Comic Sans MS", 30, 'bold'),
                  command=lambda: press('+'))
    plus.place(width=125, height=60, y=380, x=225)

    minus = Button(root, text='ـــ', fg="black", bg="light gray", font=("arial", 30, 'bold'), command=lambda: press('-'))
    minus.place(width=125, height=60, y=320, x=225)

    multiply = Button(root, text='x', fg="black", bg="light gray", font=("arial", 30, 'bold'), command=lambda: press('*'))
    multiply.place(width=125, height=60, y=260, x=225)

    Copy = Button(root, text='copy', fg="black", bg="light gray", font=("arial", 15, 'bold'), command=lambda: copyNum())
    Copy.place(width=125, height=40, y=160, x=225)

    colorMode = Button(root, text='color mode', fg="black", bg="light gray", font=("arial", 25, 'bold'))
    colorMode.place(width=225, height=40, y=160, x=1)


# create 19 buttons and 1 entry
#('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

entry = Entry(root, textvariable=input_text, font=largeFont, bg='#2D3A3E', fg="#D6DFE0")
entry.place(width=400, height=100, y=0)

#All Buttons here :
style.theme_use('alt')
style.configure("TButton", foreground="#D6DFE0", font=fontButton, background='#2D3A3E')

zero = ttk.Button(root, text='0', command=lambda: press(0))
zero.place(width=75, height=60, y=440, x=0)

dot = ttk.Button(root, text='.', command=lambda: press('.'))
dot.place(width=75, height=60, y=440, x=75)

one = ttk.Button(root, text='1', command=lambda: press(1))
one.place(width=75, height=60, y=380, x=0)

two = ttk.Button(root, text='2', command=lambda: press(2))
two.place(width=75, height=60, y=380, x=75)

three = ttk.Button(root, text='3', command=lambda: press(3))
three.place(width=75, height=60, y=380, x=150)

four = ttk.Button(root, text='4', command=lambda: press(4))
four.place(width=75, height=60, y=320, x=0)

five = ttk.Button(root, text='5', command=lambda: press(5))
five.place(width=75, height=60, y=320, x=75)

six = ttk.Button(root, text='6', command=lambda: press(6))
six.place(width=75, height=60, y=320, x=150)

seven = ttk.Button(root, text='7', command=lambda: press(7))
seven.place(width=75, height=60, y=260, x=0)

eight = ttk.Button(root, text='8', command=lambda: press(8))
eight.place(width=75, height=60, y=260, x=75)

nine = ttk.Button(root, text='9', command=lambda: press(9))
nine.place(width=75, height=60, y=260, x=150)

equal = Button(root, text='=', fg="#D6DFE0", bg="green", font=("Comic Sans MS", 30, 'bold'), command=lambda: equalResult())
equal.place(width=200, height=60, y=440, x=150)

plus = Button(root, text='+', fg="#D6DFE0", bg="green", font=("Comic Sans MS", 30,'bold'), command=lambda: press('+'))
plus.place(width=125, height=60, y=380, x=225)

minus = Button(root, text='ـــ', fg="#D6DFE0", bg="green", font=("arial", 30,'bold'), command=lambda: press('-'))
minus.place(width=125, height=60, y=320, x=225)

multiply = Button(root, text='x', fg="#D6DFE0", bg="green", font=("arial", 30, 'bold'), command=lambda: press('*'))
multiply.place(width=125, height=60, y=260, x=225)

mod = ttk.Button(root, text='%', command=lambda: press('%'))
mod.place(width=75, height=60, y=200, x=150)

Clear = ttk.Button(root, text='C', command=lambda: clear())
Clear.place(width=75, height=60, y=200, x=75)

# btn remove

Remove = ttk.Button(root, text='rem', command=lambda: remove())
Remove.place(width=75, height=60, y=200, x=0)

divide = Button(root, text='/', fg="#D6DFE0", bg="green", font=("arial", 30,'bold'),  command=lambda: press('/'))
divide.place(width=125, height=60, y=200, x=225)

colorMode = Button(root, text='color mode', fg="#D6DFE0", bg="orange", font=("arial", 25,'bold'), command=lambda: color_mode())
colorMode.place(width=225, height=40, y=160, x=1)

Copy = Button(root, text='copy', fg="#D6DFE0", bg="GREEN", font=("arial", 15,'bold'), command=lambda: copyNum())
Copy.place(width=125, height=40, y=160, x=225)




entry.configure(state=DISABLED)
mainloop()
