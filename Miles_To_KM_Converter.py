import tkinter as tk
import ttkbootstrap 
from tkinter import ttk

def convert():
    mill_input = entry_int.get()
    km_output = mill_input * 1.61
    output_string.set(km_output)

# window
window = tk.Tk()
window.title("Demo")
window.geometry("300x150")

# title
title_label = ttk.Label(master = window, text = 'Miles To Kilometers', font='calibri 24 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text="Convert", command = convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady = 10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text='Output', font='calibri 24', textvariable = output_string)
output_label.pack()
# run
window.mainloop()