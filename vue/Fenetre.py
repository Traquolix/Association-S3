import tkinter as tk
from tkinter import *
from tkinter import ttk

# Cette classe est la fenêtre de l'application qui permet de gérer les différentes pages
from Controleurs.ControleurAdherents import ControleurAdherents
from data import StockageAdherentCsv


class Fenetre:

    def __init__(self):

        self.container = Tk() # Création de la fenetre
        self.container.title('application gestion trésorerie')
        self.container.geometry("1000x500")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        """ self.frames = {}

        page_name = Accueil.__name__
        frame = Accueil(parent=self.container, controleur=self)
        self.frames[page_name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        page_name = VueAdherents.__name__
        frame = VueAdherents(parent=self.container, controleur=self)
        self.frames[page_name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Accueil") """

        """tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Gestion trésorerie ATALA")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)  """

        #self.controllerAdherent = ControleurAdherents()

        self.frames = {}

        for F in (Accueil, VueAdherents, VueFacture):

            #if F == Accueil :
             #   frame = F(self.container, )
            #else :
            frame = F(self.container, self)

            self.frames[F] = frame

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

        logoImg = tk.PhotoImage(file='vue/atala_logo.png')
        logo = tk.Label(top_bar, image=logoImg)
        logo.config(bg="skyblue")
        logo.photo = logoImg
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

        logoBtn1 = tk.PhotoImage(file='vue/adherents.png')
        button1 = ttk.Button(left_frame, text="gérer adhérents", image=logoBtn1, style='my.TButton', compound="left", command=lambda: controleur.show_frame(VueAdherents))
        button1.photo = logoBtn1
        button1.place(relx=0.5, rely=0.5, anchor=CENTER)

        logoBtn2 = tk.PhotoImage(file='vue/facture.png')
        button2 = ttk.Button(mid_frame, text="générer facture", image=logoBtn2, style='my.TButton', compound="left", command=lambda: controleur.show_frame(VueFacture))
        button2.photo = logoBtn2
        button2.place(relx=0.5, rely=0.5, anchor=CENTER)

        logoBtn3 = tk.PhotoImage(file='vue/boncommande.png')
        button3 = ttk.Button(right_frame, text="générer bon de \ncommande", image=logoBtn3, style='my.TButton', compound="left", command=lambda: controleur.show_frame(VueAdherents))
        button3.photo = logoBtn3
        button3.place(relx=0.5, rely=0.5, anchor=CENTER)


