import tkinter as tk
from tkinter import *
from tkinter import ttk


class Fenetre:

    def __init__(self):

        self.container = Tk() # Création de la fenetre
        self.container.title('application gestion trésorerie')
        self.container.geometry("1000x500")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}


        frame = Accueil(self.container, self)

        self.frames[Accueil] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Accueil)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def demarrerApplication(self):
        self.container.mainloop()


class Accueil(tk.Frame):

    def __init__(self, parent, controleur):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        top_bar = tk.Frame(self, width=300, height=70)
        top_bar.config(bg="skyblue")
        top_bar.rowconfigure(0, weight=1)
        top_bar.columnconfigure(0, weight=1)
        top_bar.columnconfigure(1, weight=1)
        top_bar.columnconfigure(2, weight=1)
        top_bar.grid(row=0, column=0, columnspan=3, sticky="nsew")

        logo = tk.Label(top_bar)
        logo.config(bg="skyblue")
        logo.grid(row=0, column=0)

        conteneurTitre = tk.Frame(top_bar)
        conteneurTitre.config(bg="skyblue")
        conteneurTitre.rowconfigure(0,weight=1)
        conteneurTitre.columnconfigure(0, weight=1)
        conteneurTitre.grid(row=0, column=1, columnspan=2, sticky="nsew")

        titre = tk.Label(conteneurTitre, text="Opérations de gestion de \nla trésorerie d'ATALA")
        titre.config(font=("Courier", 20), bg="skyblue")
        titre.grid(row=0, column=0, sticky='w')

        bottom_bar = tk.Frame(self, width=300, height=70)
        bottom_bar.config(bg="skyblue")
        bottom_bar.grid(row=2, column=0, columnspan=3, sticky="nsew")

        left_frame = Frame(self, width=333, height=100)
        left_frame.config(bg='skyblue')
        left_frame.grid(row=1, column=0, sticky="nsew")
        mid_frame = Frame(self, width=333, height=100)
        mid_frame.config(bg='skyblue')
        mid_frame.grid(row=1, column=1, sticky="nsew")
        right_frame = Frame(self, width=333, height=100)
        right_frame.config(bg='skyblue')
        right_frame.grid(row=1, column=2, sticky="nsew")

        s = ttk.Style()
        s.configure('my.TButton', font=('Courier', 12), borderwidth=0)

        button1 = ttk.Button(left_frame, text="gérer adhérents", style='my.TButton', compound="left", command=lambda: controleur.show_frame(VueAdherents))
        button1.place(relx=0.5, rely=0.5, anchor=CENTER)

        button2 = ttk.Button(mid_frame, text="générer facture", style='my.TButton', compound="left", command=lambda: controleur.show_frame(VueFacture))
        button2.place(relx=0.5, rely=0.5, anchor=CENTER)

        button3 = ttk.Button(right_frame, text="générer bon de \ncommande", style='my.TButton', compound="left", command=lambda: controleur.show_frame(VueAdherents))
        button3.place(relx=0.5, rely=0.5, anchor=CENTER)


app = Fenetre()
app.demarrerApplication()
