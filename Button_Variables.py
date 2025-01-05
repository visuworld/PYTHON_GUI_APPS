import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Buttons and Variables')
window.geometry('800x500')

# Button
def button_func():
    print("hELLO")

button_string = tk.StringVar(value='A Button with stringVar')
button = tk.Button(window, text='A Simple Button', command=button_func, textvariable=button_string)
button.pack()

# Checkbutton
check_var = tk.IntVar()
check1 = tk.Checkbutton(
    window, text='checkbox 1', 
    command=lambda:print(check_var.get()),
    variable=check_var,
    onvalue=10,
    offvalue=5)
check1.pack()

check2 = tk.Checkbutton(
    window, text='checkbox 2',
    command = lambda:print(check_var.get()),
    variable=check_var,
    onvalue=20,
    offvalue=21
)
check2.pack()

# Radio Button
radio_var = tk.StringVar()
radio1 = tk.Radiobutton(
    window,
    text='Radiobutton 1',
    value='1',
    variable=radio_var,
    command=lambda:print(radio_var.get()))
radio1.pack()

radio2 = tk.Radiobutton(text='Radionbutton 2', value=2, variable=radio_var)
radio2.pack()


#Run
window.mainloop()