class VueAdherents(tk.Frame):

    def __init__(self, parent, controleur):
        tk.Frame.__init__(self, parent)
        self.config(bg="skyblue")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        top_bar = tk.Frame(self)
        top_bar.config(bg="skyblue")
        top_bar.rowconfigure(0, weight=1)
        top_bar.columnconfigure(0, weight=1)
        top_bar.columnconfigure(1, weight=1)
        top_bar.columnconfigure(2, weight=1)
        top_bar.grid(row=0, column=0, columnspan=3, sticky="nsew")

        titre = tk.Label(self, text="Gestion des adhérents")
        titre.config(font=("Courier", 20), bg="skyblue")
        titre.grid(row=0, column=1, sticky='nsew')

        conteneur_bouton_accueil = tk.Frame(self)
        conteneur_bouton_accueil.config(bg="skyblue")
        conteneur_bouton_accueil.rowconfigure(0, weight=1)
        conteneur_bouton_accueil.columnconfigure(0, weight=1)
        conteneur_bouton_accueil.grid(row=0, column=0, sticky="nsew")

        logo_btn_accueil = tk.PhotoImage(file='vue/accueil.png')
        accueil = ttk.Button(conteneur_bouton_accueil, text="accueil", image=logo_btn_accueil, style='my.TButton', compound="left", command=lambda: controleur.show_frame(Accueil))
        accueil.photo = logo_btn_accueil
        accueil.place(relx=0.5, rely=0.5, anchor=CENTER)

        left_frame = Frame(self)
        left_frame.config(bg='skyblue')
        left_frame.columnconfigure(0, weight=1)
        left_frame.rowconfigure(0, weight=1)
        left_frame.rowconfigure(1, weight=1)
        left_frame.rowconfigure(2, weight=1)
        left_frame.grid(row=1, column=0, sticky="nsew")

        formulaire = Frame(left_frame)
        formulaire.config(bg='skyblue')
        formulaire.columnconfigure(0, weight=1)
        formulaire.rowconfigure(0, weight=1)
        formulaire.rowconfigure(1, weight=1)
        formulaire.rowconfigure(2, weight=1)
        formulaire.rowconfigure(3, weight=1)
        formulaire.grid(row=1, column=1, sticky="nsew")

        conteneur_nom = Frame(formulaire)
        conteneur_nom.config(bg='skyblue')
        conteneur_nom.columnconfigure(0, weight=1)
        conteneur_nom.columnconfigure(1, weight=1)
        conteneur_nom.rowconfigure(0, weight=1)
        conteneur_nom.grid(row=0, column=0, sticky="nsew")

        lnom = Label(conteneur_nom, text="nom :")
        lnom.config(bg='skyblue')
        lnom.grid(row=0, column=0, padx=(0, 15))
        nom = Entry(conteneur_nom, textvariable="nom", width=20)
        nom.grid(row=0, column=1)

        conteneur_prenom = Frame(formulaire)
        conteneur_prenom.config(bg='skyblue')
        conteneur_prenom.columnconfigure(0, weight=1)
        conteneur_prenom.columnconfigure(1, weight=1)
        conteneur_prenom.rowconfigure(0, weight=1)
        conteneur_prenom.grid(row=1, column=0, sticky="nsew")

        lprenom = Label(conteneur_prenom, text="prénom :")
        lprenom.config(bg='skyblue')
        lprenom.grid(row=0, column=0, padx=(0, 15))
        prenom = Entry(conteneur_prenom, textvariable="prénom", width=20)
        prenom.grid(row=0, column=1)

        conteneur_labo = Frame(formulaire)
        conteneur_labo.config(bg='skyblue')
        conteneur_labo.columnconfigure(0, weight=1)
        conteneur_labo.columnconfigure(1, weight=1)
        conteneur_labo.rowconfigure(0, weight=1)
        conteneur_labo.grid(row=2, column=0, sticky="nsew")

        llabo = Label(conteneur_labo, text="laboratoire :")
        llabo.config(bg='skyblue')
        llabo.grid(row=0, column=0, padx=(0, 15))
        labo = Entry(conteneur_labo, textvariable="labo", width=20)
        labo.grid(row=0, column=1)

        ajouter = ttk.Button(formulaire, text="ajouter adhérent", style='my.TButton')
        ajouter.grid(row=3, column=0)

        mid_frame = Frame(self)
        mid_frame.config(bg='skyblue')
        mid_frame.rowconfigure(0, weight=1)
        mid_frame.rowconfigure(1, weight=1)
        mid_frame.columnconfigure(0, weight=1)
        mid_frame.grid(row=1, column=1, sticky="nsew")

        self.adherents = tk.Listbox(mid_frame, width=60)
        self.initialiserListe()
        self.adherents.grid(row=0, column=0)

        supprimer = ttk.Button(mid_frame, text="supprimer adhérent", style='my.TButton')
        supprimer.grid(row=1, column=0)

    def initialiserListe(self):
        adh = StockageAdherentCsv.StockageAdherentCsv()
        a = adh.lirefichier()
        cpt=1
        for adhe in a :
            self.adherents.insert(cpt,adhe)

        """
      


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

        label = tk.Label(self, text="page gestion des adhérents")
        label.pack(side="top", fill="x", pady=10)

        button1 = ttk.Button(self, text="accueil", command=lambda: controleur.show_frame(Accueil))
      
        button1.pack()"""


class VueFacture(tk.Frame):
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
