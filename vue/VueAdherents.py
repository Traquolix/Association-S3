import tkinter as tk
from tkinter import *


class VueAdherents(tk.Frame):
    def __init__(self, parent, controleur):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="page gestion des adhérents")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="accueil", command=lambda: controleur.show_frame("Accueil"))
        button1.pack()
