import tkinter as tk
from tkinter import *

from vue.Accueil import Accueil
from vue.VueAdherents import VueAdherents

# Cette classe est la fenêtre de l'application qui permet de gérer les différentes pages


class Fenetre:

    def __init__(self):

        self.container = Tk() # Création de la fenetre
        self.container.title('application gestion trésorerie')
        self.container.geometry("1000x500")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        page_name = Accueil.__name__
        frame = Accueil(parent=self.container, controleur=self)
        self.frames[page_name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        page_name = VueAdherents.__name__
        frame = VueAdherents(parent=self.container, controleur=self)
        self.frames[page_name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Accueil")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def demarrerApplication(self):
        self.container.mainloop()
