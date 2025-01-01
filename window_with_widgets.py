import tkinter as tk
from tkinter import ttk

def button_func():
    print('a button was pressed')

def hlo_func():
    print('Hello')

# Create a Window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')
# ttk Lable
label = ttk.Label(master = window, text='This is a text')
label.pack()

# tk.text
tk.Text(master = window).pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# My label
my_label = ttk.Label(master = window, text='My Label')
my_label.pack()

# hello Button
# helo_btn = ttk.Button(master = window, text='clk to helo', command= hlo_func)
helo_btn = ttk.Button(master = window, text='clk to helo', command= lambda : print('Hello'))
helo_btn.pack()

# ttk button
button = ttk.Button(master = window, text='A button', command= button_func)
button.pack()


# Run
window.mainloop()