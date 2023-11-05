import tkinter as tk

class CTFOptions:
    def __init__(self, parent, disciplines):
        self.frame = tk.Frame(parent)

        # Label et entrée pour le nom du CTF
        self.name_label = tk.Label(self.frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10)
        self.ctf_name = tk.Entry(self.frame)
        self.ctf_name.grid(row=0, column=1)

        # Checkbuttons pour les disciplines
        self.discipline_vars = []
        for i, discipline in enumerate(disciplines):
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self.frame, text=discipline, variable=var)
            checkbox.grid(row=i + 1, column=0, columnspan=2, padx=10, sticky="w")
            self.discipline_vars.append(var)

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)
