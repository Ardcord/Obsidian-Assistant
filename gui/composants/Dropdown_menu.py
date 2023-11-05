import tkinter as tk

class TypeDropdown:
    def __init__(self, parent, choices):
        self.selected_type = tk.StringVar()
        
        self.label = tk.Label(parent, text="Type")
        self.label.pack(pady=10)

        self.menu = tk.OptionMenu(parent, self.selected_type, *choices)
        self.menu.pack()
