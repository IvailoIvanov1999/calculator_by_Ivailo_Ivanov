from tkinter import *


def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)

    eq_label.set(equation_text)


def equal():
    global equation_text
    try:
        total = str(eval(equation_text))

        eq_label.set(total)

        equation_text = total

    except SyntaxError:
        eq_label.set("Syntax error")
        equation_text = ''
    except ZeroDivisionError:
        eq_label.set("Cannot divide by 0")
        equation_text = ''


def clear():
    global equation_text
    eq_label.set("")
    equation_text = ""



root = Tk()
root.title("Calculator-by-Ivailo_Ivanov")
root.geometry("295x480")

equation_text = ''

eq_label = StringVar()

label = Label(root, textvariable=eq_label,font=('Times', 23), bg="white", width=50, height=2)
label.pack()

frame = Frame(root)
frame.pack()


button_one = Button(frame, text=1, fg="white",height=5, width=9, bg="grey", command=lambda: button_press(1))
button_one.grid(row=3, column=0)

button_two = Button(frame, text=2,fg="white", height=5, width=9, bg="grey", command=lambda: button_press(2))
button_two.grid(row=3, column=1)

button_three = Button(frame, text=3,fg="white", height=5, width=9, bg="grey", command=lambda: button_press(3))
button_three.grid(row=3, column=2)

button_four = Button(frame, text=4,fg="white", height=5, width=9, bg="grey", command=lambda: button_press(4))
button_four.grid(row=2, column=0)

button_five = Button(frame, text=5,fg="white", height=5, width=9, bg="grey", command=lambda: button_press(5))
button_five.grid(row=2, column=1)

button_six = Button(frame, text=6,fg="white", height=5, width=9, bg="grey", command=lambda: button_press(6))
button_six.grid(row=2, column=2)

button_seven = Button(frame, text=7,fg="white", height=5, width=9, bg="grey", command=lambda: button_press(7))
button_seven.grid(row=1, column=0)

button_eight = Button(frame, text=8,fg="white", height=5, width=9, bg="grey", command=lambda: button_press(8))
button_eight.grid(row=1, column=1)

button_nine = Button(frame, text=9,fg="white", height=5, width=9, bg="grey", command=lambda: button_press(9))
button_nine.grid(row=1, column=2)

button_zero = Button(frame, text=0,fg="white", height=5, width=9, bg="grey", command=lambda: button_press(0))
button_zero.grid(row=4, column=1)

button_plus = Button(frame, text='+',fg="black", height=5, width=9, bg="yellow", command=lambda: button_press("+"))
button_plus.grid(row=1, column=3)

button_minus = Button(frame, text='-',fg="black", height=5, width=9, bg="yellow", command=lambda: button_press('-'))
button_minus.grid(row=2, column=3)

button_multiply = Button(frame, text='*',fg="black", height=5, width=9, bg="yellow", command=lambda: button_press('*'))
button_multiply.grid(row=3, column=3)

button_divide = Button(frame, text='/',fg="black", height=5, width=9, bg="yellow", command=lambda: button_press('/'))
button_divide.grid(row=4, column=2)

button_equal = Button(frame, text='=',fg="white", height=5, width=9, bg="green", command=equal)
button_equal.grid(row=4, column=3)

button_dot = Button(frame, text='.',fg="black", height=5, width=9, bg="cyan", command=lambda: button_press('.'))
button_dot.grid(row=4, column=0)

button_clear = Button(root, text='Clear', height=4, width=10, bg="red", command=clear)
button_clear.pack()

root.mainloop()
