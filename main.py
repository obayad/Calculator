import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("720x480")

def button_press(num):
    global equation_text

    equation_text += str(num)
    equation_label.set(equation_text)

def button_equal():
    pass

def button_clear():
    global equation_text
    equation_text =""
    equation_label.set(equation_text)

equation_text = ""
equation_label = tk.StringVar()


label = tk.Label(root, textvariable=equation_label,font=("Arial",20), width=50,  height=2, bg="white")
label.pack()


buttonFrame = tk.Frame(root)

buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

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
btn0.grid(row=3, column=1, sticky=tk.W+tk.E, padx=4,pady=4)

btnob = tk.Button(buttonFrame, text="(",font=("Arial",14), command=lambda:button_press("("))
btnob.grid(row=3, column=0, sticky=tk.W+tk.E, padx=4,pady=4)
btncb = tk.Button(buttonFrame, text=")",font=("Arial",14), command=lambda:button_press(")"))
btncb.grid(row=3, column=2, sticky=tk.W+tk.E, padx=4,pady=4)

btnclear = tk.Button(root, text="clear", font=("Arial",16), command=button_clear)
btnclear.pack()

buttonFrame.pack(fill="both",padx=20, pady=20)

root.mainloop()