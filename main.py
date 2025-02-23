import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("500x400")
root.configure(background="Black")

#change icon
icon = tk.PhotoImage(file="icon.png")
root.iconphoto(False, icon)

def button_press(num):
    global equation_text

    equation_text += str(num)
    equation_label.set(equation_text)

def button_equal():
    global equation_text

    try:
        if "^" in equation_text:
            equation_text=equation_text.replace("^", "**")
            total = str(eval(equation_text))
            equation_label.set(total)
        else:
            total = str(eval(equation_text))
            equation_label.set(total)

    except SyntaxError:
        equation_label.set("Syntax Error! 😔")

    except ZeroDivisionError:
        equation_label.set("❌ Error!")
    equation_text = total

def button_clear():
    global equation_text
    equation_text =""
    equation_label.set(equation_text)

equation_text = ""
equation_label = tk.StringVar()


label = tk.Label(root, textvariable=equation_label,font=("Arial",20), width=50,  height=2, bg="white")
label.pack()


buttonFrame = tk.Frame(root, bg="Black")

buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)

btn1 = tk.Button(buttonFrame, text="7",font=("Arial", 14),command=lambda:button_press(7))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E,padx=4,pady=4)
btn2 = tk.Button(buttonFrame, text="8", font=("Arial", 14), command=lambda:button_press(8))
btn2.grid(row=0, column=1 , sticky=tk.W+tk.E, padx=4,pady=4)
btn3 = tk.Button(buttonFrame, text="9",font=("Arial", 14), command=lambda:button_press(9))
btn3.grid(row=0, column=2 , sticky=tk.W+tk.E, padx=4,pady=4)
btn4 = tk.Button(buttonFrame, text="4", font=("Arial", 14), command=lambda:button_press(4))
btn4.grid(row=1, column=0 , sticky=tk.W+tk.E, padx=4,pady=4)
btn5 = tk.Button(buttonFrame, text="5", font=("Arial", 14), command=lambda:button_press(5))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E, padx=4,pady=4)
btn6 = tk.Button(buttonFrame, text="6", font=("Arial", 14), command=lambda:button_press(6))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E, padx=4,pady=4)
btn7 = tk.Button(buttonFrame, text="1", font=("Arial", 14), command=lambda:button_press(1))
btn7.grid(row=2, column=0, sticky=tk.W+tk.E, padx=4,pady=4)
btn8 = tk.Button(buttonFrame, text="2", font=("Arial", 14), command=lambda:button_press(2))
btn8.grid(row=2, column=1, sticky=tk.W+tk.E, padx=4,pady=4)
btn9 = tk.Button(buttonFrame, text="3", font=("Arial", 14), command=lambda:button_press(3))
btn9.grid(row=2, column=2, sticky=tk.W+tk.E, padx=4,pady=4)
btn0 = tk.Button(buttonFrame, text="0",font=("Arial", 14), command=lambda:button_press(0))
btn0.grid(row=3, column=0, sticky=tk.W+tk.E, padx=4,pady=4)

btn_point = tk.Button(buttonFrame, text=".", font=("Arial",14), command=lambda:button_press("."))
btn_point.grid(row=3, column=1, sticky="nsew", padx=4, pady=4)

btn_equal = tk.Button(buttonFrame, text="=", font=("Arial",14), fg="white", bg="Green", command=button_equal)
btn_equal.grid(row=4, column=2, sticky="nsew", padx=4, pady=4)

btn_sum = tk.Button(buttonFrame, text="+", font=("Arial",14), fg="white", bg="Green", command=lambda:button_press("+"))
btn_sum.grid(row=3, column="3", sticky="nsew", padx=4, pady=4)
btn_sub = tk.Button(buttonFrame, text="-", font=("Arial",14), fg="white", bg="Green", command=lambda:button_press("-"))
btn_sub.grid(row=2, column="3", sticky="nsew", padx=4, pady=4)
btn_mul = tk.Button(buttonFrame, text="*", font=("Arial",14), fg="white", bg="Green", command=lambda:button_press("*"))
btn_mul.grid(row=1, column="3", sticky="nsew", padx=4, pady=4)
btn_div = tk.Button(buttonFrame, text="/", font=("Arial",14), fg="white", bg="Green", command=lambda:button_press("/"))
btn_div.grid(row=0, column="3", sticky="nsew", padx=4, pady=4)

btn_power = tk.Button(buttonFrame, text="^", font=("Arial",14), command=lambda:button_press("^"))
btn_power.grid(row=3, column="2", sticky="nsew", padx=4, pady=4)

btnob = tk.Button(buttonFrame, text="(",font=("Arial",14), fg="white", bg="Green", command=lambda:button_press("("))
btnob.grid(row=4, column=0, sticky=tk.W+tk.E, padx=4,pady=4)
btncb = tk.Button(buttonFrame, text=")",font=("Arial",14), fg="white", bg="Green", command=lambda:button_press(")"))
btncb.grid(row=4, column=1, sticky=tk.W+tk.E, padx=4,pady=4)

btnclear = tk.Button(buttonFrame, text="clear", font=("Arial",16), fg="white", bg="Red", command=button_clear)
btnclear.grid(row=4,column=3, sticky="nsew", padx=4, pady=4)

buttonFrame.pack(fill="both",padx=20, pady=20)

root.mainloop()