import tkinter as tk
from tkinter import ttk

def button_func():
    # get the content of the entry
    entry_text = entry.get()

    # Update the label
    # label.configure(text='some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled'

# Window
window = tk.Tk()
window.title('Getting and setting widgets')
window.geometry('800x400')

# widgets

label = ttk.Label(master = window, text='Some Text on Label')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button( master = window, text='Button', command= button_func)
button.pack()


def reset_func():
    label['text'] = 'Some text'
    entry['state'] = 'enabled'

# excercise Button
exercise_button = ttk.Button(master = window, text='Exercise Button', command=reset_func)
exercise_button.pack()
 
# Run
window.mainloop()