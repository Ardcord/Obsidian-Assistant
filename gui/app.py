import tkinter as tk
from tkinter import ttk
from gui.composants.ctf_options import CTFOptions

class MyApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Obsidian Assistant")
        self.root.geometry("800x650")

        # Créez un cadre pour les boutons et options
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Bouton pour "CTF"
        self.ctf_button = tk.Button(self.frame, text="CTF", width=10, height=2, command=self.show_ctf_options)
        self.ctf_button.grid(row=0, column=1, padx=(0, 10))

        # Bouton pour "BOX"
        self.box_button = tk.Button(self.frame, text="BOX", width=10, height=2, command=self.show_box_options)
        self.box_button.grid(row=0, column=0, padx=(10, 0))

        # Frame pour les options CTF (initiallement masquées)
        self.ctf_frame = CTFOptions(self.frame, ["Crypto", "Stegano", "Forensic", "Pwn", "Reverse", "Web", "Web3", "Misc", "Network"])

        # Bouton "Retour" pour les options CTF
        self.ctf_return_button = tk.Button(self.ctf_frame.frame, text="Retour", command=self.hide_ctf_options)
        self.style_red_button(self.ctf_return_button)

        # Frame pour les options BOX (initiallement masquées)
        self.box_frame = tk.Frame(self.frame)
        self.box_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.box_return_button = tk.Button(self.box_frame, text="Retour", command=self.hide_box_options)
        self.style_red_button(self.box_return_button)

        # Masquer initialement les options CTF et BOX
        self.hide_ctf_options()
        self.hide_box_options()

    def style_red_button(self, button):
        # Appliquer un style au bouton pour le rendre rouge
        button.configure(bg="red", fg="white", width=10, height=2)

    def show_ctf_options(self):
        # Afficher les options CTF et masquer les boutons BOX et CTF
        self.ctf_button.grid_forget()
        self.box_button.grid_forget()
        self.ctf_frame.frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.ctf_return_button.grid(row=2, column=0, columnspan=2, pady=10)

    def show_box_options(self):
        # Afficher les options BOX et masquer les boutons BOX et CTF
        self.ctf_button.grid_forget()
        self.box_button.grid_forget()
        self.box_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.box_return_button.grid(row=2, column=0, columnspan=2, pady=10)

    def hide_ctf_options(self):
        # Masquer les options CTF et afficher les boutons CTF et BOX
        self.ctf_frame.frame.grid_forget()
        self.ctf_button.grid(row=0, column=1, padx=(0, 10))
        self.box_button.grid(row=0, column=0, padx=(10, 0))
        self.ctf_return_button.grid_forget()

    def hide_box_options(self):
        # Masquer les options BOX et afficher les boutons CTF et BOX
        self.box_frame.grid_forget()
        self.ctf_button.grid(row=0, column=1, padx=(0, 10))
        self.box_button.grid(row=0, column=0, padx=(10, 0))
        self.box_return_button.grid_forget()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MyApp()
    app.run()
