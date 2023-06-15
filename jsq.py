from tkinter import *
import math

# 创建窗口
root = Tk()
root.title("计算器")

# 创建显示框
display = Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# 定义按钮点击事件
def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))

def button_clear():
    display.delete(0, END)

def button_add():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = float(first_number)
    display.delete(0, END)

def button_subtract():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = float(first_number)
    display.delete(0, END)

def button_multiply():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = float(first_number)
    display.delete(0, END)

def button_divide():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = float(first_number)
    display.delete(0, END)

def button_equal():
    second_number = display.get()
    display.delete(0, END)

    if math_operation == "addition":
        display.insert(0, f_num + float(second_number))

    if math_operation == "subtraction":
        display.insert(0, f_num - float(second_number))

    if math_operation == "multiplication":
        display.insert(0, f_num * float(second_number))

    if math_operation == "division":
        display.insert(0, f_num / float(second_number))

def button_square():
    first_number = display.get()
    display.delete(0, END)
    display.insert(0, float(first_number) ** 2)

def button_sqrt():
    first_number = display.get()
    display.delete(0, END)
    display.insert(0, math.sqrt(float(first_number)))

# 创建按钮
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)
button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)
button_clear = Button(root, text="C", padx=40, pady=20, command=button_clear)
button_square = Button(root, text="平方", padx=40, pady=20, command=button_square)
button_sqrt = Button(root, text="开方", padx=40, pady=20, command=button_sqrt)

# 将按钮放置在窗口上
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=5, column=1)
button_equal.grid(row=4, column=2)
button_square.grid(row=5, column=2)
button_sqrt.grid(row=6, column=2)

# 运行窗口
root.mainloop()
