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

        self.frames = {}

        self.ctrlAdherent = ControleurAdherents(self)

        for F in (Accueil, VueAdherents, VueFacture):

            if F == VueAdherents:
                frame = F(self.container, ctrlFenetre=self, ctrlAdherent=self.ctrlAdherent)
            else:
                frame = F(self.container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Accueil)

        self.ctrlAdherent.setVue(self.get_frame_VueAdherent())

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_frame_Accueil(self):
        return self.frames[Accueil]

    def get_frame_VueAdherent(self):
        return self.frames[VueAdherents]

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

    def __init__(self, parent, ctrlFenetre, ctrlAdherent):
        tk.Frame.__init__(self, parent)
        self.config(bg="skyblue")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.ctrlAdherent = ctrlAdherent

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
        accueil = ttk.Button(conteneur_bouton_accueil, text="accueil", image=logo_btn_accueil, style='my.TButton', compound="left", command=lambda: ctrlFenetre.show_frame(Accueil))
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
        self.str_nom = tk.StringVar()
        self.str_nom.set("")
        self.nom = Entry(conteneur_nom, textvariable=self.str_nom, width=20)
        self.nom.grid(row=0, column=1)

        conteneur_prenom = Frame(formulaire)
        conteneur_prenom.config(bg='skyblue')
        conteneur_prenom.columnconfigure(0, weight=1)
        conteneur_prenom.columnconfigure(1, weight=1)
        conteneur_prenom.rowconfigure(0, weight=1)
        conteneur_prenom.grid(row=1, column=0, sticky="nsew")

        lprenom = Label(conteneur_prenom, text="prénom :")
        lprenom.config(bg='skyblue')
        lprenom.grid(row=0, column=0, padx=(0, 15))
        self.str_prenom = tk.StringVar()
        self.str_prenom.set("")
        self.prenom = Entry(conteneur_prenom, textvariable=self.str_prenom, width=20)
        self.prenom.grid(row=0, column=1)

        conteneur_labo = Frame(formulaire)
        conteneur_labo.config(bg='skyblue')
        conteneur_labo.columnconfigure(0, weight=1)
        conteneur_labo.columnconfigure(1, weight=1)
        conteneur_labo.rowconfigure(0, weight=1)
        conteneur_labo.grid(row=2, column=0, sticky="nsew")

        llabo = Label(conteneur_labo, text="laboratoire :")
        llabo.config(bg='skyblue')
        llabo.grid(row=0, column=0, padx=(0, 15))
        self.labo = tk.Listbox(conteneur_labo, width=10, height=2)
        self.actualiser_liste_labo()
        self.labo.grid(row=0, column=1)

        ajouter = ttk.Button(formulaire, text="ajouter adhérent", style='my.TButton', command=lambda: ctrlAdherent.ajouterAdherent())
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

        supprimer = ttk.Button(mid_frame, text="supprimer adhérent", style='my.TButton', command=lambda: ctrlAdherent.supprimerAdherent())
        supprimer.grid(row=1, column=0)

        bottom_bar = tk.Frame(self)
        bottom_bar.config(bg="skyblue")
        bottom_bar.rowconfigure(0, weight=1)
        bottom_bar.columnconfigure(0, weight=1)
        bottom_bar.columnconfigure(1, weight=1)
        bottom_bar.columnconfigure(2, weight=1)
        bottom_bar.grid(row=2, column=0, columnspan=3, sticky="nsew")

        conteneur_gerer_labo = tk.Frame(bottom_bar)
        conteneur_gerer_labo.config(bg="skyblue")
        conteneur_gerer_labo.rowconfigure(0, weight=1)
        conteneur_gerer_labo.columnconfigure(0, weight=1)
        conteneur_gerer_labo.grid(row=0, column=0, columnspan=1, sticky="nsew")
        gerer_labo = ttk.Button(conteneur_gerer_labo, text="gérer laboratoires", style='my.TButton', command=lambda : self.fenetre_labo(parent))
        gerer_labo.grid(row=0, column=0)

    def fenetre_labo(self, parent):
        top = Toplevel(parent)
        top.mainloop()

    def initialiserListe(self):
        self.adherents.delete(0, END)
        liste = self.ctrlAdherent.actualiser_liste_adherents()
        cpt = 1
        for ad in liste:
            self.adherents.insert(cpt, ad)
        self.adherents.select_set(0)

    def actualiser_liste_labo(self):
        self.labo.delete(0, END)
        liste = self.ctrlAdherent.actualiser_liste_laboratoire()
        cpt = 1
        for ad in liste:
            self.labo.insert(cpt, ad)
        self.labo.select_set(0)

    def getPrenom(self):
        return self.prenom.get()

    def getNom(self):
        return self.nom.get()

    def getLabo(self):
        return self.labo.get(self.labo.curselection())

    def viderChamps(self):
        self.str_prenom.set("")
        self.str_nom.set("")
        self.labo.select_set(0)

    def listBoxEstVide(self):
        return self.adherents.size() == 0

    def getSelectedAdherent(self):
        return self.adherents.get(self.adherents.curselection())


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
    def __init__(self, parent, ctrl_fenetre):
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

        titre = tk.Label(self, text="Generation Facture")
        titre.config(font=("Courier", 20), bg="skyblue")
        titre.grid(row=0, column=1, sticky='nsew')

        conteneur_bouton_accueil = tk.Frame(self)
        conteneur_bouton_accueil.config(bg="skyblue")
        conteneur_bouton_accueil.rowconfigure(0, weight=1)
        conteneur_bouton_accueil.columnconfigure(0, weight=1)
        conteneur_bouton_accueil.grid(row=0, column=0, sticky="nsew")

        logo_btn_accueil = tk.PhotoImage(file='vue/accueil.png')
        accueil = ttk.Button(conteneur_bouton_accueil, text="accueil", image=logo_btn_accueil, style='my.TButton',
                             compound="left", command=lambda: ctrl_fenetre.show_frame(Accueil))
        accueil.photo = logo_btn_accueil
        accueil.place(relx=0.5, rely=0.5, anchor=CENTER)

        left_frame = Frame(self)
        left_frame.config(bg='skyblue')
        left_frame.columnconfigure(0, weight=1)
        left_frame.rowconfigure(0, weight=1)
        left_frame.rowconfigure(1, weight=1)
        left_frame.rowconfigure(2, weight=1)
        left_frame.grid(row=1, column=0, sticky="nsew")

        formulaire_gauche = Frame(left_frame)
        formulaire_gauche.config(bg='skyblue')
        formulaire_gauche.columnconfigure(0, weight=1)
        formulaire_gauche.rowconfigure(0, weight=1)
        formulaire_gauche.rowconfigure(1, weight=1)
        formulaire_gauche.rowconfigure(2, weight=1)
        formulaire_gauche.rowconfigure(3, weight=1)
        formulaire_gauche.grid(row=1, column=1, sticky="nsew")

        conteneur_numf = Frame(formulaire_gauche)
        conteneur_numf.config(bg='skyblue')
        conteneur_numf.columnconfigure(0, weight=1)
        conteneur_numf.columnconfigure(1, weight=1)
        conteneur_numf.rowconfigure(0, weight=1)
        conteneur_numf.grid(row=0, column=0, sticky="nsew")

        lnum = Label(conteneur_numf, text="numéro de facture :")
        lnum.config(bg='skyblue')
        lnum.grid(row=0, column=0, padx=(0, 15))
        self.str_num = tk.StringVar()
        self.str_num.set("")
        self.num = Entry(conteneur_numf, textvariable=self.str_num, width=20)
        self.num.grid(row=0, column=1)

        conteneur_montant = Frame(formulaire_gauche)
        conteneur_montant.config(bg='skyblue')
        conteneur_montant.columnconfigure(0, weight=1)
        conteneur_montant.columnconfigure(1, weight=1)
        conteneur_montant.rowconfigure(0, weight=1)
        conteneur_montant.grid(row=1, column=0, sticky="nsew")

        lmontant = Label(conteneur_montant, text="montant :")
        lmontant.config(bg='skyblue')
        lmontant.grid(row=0, column=0, padx=(0, 15))
        self.str_montant = tk.StringVar()
        self.str_montant.set("")
        self.num = Entry(conteneur_montant, textvariable=self.str_num, width=20)
        self.num.grid(row=0, column=1)

        conteneur_numb = Frame(formulaire_gauche)
        conteneur_numb.config(bg='skyblue')
        conteneur_numb.columnconfigure(0, weight=1)
        conteneur_numb.columnconfigure(1, weight=1)
        conteneur_numb.rowconfigure(0, weight=1)
        conteneur_numb.grid(row=2, column=0, sticky="nsew")

        lnumb = Label(conteneur_numb, text="numéro bon de commande : ")
        lnumb.config(bg='skyblue')
        lnumb.grid(row=0, column=0, padx=(0, 15))
        self.str_montant = tk.StringVar()
        self.str_montant.set("")
        self.num = Entry(conteneur_numb, textvariable=self.str_num, width=20)
        self.num.grid(row=0, column=1)

        mid_frame = Frame(self)
        mid_frame.config(bg='skyblue')
        mid_frame.columnconfigure(0, weight=1)
        mid_frame.rowconfigure(0, weight=1)
        mid_frame.rowconfigure(1, weight=1)
        mid_frame.rowconfigure(2, weight=1)
        mid_frame.grid(row=1, column=1, sticky="nsew")

        formulaire_droit = Frame(mid_frame)
        formulaire_droit.config(bg='skyblue')
        formulaire_droit.columnconfigure(0, weight=1)
        formulaire_droit.rowconfigure(0, weight=1)
        formulaire_droit.rowconfigure(1, weight=1)
        formulaire_droit.rowconfigure(2, weight=1)
        formulaire_droit.rowconfigure(3, weight=1)
        formulaire_droit.grid(row=1, column=3, sticky="nsew")

        conteneur_nbadherents = Frame(formulaire_droit)
        conteneur_nbadherents.config(bg='skyblue')
        conteneur_nbadherents.columnconfigure(0, weight=1)
        conteneur_nbadherents.columnconfigure(1, weight=1)
        conteneur_nbadherents.rowconfigure(0, weight=1)
        conteneur_nbadherents.grid(row=0, column=0, sticky="nsew")

        lnbadh = Label(conteneur_nbadherents, text="nombre d'adhérent :")
        lnbadh.config(bg='skyblue')
        lnbadh.grid(row=0, column=0, padx=(0, 15))
        self.nbadh = Spinbox(conteneur_nbadherents, from_=0, to=10)
        self.nbadh.grid(row=0, column=1)

        conteneur_adherents = Frame(formulaire_droit)
        conteneur_adherents.config(bg='skyblue')
        conteneur_adherents.columnconfigure(0, weight=1)
        conteneur_adherents.columnconfigure(1, weight=1)
        conteneur_adherents.rowconfigure(0, weight=1)
        conteneur_adherents.grid(row=1, column=0, sticky="nsew")

        lnbadh = Label(conteneur_nbadherents, text="nombre d'adhérent :")
        lnbadh.config(bg='skyblue')
        lnbadh.grid(row=0, column=0, padx=(0, 15))
        self.nbadh = Spinbox(conteneur_nbadherents)
        self.nbadh.grid(row=0, column=1)
