import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("720x480")

label = tk.Label(root, text="Calculator", font=("Arial", 20))
label.pack(padx=10, pady=10)

textbox = tk.Text(root, font=("Arial", 14), height=2)
textbox.pack(padx=20, pady=20)

buttonFrame = tk.Frame(root)

buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonFrame, text="7",font=("Arial", 14))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E,padx=4,pady=4)
btn2 = tk.Button(buttonFrame, text="8", font=("Arial", 14))
btn2.grid(row=0, column=1 , sticky=tk.W+tk.E, padx=4,pady=4)
btn3 = tk.Button(buttonFrame, text="9",font=("Arial", 14))
btn3.grid(row=0, column=2 , sticky=tk.W+tk.E, padx=4,pady=4)
btn4 = tk.Button(buttonFrame, text="4", font=("Arial", 14))
btn4.grid(row=1, column=0 , sticky=tk.W+tk.E, padx=4,pady=4)
btn5 = tk.Button(buttonFrame, text="5", font=("Arial", 14))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E, padx=4,pady=4)
btn6 = tk.Button(buttonFrame, text="6", font=("Arial", 14))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E, padx=4,pady=4)
btn7 = tk.Button(buttonFrame, text="1", font=("Arial", 14))
btn7.grid(row=2, column=0, sticky=tk.W+tk.E, padx=4,pady=4)
btn8 = tk.Button(buttonFrame, text="2", font=("Arial", 14))
btn8.grid(row=2, column=1, sticky=tk.W+tk.E, padx=4,pady=4)
btn9 = tk.Button(buttonFrame, text="3", font=("Arial", 14))
btn9.grid(row=2, column=2, sticky=tk.W+tk.E, padx=4,pady=4)
btn0 = tk.Button(buttonFrame, text="0",font=("Arial", 14))
btn0.grid(row=3, column=1, sticky=tk.W+tk.E, padx=4,pady=4)

btnob = tk.Button(buttonFrame, text="(",font=("Arial",14))
btnob.grid(row=3, column=0, sticky=tk.W+tk.E, padx=4,pady=4)
btncb = tk.Button(buttonFrame, text=")",font=("Arial",14))
btncb.grid(row=3, column=2, sticky=tk.W+tk.E, padx=4,pady=4)

buttonFrame.pack(fill="both",padx=20, pady=20)

root.mainloop()