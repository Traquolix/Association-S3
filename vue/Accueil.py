import tkinter as tk
from tkinter import *

from vue.VueAdherents import VueAdherents


class Accueil(tk.Frame):
    def __init__(self, parent, controleur):
        tk.Frame.__init__(self, parent)
        self.config(bg="red")

        label = tk.Label(self, text="page d'accueil")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="gérer adhérents", command=lambda: controleur.show_frame("VueAdherents"))
        button1.pack()
