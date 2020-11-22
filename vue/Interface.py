from tkinter import *


class Interface:

    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.title("gestion trésorerie")
        self.fenetre.geometry("1000x700")

    def demarrerAppli(self):
        self.fenetre.mainloop()

    def vueGestionadherents(self):
        champ_label = Label(self.fenetre, text="Gestion Adhérents")
        champ_label.pack()