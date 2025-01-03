# Tkinter has inbiult variables that are design to work with widgets.
# They are automatically update by a widget and they update a widgets

import tkinter as tk
from tkinter import ttk

def button_func():
    string_var.set('Button pressed')
    
def exercise_func():
    exercise_str_var.set('Test')




# window
window = tk.Tk()
window.title('Tkinter Variable')
window.geometry('800x400')

# Tkinter variable
string_var = tk.StringVar()
exercise_str_var = tk.StringVar()

# widgets
label  = ttk.Label(master = window, text='Label', textvariable= string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

button = tk.Button(master = window,text='Button', command= button_func)
button.pack()

# Exercise

exercise_label = tk.Label(master = window, text='Exercise Label', textvariable=exercise_str_var)
exercise_label.pack()

excercise_entry1 = tk.Entry(master = window, textvariable=exercise_str_var)
excercise_entry1.pack()

excercise_entry2 = tk.Entry(master = window, textvariable=exercise_str_var )
excercise_entry2.pack()

excercise_button = tk.Button(master = window, text='Exercise Button', command=exercise_func)
excercise_button.pack()


# Run
window.mainloop()