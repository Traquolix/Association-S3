import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

# Cette classe est la fenêtre de l'application qui permet de gérer les différentes pages
from Controleurs.ControleurBonDeCommande import ControleurBonDeCommande
from Controleurs.ControleurAdherents import ControleurAdherents
from Controleurs.ControleurFacture import ControleurFacture
from Controleurs.ControleurFenetre import ControleurFenetre
from Controleurs.ControleurBilan import ControleurBilan


class Fenetre:

    def __init__(self):

        self.container = Tk()  # Création de la fenetre
        self.container.title('application gestion trésorerie')
        self.container.geometry("1100x700")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Dictionnaire qui sert à stocker les instance des différentes vues.

        # Instanciation des différents controleurs
        self.ctrl_Fenetre = ControleurFenetre(self)
        self.ctrl_Adherents = ControleurAdherents(self)
        self.ctrl_Bon_de_commande = ControleurBonDeCommande(self)
        self.ctrl_Facture = ControleurFacture(self)
        self.ctrl_Bilan = ControleurBilan(self)

        for F in (Accueil, VueAdherents, VueOrganisations, VueFacture, VueBonDeCommande, VueBilan, VueBilan_categories):

            if F == VueAdherents or F == VueOrganisations:
                frame = F(self.container, ctrl_fenetre=self.ctrl_Fenetre, ctrl_adherent=self.ctrl_Adherents)
            elif F == VueBonDeCommande:
                frame = F(self.container, ctrl_fenetre=self.ctrl_Fenetre, ctrl_bon_commande=self.ctrl_Bon_de_commande)
            elif F == VueFacture:
                frame = F(self.container, ctrl_fenetre=self.ctrl_Fenetre, ctrl_facture=self.ctrl_Facture)
            elif F == VueBilan:
                frame = F(self.container, ctrl_fenetre=self.ctrl_Fenetre, ctrl_bilan=self.ctrl_Bilan)
            elif F == VueBilan_categories:
                frame = F(self.container, ctrl_fenetre=self.ctrl_Fenetre, ctrl_bilan=self.ctrl_Bilan)
            else:
                frame = F(self.container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Accueil)  # Au lancement de l'application on affiche la vue d'accueil

        self.ctrl_Adherents.set_vue_adherents(self.get_frame_VueAdherents())
        self.ctrl_Adherents.set_vue_organisations(self.get_frame_VueOrganisations())
        self.ctrl_Adherents.set_vue_bon_commande(self.get_frame_VueBonDeCommande())
        self.ctrl_Adherents.set_vue_facture(self.get_frame_VueFacture())

        self.ctrl_Fenetre.set_vue_bon_de_commande(self.get_frame_VueBonDeCommande())
        self.ctrl_Fenetre.set_vue_facture(self.get_frame_VueFacture())

        self.ctrl_Bon_de_commande.set_vue_bon_commande(self.get_frame_VueBonDeCommande())

        self.ctrl_Facture.set_vue_facture(self.get_frame_VueFacture())

        self.ctrl_Bilan.set_vue_bilan(self.get_frame_VueBilan())
        self.ctrl_Bilan.set_vue_bilan_categorie(self.get_frame_VueBilan_categories())

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_frame_Accueil(self):
        return self.frames[Accueil]

    def get_frame_VueAdherents(self):
        return self.frames[VueAdherents]

    def get_frame_VueOrganisations(self):
        return self.frames[VueOrganisations]

    def get_frame_VueBonDeCommande(self):
        return self.frames[VueBonDeCommande]

    def get_frame_VueFacture(self):
        return self.frames[VueFacture]

    def get_frame_VueBilan(self):
        return self.frames[VueBilan]

    def get_frame_VueBilan_categories(self):
        return self.frames[VueBilan_categories]

    def demarrer_application(self):
        self.container.mainloop()


class Accueil(tk.Frame):
    def __init__(self, parent, controleur_fenetre):
        tk.Frame.__init__(self, parent)
        self.config(bg="skyblue")  # On set le background de la page
        # La grille de placement de la frame principale est de 3 par 3
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # On  crée l'image qui représente le logo d'atala sur la page d'accueil
        logo_image = tk.PhotoImage(file='vue/images/atala_logo.png')
        logo = tk.Label(self, image=logo_image)
        logo.config(bg="skyblue")
        logo.photo = logo_image
        # On place cette image à la première cellule du conteneur ligne_haut
        logo.grid(row=0, column=0)

        # On crée le titre
        titre = tk.Label(self, text="Opérations de gestion de \nla trésorerie d'ATALA")
        titre.config(font=("Courier", 20), bg="skyblue")
        # On le place dans le conteneur titre aligner sur le bord gauche de celui-ci
        titre.grid(row=0, column=1, columnspan=2, sticky='w')

        # On configure le style qui s'appliquera à tous les boutons de l'interface
        style_boutons_application = ttk.Style()
        style_boutons_application.configure('my.TButton', font=('Courier', 12), borderwidth=0)

        # On crée le conteneur milieu gauche
        conteneur_milieu_gauche = Frame(self)
        conteneur_milieu_gauche.config(bg='skyblue')
        conteneur_milieu_gauche.grid(row=1, column=0, sticky="nsew")

        # On crée le bouton qui permet d'afficher la vue de gestion des adhérents
        image_bouton_adherents = tk.PhotoImage(file='vue/images/adherents.png')
        # Dans tkinter les widget on leur propre listeners, ainsi l'attribut command perme de préciser la
        # méthode des controleurs à appeler
        bouton_adherents = ttk.Button(conteneur_milieu_gauche, text="gérer adhérents", image=image_bouton_adherents,
                                      style='my.TButton',
                                      compound="left", command=lambda: controleur_fenetre.show_frame(VueAdherents))
        bouton_adherents.photo = image_bouton_adherents
        bouton_adherents.place(relx=0.5, rely=0.5, anchor=CENTER)

        # On crée le conteneur milieu centre
        conteneur_milieu_centre = Frame(self)
        conteneur_milieu_centre.config(bg='skyblue')
        conteneur_milieu_centre.grid(row=1, column=1, sticky="nsew")

        image_bouton_facture = tk.PhotoImage(file='vue/images/facture.png')
        bouton_facture = ttk.Button(conteneur_milieu_centre, text="générer facture", image=image_bouton_facture,
                                    style='my.TButton',
                                    compound="left", command=lambda: controleur_fenetre.show_frame(VueFacture))
        bouton_facture.photo = image_bouton_facture
        bouton_facture.place(relx=0.5, rely=0.5, anchor=CENTER)

        # On crée le conteneur milieu centre
        conteneur_milieu_droite = Frame(self)
        conteneur_milieu_droite.config(bg='skyblue')
        conteneur_milieu_droite.grid(row=1, column=2, sticky="nsew")

        image_bouton_bon_commande = tk.PhotoImage(file='vue/images/boncommande.png')
        bouton_bon_commande = ttk.Button(conteneur_milieu_droite, text="générer bon de \ncommande",
                                         image=image_bouton_bon_commande,
                                         style='my.TButton', compound="left",
                                         command=lambda: controleur_fenetre.show_frame(VueBonDeCommande))

        bouton_bon_commande.photo = image_bouton_bon_commande
        bouton_bon_commande.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Bouton Bilan coneteneur bas centre
        conteneur_bas_centre = Frame(self)
        conteneur_bas_centre.config(bg='skyblue')
        conteneur_bas_centre.grid(row=2, column=1, sticky="nsew")

        image_bouton_bilan = tk.PhotoImage(file='vue/images/facture.png')
        bouton_bilan = ttk.Button(conteneur_bas_centre, text="gérer bilan",
                                  image=image_bouton_bilan,
                                  style='my.TButton',
                                  compound="left",
                                  command=lambda: controleur_fenetre.show_frame(VueBilan))
        bouton_bilan.photo = image_bouton_bilan
        bouton_bilan.place(relx=0.5, rely=0.5, anchor=CENTER)


class VueAdherents(tk.Frame):

    def __init__(self, parent, ctrl_fenetre, ctrl_adherent):

        self.ctrlFenetre = ctrl_fenetre
        self.ctrlAdherent = ctrl_adherent

        tk.Frame.__init__(self, parent)
        self.config(bg="skyblue")  # On set le background de la page

        # La grille de placement de la frame principale est de 3 par 3
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # On crée le conteneur du bouton pour retourner à l'accueil
        conteneur_bouton_accueil = tk.Frame(self)
        conteneur_bouton_accueil.config(bg="skyblue")
        # La grille est de 1 par 1
        conteneur_bouton_accueil.rowconfigure(0, weight=1)
        conteneur_bouton_accueil.columnconfigure(0, weight=1)
        # On place ce conteneur à la première case du conteneur ligne_haut
        conteneur_bouton_accueil.grid(row=0, column=0, sticky="nsew")

        # On charge l'image qui va aller sur le bouton et création du bouton
        logo_btn_accueil = tk.PhotoImage(file='vue/images/accueil.png')
        accueil = ttk.Button(conteneur_bouton_accueil, text="accueil", image=logo_btn_accueil, style='my.TButton',
                             compound="left", command=lambda: ctrl_fenetre.show_frame(Accueil))
        accueil.photo = logo_btn_accueil
        accueil.place(relx=0.5, rely=0.5, anchor=CENTER)

        titre = tk.Label(self, text="Gestion des adhérents")
        titre.config(font=("Courier", 20), bg="skyblue")
        titre.grid(row=0, column=1, columnspan=2, sticky='nsew')

        conteneur_milieu_gauche = Frame(self)
        conteneur_milieu_gauche.config(bg='skyblue')
        conteneur_milieu_gauche.columnconfigure(0, weight=1)
        conteneur_milieu_gauche.rowconfigure(0, weight=1)
        conteneur_milieu_gauche.rowconfigure(1, weight=1)
        conteneur_milieu_gauche.rowconfigure(2, weight=1)
        conteneur_milieu_gauche.grid(row=1, column=0, sticky="nsew")

        formulaire = Frame(conteneur_milieu_gauche)
        formulaire.config(bg='skyblue')
        formulaire.columnconfigure(0, weight=1)
        formulaire.rowconfigure(0, weight=1)
        formulaire.rowconfigure(1, weight=1)
        formulaire.rowconfigure(2, weight=1)
        formulaire.rowconfigure(3, weight=1)
        formulaire.rowconfigure(4, weight=1)
        formulaire.rowconfigure(5, weight=1)
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

        conteneur_radio = Frame(formulaire)
        conteneur_radio.config(bg='skyblue')
        conteneur_radio.columnconfigure(0, weight=1)
        conteneur_radio.columnconfigure(1, weight=1)
        conteneur_radio.rowconfigure(0, weight=1)
        conteneur_radio.grid(row=2, column=0, sticky="nsew")

        self.choix = StringVar()
        self.choix.set("organisation")

        self.radio1 = Radiobutton(conteneur_radio, takefocus=0, variable=self.choix, text="organisation",
                                  value="organisation", tristatevalue=0, highlightthickness=0,
                                  command=lambda: self.choix_radio_button())
        self.radio1.config(bg='skyblue', activebackground='skyblue')
        self.radio1.grid(row=0, column=0, sticky="nsew")

        self.radio2 = Radiobutton(conteneur_radio, variable=self.choix, takefocus=0, text="indépendant",
                                  value="indépendant", tristatevalue=0, highlightthickness=0,
                                  command=lambda: self.choix_radio_button())
        self.radio2.config(bg='skyblue', activebackground='skyblue')
        self.radio2.grid(row=0, column=1, sticky="nsew")

        self.conteneur_organisation = Frame(formulaire)
        self.conteneur_organisation.config(bg='skyblue')
        self.conteneur_organisation.columnconfigure(0, weight=1)
        self.conteneur_organisation.columnconfigure(1, weight=1)
        self.conteneur_organisation.columnconfigure(2, weight=2)
        self.conteneur_organisation.rowconfigure(0, weight=1)

        lorga = Label(self.conteneur_organisation, text="organisation :")
        lorga.config(bg='skyblue')
        lorga.grid(row=0, column=0, padx=(0, 15))
        self.organisations = tk.Listbox(self.conteneur_organisation, width=10, height=3)
        self.actualiser_liste_organisations()
        self.organisations.grid(row=0, column=1)

        scrollbar = ttk.Scrollbar(self.conteneur_organisation)
        scrollbar.grid(row=0, column=2)
        self.organisations.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.organisations.yview)

        self.conteneur_independant = Frame(formulaire)
        self.conteneur_independant.config(bg='skyblue')
        self.conteneur_independant.columnconfigure(0, weight=1)
        self.conteneur_independant.rowconfigure(0, weight=1)
        self.conteneur_independant.rowconfigure(1, weight=1)

        ladresse = Label(self.conteneur_independant, text="adresse :")
        ladresse.config(bg='skyblue')
        ladresse.grid(row=0, column=0, padx=(0, 15))
        self.str_adresse = tk.StringVar()
        self.str_adresse.set("")
        self.adresse = Entry(self.conteneur_independant, textvariable=self.str_adresse, width=20)
        self.adresse.grid(row=0, column=1)

        lville = Label(self.conteneur_independant, text="ville :")
        lville.config(bg='skyblue')
        lville.grid(row=1, column=0, padx=(0, 15), pady=(0, 15))
        self.str_ville = tk.StringVar()
        self.str_ville.set("")
        self.ville = Entry(self.conteneur_independant, textvariable=self.str_ville, width=20)
        self.ville.grid(row=1, column=1, pady=(0, 15))

        ajouter = ttk.Button(formulaire, text="ajouter adhérent", style='my.TButton',
                             command=lambda: ctrl_adherent.ajouter_adherent())
        ajouter.grid(row=5, column=0)

        conteneur_milieu = Frame(self)
        conteneur_milieu.config(bg='skyblue')
        conteneur_milieu.rowconfigure(0, weight=1)
        conteneur_milieu.rowconfigure(1, weight=1)
        conteneur_milieu.columnconfigure(0, weight=1)
        conteneur_milieu.grid(row=1, column=1, sticky="nsew")

        conteneur_adherents = Frame(conteneur_milieu)
        conteneur_adherents.config(bg='skyblue')
        conteneur_adherents.rowconfigure(0, weight=1)
        conteneur_adherents.columnconfigure(0, weight=1)
        conteneur_adherents.columnconfigure(1, weight=1)
        conteneur_adherents.grid(row=0, column=0, sticky="nsew")
        self.adherents = tk.Listbox(conteneur_adherents, width=60)
        self.actualiser_liste_adherents()
        self.adherents.grid(row=0, column=0, sticky="ens")

        scrollbar = ttk.Scrollbar(conteneur_adherents)
        scrollbar.grid(row=0, column=1, sticky="wns")
        self.adherents.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.adherents.yview)

        conteneur_supprimer = tk.Frame(conteneur_milieu)
        conteneur_supprimer.config(bg='skyblue')
        conteneur_supprimer.rowconfigure(0, weight=1)
        conteneur_supprimer.columnconfigure(0, weight=1)
        conteneur_supprimer.columnconfigure(1, weight=1)
        conteneur_supprimer.grid(row=1, column=0)

        supprimer = ttk.Button(conteneur_supprimer, text="supprimer adhérent", style='my.TButton',
                               command=lambda: ctrl_adherent.supprimer_adherent())
        supprimer.grid(row=0, column=0, padx=(0, 15))

        tout_supprimer = ttk.Button(conteneur_supprimer, text="tout supprimer", style='my.TButton',
                                    command=lambda: ctrl_adherent.supprimer_tout_adherents())
        tout_supprimer.grid(row=0, column=1)

        conteneur_bas = tk.Frame(self)
        conteneur_bas.config(bg="skyblue")
        conteneur_bas.rowconfigure(0, weight=1)
        conteneur_bas.columnconfigure(0, weight=1)
        conteneur_bas.columnconfigure(1, weight=1)
        conteneur_bas.columnconfigure(2, weight=1)
        conteneur_bas.grid(row=2, column=0, columnspan=3, sticky="nsew")

        conteneur_gerer_organisation = tk.Frame(conteneur_bas)
        conteneur_gerer_organisation.config(bg="skyblue")
        conteneur_gerer_organisation.rowconfigure(0, weight=1)
        conteneur_gerer_organisation.columnconfigure(0, weight=1)
        conteneur_gerer_organisation.grid(row=0, column=0, columnspan=1, sticky="nsew")
        gerer_organisation = ttk.Button(conteneur_gerer_organisation, text="gérer organisation", style='my.TButton',
                                        command=lambda: ctrl_fenetre.show_frame(VueOrganisations))
        gerer_organisation.grid(row=0, column=0)

        self.choix_radio_button()

    def actualiser_liste_adherents(self):
        self.adherents.delete(0, END)
        liste = self.ctrlAdherent.actualiser_liste_adherents()
        liste2 = self.ctrlAdherent.actualiser_liste_adherents_independants()
        cpt = 1
        for adherent in liste:
            self.adherents.insert(cpt, adherent)
            cpt += 1
        for adherent in liste2:
            self.adherents.insert(cpt, adherent)
            cpt += 1
        self.adherents.select_set(0)

    def actualiser_liste_organisations(self):
        self.organisations.delete(0, END)
        liste = self.ctrlAdherent.actualiser_liste_organisations_noms()
        cpt = 1
        for organisation in liste:
            self.organisations.insert(cpt, organisation)
            cpt += 1
        self.organisations.select_set(0)

    def get_prenom(self):
        return self.prenom.get()

    def get_nom(self):
        return self.nom.get()

    def get_organisation(self):
        return self.organisations.get(ANCHOR)

    def get_choix_selectionne(self):
        return self.choix.get()

    def get_adresse(self):
        return self.adresse.get()

    def get_ville(self):
        return self.ville.get()

    def get_selected_adherent(self):
        return self.adherents.get(ANCHOR)

    def viderChamps(self):
        self.str_prenom.set("")
        self.str_nom.set("")
        self.str_adresse.set("")
        self.str_ville.set("")
        self.organisations.select_set(0)

    def champ_vide(self):
        est_vide = False
        if self.get_prenom() == "":
            est_vide = True
        if self.get_nom() == "":
            est_vide = True
        if self.get_ville() == "" and self.get_choix_selectionne() == "indépendant":
            est_vide = True
        if self.get_adresse() == "" and self.get_choix_selectionne() == "indépendant":
            est_vide = True
        return est_vide

    def listbox_adherent_est_vide(self):
        return self.adherents.size() == 0

    def listbox_organisations_est_vide(self):
        return self.organisations.size() == 0

    def choix_radio_button(self):
        if self.choix.get() == "organisation":
            self.conteneur_organisation.grid(row=4, column=0, sticky="nsew")
            self.conteneur_independant.grid_forget()
        if self.choix.get() == "indépendant":
            self.conteneur_organisation.grid_forget()
            self.conteneur_independant.grid(row=4, column=0, sticky="nsew")

    @staticmethod
    def message_erreur_suppression():
        messagebox.showerror(title="erreur de suppression", message="Il n'y a plus d'adhérents")

    @staticmethod
    def message_erreur_champs_vide():
        messagebox.showwarning(title="erreur de saisie", message="veuillez remplir tout les champs")

    @staticmethod
    def message_erreur_organisation_vide():
        messagebox.showwarning(title="erreur de saisie", message="veuillez selectionner une organisation")

    @staticmethod
    def message_erreur_ajout():
        messagebox.showerror(title="erreur d'ajout", message="l'adhérent existe déjà")


class VueOrganisations(tk.Frame):

    def __init__(self, parent, ctrl_fenetre, ctrl_adherent):
        tk.Frame.__init__(self, parent)
        self.config(bg='skyblue')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.ctrl_adherent = ctrl_adherent

        conteneur_bouton_retour = tk.Frame(self)
        conteneur_bouton_retour.config(bg="skyblue")
        conteneur_bouton_retour.rowconfigure(0, weight=1)
        conteneur_bouton_retour.columnconfigure(0, weight=1)
        conteneur_bouton_retour.grid(row=0, column=0, sticky="nsew")

        retour = ttk.Button(conteneur_bouton_retour, text="retour", style='my.TButton',
                            compound="left", command=lambda: ctrl_fenetre.show_frame(VueAdherents))
        retour.place(relx=0.5, rely=0.5, anchor=CENTER)

        titre = tk.Label(self, text="Gestion des organisations")
        titre.config(font=("Courier", 20), bg="skyblue")
        titre.grid(row=0, column=1, columnspan=2, sticky='nsew')

        conteneur_milieu_gauche = Frame(self)
        conteneur_milieu_gauche.config(bg='skyblue')
        conteneur_milieu_gauche.columnconfigure(0, weight=1)
        conteneur_milieu_gauche.rowconfigure(0, weight=1)
        conteneur_milieu_gauche.rowconfigure(1, weight=1)
        conteneur_milieu_gauche.rowconfigure(2, weight=1)
        conteneur_milieu_gauche.grid(row=1, column=0, sticky="nsew")

        formulaire = Frame(conteneur_milieu_gauche)
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

        conteneur_adresse = Frame(formulaire)
        conteneur_adresse.config(bg='skyblue')
        conteneur_adresse.columnconfigure(0, weight=1)
        conteneur_adresse.columnconfigure(1, weight=1)
        conteneur_adresse.rowconfigure(0, weight=1)
        conteneur_adresse.grid(row=1, column=0, sticky="nsew")

        ladresse = Label(conteneur_adresse, text="adresse :")
        ladresse.config(bg='skyblue')
        ladresse.grid(row=0, column=0, padx=(0, 15))
        self.str_adresse = tk.StringVar()
        self.str_adresse.set("")
        self.adresse = Entry(conteneur_adresse, textvariable=self.str_adresse, width=20)
        self.adresse.grid(row=0, column=1)

        conteneur_ville = Frame(formulaire)
        conteneur_ville.config(bg='skyblue')
        conteneur_ville.columnconfigure(0, weight=1)
        conteneur_ville.columnconfigure(1, weight=1)
        conteneur_ville.rowconfigure(0, weight=1)
        conteneur_ville.grid(row=2, column=0, sticky="nsew")

        lville = Label(conteneur_ville, text="ville :")
        lville.config(bg='skyblue')
        lville.grid(row=0, column=0, padx=(0, 15))
        self.str_ville = tk.StringVar()
        self.str_ville.set("")
        self.ville = Entry(conteneur_ville, textvariable=self.str_ville, width=20)
        self.ville.grid(row=0, column=1)

        ajouter = ttk.Button(formulaire, text="ajouter organisation", style='my.TButton',
                             command=lambda: ctrl_adherent.ajouter_organisation())
        ajouter.grid(row=3, column=0)

        conteneur_milieu = Frame(self)
        conteneur_milieu.config(bg='skyblue')
        conteneur_milieu.rowconfigure(0, weight=1)
        conteneur_milieu.rowconfigure(1, weight=1)
        conteneur_milieu.columnconfigure(0, weight=1)
        conteneur_milieu.grid(row=1, column=1, sticky="nsew")

        conteneur_organisation = tk.Frame(conteneur_milieu)
        conteneur_organisation.config(bg='skyblue')
        conteneur_organisation.rowconfigure(0, weight=1)
        conteneur_organisation.columnconfigure(0, weight=1)
        conteneur_organisation.columnconfigure(1, weight=1)
        conteneur_organisation.grid(row=0, column=0)

        self.organisations = tk.Listbox(conteneur_organisation, width=60)
        self.actualiser_liste_organisations()
        self.organisations.grid(row=0, column=0)

        scrollbar = ttk.Scrollbar(conteneur_organisation)
        scrollbar.grid(row=0, column=1, sticky="nsew")
        self.organisations.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.organisations.yview)

        conteneur_supprimer = tk.Frame(conteneur_milieu)
        conteneur_supprimer.config(bg='skyblue')
        conteneur_supprimer.rowconfigure(0, weight=1)
        conteneur_supprimer.columnconfigure(0, weight=1)
        conteneur_supprimer.columnconfigure(1, weight=1)
        conteneur_supprimer.grid(row=1, column=0)

        supprimer = ttk.Button(conteneur_supprimer, text="supprimer organisation", style='my.TButton',
                               command=lambda: ctrl_adherent.supprimer_organisation())
        supprimer.grid(row=0, column=0, padx=(0, 15))

        tout_supprimer = ttk.Button(conteneur_supprimer, text="tout supprimer", style='my.TButton',
                                    command=lambda: ctrl_adherent.supprimer_tout_organisations())
        tout_supprimer.grid(row=0, column=1)

    def get_nom(self):
        return self.nom.get()

    def get_adresse(self):
        return self.adresse.get()

    def get_ville(self):
        return self.ville.get()

    def get_selected_organisation(self):
        return self.organisations.get(ANCHOR)

    def viderChamps(self):
        self.str_nom.set("")
        self.str_adresse.set("")
        self.str_ville.set("")

    def champ_vide(self):
        est_vide = False
        if self.get_nom() == "":
            est_vide = True
        if self.get_adresse() == "":
            est_vide = True
        if self.get_ville() == "":
            est_vide = True
        return est_vide

    def actualiser_liste_organisations(self):
        self.organisations.delete(0, END)
        liste = self.ctrl_adherent.actualiser_liste_organisations_complets()
        cpt = 1
        for organisation in liste:
            self.organisations.insert(cpt, organisation)
            cpt += 1
        self.organisations.select_set(0)

    def listbox_organisations_est_vide(self):
        return self.organisations.size() == 0

    @staticmethod
    def message_erreur_suppression():
        messagebox.showerror(title="erreur de suppression", message="Il n'y a plus d'organisations")

    @staticmethod
    def message_erreur_champs_vide():
        messagebox.showwarning(title="erreur de saisie", message="veuillez remplir tout les champs")

    @staticmethod
    def message_erreur_ajout():
        messagebox.showerror(title="erreur d'ajout", message="l'organisation existe déjà")


class VueFacture(tk.Frame):
    def __init__(self, parent, ctrl_fenetre, ctrl_facture):
        self.ctrl_facture = ctrl_facture

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

        logo_btn_accueil = tk.PhotoImage(file='vue/images/accueil.png')
        accueil = ttk.Button(conteneur_bouton_accueil, text="accueil", image=logo_btn_accueil, style='my.TButton',
                             compound="left", command=lambda: ctrl_fenetre.facture_accueil(Accueil))
        accueil.photo = logo_btn_accueil
        accueil.place(relx=0.5, rely=0.5, anchor=CENTER)

        conteneur_milieu = Frame(self)
        conteneur_milieu.config(bg='skyblue')
        conteneur_milieu.rowconfigure(0, weight=1)
        conteneur_milieu.rowconfigure(1, weight=1)
        conteneur_milieu.columnconfigure(0, weight=1)
        conteneur_milieu.columnconfigure(1, weight=1)
        conteneur_milieu.columnconfigure(2, weight=1)
        conteneur_milieu.grid(row=1, column=0, columnspan=3, sticky="nsew")

        conteneur_formulaire_haut = Frame(conteneur_milieu, width=40)
        conteneur_formulaire_haut.config(bg='skyblue')
        conteneur_formulaire_haut.rowconfigure(0, weight=1)
        conteneur_formulaire_haut.rowconfigure(1, weight=1)
        conteneur_formulaire_haut.columnconfigure(0, weight=1)
        conteneur_formulaire_haut.columnconfigure(1, weight=1)
        conteneur_formulaire_haut.grid(row=0, column=0, columnspan=3, sticky="nsew")

        conteneur_formulaire_haut_gauche = Frame(conteneur_formulaire_haut)
        conteneur_formulaire_haut_gauche.config(bg='skyblue')
        conteneur_formulaire_haut_gauche.rowconfigure(0, weight=1)
        conteneur_formulaire_haut_gauche.rowconfigure(1, weight=1)
        conteneur_formulaire_haut_gauche.rowconfigure(2, weight=1)
        conteneur_formulaire_haut_gauche.columnconfigure(0, weight=1)
        conteneur_formulaire_haut_gauche.columnconfigure(1, weight=1)
        conteneur_formulaire_haut_gauche.grid(row=0, rowspan=2, column=0)

        label_num_facture = Label(conteneur_formulaire_haut_gauche, text="numéro facture :")
        label_num_facture.config(bg='skyblue')
        label_num_facture.grid(row=0, column=0, pady=(0, 10), padx=(0, 15))
        self.str_num_facture = tk.StringVar()
        self.str_num_facture.set("")
        self.num_facture = Entry(conteneur_formulaire_haut_gauche, textvariable=self.str_num_facture, width=20)
        self.num_facture.grid(row=0, column=1, pady=(0, 10))

        label_num_bon = Label(conteneur_formulaire_haut_gauche, text="bon de commande référent : ")
        label_num_bon.config(bg='skyblue')
        label_num_bon.grid(row=1, column=0, padx=(0, 15), pady=(0, 10))
        self.str_num_bon = tk.StringVar()
        self.str_num_bon.set("")
        self.num_bon = Entry(conteneur_formulaire_haut_gauche, textvariable=self.str_num_bon, width=20)
        self.num_bon.grid(row=1, column=1, pady=(0, 10))

        label_montant_total = Label(conteneur_formulaire_haut_gauche, text="montant total : ")
        label_montant_total.config(bg='skyblue')
        label_montant_total.grid(row=2, column=0, padx=(0, 15))
        self.str_montant_total = tk.StringVar()
        self.str_montant_total.set("")
        self.montant_total = Entry(conteneur_formulaire_haut_gauche, textvariable=self.str_montant_total, width=20)
        self.montant_total.grid(row=2, column=1)

        conteneur_formulaire_haut_droite = Frame(conteneur_formulaire_haut)
        conteneur_formulaire_haut_droite.config(bg='skyblue')
        conteneur_formulaire_haut_droite.rowconfigure(0, weight=1)
        conteneur_formulaire_haut_droite.rowconfigure(1, weight=1)
        conteneur_formulaire_haut_droite.rowconfigure(2, weight=1)
        conteneur_formulaire_haut_droite.columnconfigure(0, weight=1)
        conteneur_formulaire_haut_droite.columnconfigure(1, weight=1)
        conteneur_formulaire_haut_droite.columnconfigure(2, weight=1)
        conteneur_formulaire_haut_droite.grid(row=0, rowspan=2, column=1)

        conteneur_organisations = Frame(conteneur_formulaire_haut_droite)
        conteneur_organisations.config(bg='skyblue')
        conteneur_organisations.rowconfigure(0, weight=1)
        conteneur_organisations.columnconfigure(0, weight=1)
        conteneur_organisations.columnconfigure(1, weight=1)
        conteneur_organisations.columnconfigure(2, weight=2)
        conteneur_organisations.grid(row=0, columnspan=3, column=0, pady=(0, 15), sticky='w')

        lorganisations = Label(conteneur_organisations, text="destinataire :")
        lorganisations.config(bg='skyblue')
        lorganisations.grid(row=0, column=0, padx=(0, 15))
        self.organisations = tk.Listbox(conteneur_organisations, width=20, height=3)
        self.actualiser_liste_organisations()
        self.organisations.grid(row=0, column=1, padx=(0, 15))

        scrollbar = ttk.Scrollbar(conteneur_organisations)
        scrollbar.grid(row=0, column=2)
        self.organisations.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.organisations.yview)

        label_nombre_adherents = Label(conteneur_formulaire_haut_droite, text="nombre adhérents : ")
        label_nombre_adherents.config(bg='skyblue')
        label_nombre_adherents.grid(row=1, column=0, padx=(0, 15), pady=(0, 15))
        self.int_nombre = tk.IntVar()
        self.int_nombre.set(0)
        self.nombre_adherents = Spinbox(conteneur_formulaire_haut_droite, from_=1, to=30, textvariable=self.int_nombre)
        self.nombre_adherents.grid(row=1, column=1, padx=(0, 30), pady=(0, 15)) # modifier le 30 pour modifier le nombre max d'adhérent (/!\ le code peut faire jusqu'a un maximum de 40)

        self.valider = ttk.Button(conteneur_formulaire_haut_droite, text="valider", style='my.TButton',
                                  compound="left",
                                  command=lambda: ctrl_facture.valider_informations_generales_facture())
        self.valider.grid(row=1, column=2, pady=(0, 15))

        conteneur_formulaire_bas = Frame(conteneur_milieu, width=600)
        conteneur_formulaire_bas.config(bg='skyblue')
        conteneur_formulaire_bas.rowconfigure(0, weight=1)
        conteneur_formulaire_bas.columnconfigure(0, weight=1)
        conteneur_formulaire_bas.columnconfigure(1, weight=1)
        conteneur_formulaire_bas.grid(row=1, column=0, columnspan=3, sticky="nsew")

        conteneur_informations = Frame(conteneur_formulaire_bas)
        conteneur_informations.config(bg='skyblue')
        conteneur_informations.rowconfigure(0, weight=1)
        conteneur_informations.rowconfigure(1, weight=1)
        conteneur_informations.rowconfigure(2, weight=1)
        conteneur_informations.columnconfigure(0, weight=1)
        conteneur_informations.grid(row=0, column=0, sticky="e")

        conteneur_type_tarif = Frame(conteneur_informations)
        conteneur_type_tarif.config(bg='skyblue')
        conteneur_type_tarif.rowconfigure(0, weight=1)
        conteneur_type_tarif.columnconfigure(0, weight=1)
        conteneur_type_tarif.columnconfigure(1, weight=1)
        conteneur_type_tarif.grid(row=0, column=0, pady=(20, 20), sticky="e")
        label_type_tarif = Label(conteneur_type_tarif, text="type de tarif : ")
        label_type_tarif.config(bg='skyblue')
        label_type_tarif.grid(row=0, column=0, padx=(0, 15))
        self.str_type_tarif = tk.StringVar()
        self.str_type_tarif.set("")
        self.type_tarif = Entry(conteneur_type_tarif, textvariable=self.str_type_tarif, width=20)
        self.type_tarif.config(state="disabled")
        self.type_tarif.grid(row=0, column=1)

        conteneur_adherents = Frame(conteneur_formulaire_bas)
        conteneur_adherents.config(bg='skyblue')
        conteneur_adherents.rowconfigure(0, weight=1)
        conteneur_adherents.rowconfigure(1, weight=1)
        conteneur_adherents.columnconfigure(0, weight=1)
        conteneur_adherents.grid(row=0, column=1, sticky="nsew")

        self.adherents = tk.Listbox(conteneur_adherents, width=40)
        self.adherents.config(state='disabled')
        # self.actualiser_liste_adherents()
        self.adherents.grid(row=0, column=0)

        self.ajouter = ttk.Button(conteneur_adherents, text="ajouter", style='my.TButton',
                                  command=lambda: ctrl_facture.ajouter_informations_adherents_facture())
        self.ajouter.config(state='disabled')
        self.ajouter.grid(row=1, column=0)

        ligne_bas = Frame(self)
        ligne_bas.config(bg='skyblue')
        ligne_bas.rowconfigure(0, weight=1)
        ligne_bas.rowconfigure(1, weight=1)
        ligne_bas.rowconfigure(2, weight=1)
        ligne_bas.columnconfigure(0, weight=1)
        ligne_bas.columnconfigure(1, weight=1)
        ligne_bas.columnconfigure(2, weight=1)
        ligne_bas.columnconfigure(3, weight=1)
        ligne_bas.grid(row=2, column=0, columnspan=3, sticky="nsew")

        self.adherents_ajoutes = ttk.Treeview(ligne_bas, columns=('prenom', 'nom', 'tarif'))
        self.adherents_ajoutes.heading('prenom', text='Prénom')
        self.adherents_ajoutes.heading('nom', text='Nom')
        self.adherents_ajoutes.heading('tarif', text='type de Tarif')
        self.adherents_ajoutes['show'] = 'headings'
        self.adherents_ajoutes.grid(row=0, column=1)

        self.generer = ttk.Button(ligne_bas, text="générer Facture", style='my.TButton',
                                  command=lambda: ctrl_facture.generer())
        self.generer.config(state='disabled')
        self.generer.grid(row=1, column=1)

    def actualiser_liste_adherents(self, liste):
        self.adherents.delete(0, END)
        cpt = 1
        for adherent in liste:
            self.adherents.insert(cpt, adherent)
            cpt += 1
        self.adherents.select_set(0)

    def actualiser_liste_organisations(self):
        self.organisations.delete(0, END)
        liste = self.ctrl_facture.actualiser_liste_organisations_noms()
        self.organisations.insert(1, "indépendants")
        cpt = 2
        for organisation in liste:
            self.organisations.insert(cpt, organisation)
            cpt += 1
        self.organisations.select_set(0)

    def nombre_adherents_liste(self):
        return self.adherents.size()

    def champs_partie1_vides(self):
        est_vide = False
        if self.get_numero_bon() == "":
            est_vide = True
        if self.get_numero_facture() == "":
            est_vide = True
        if self.get_montant_total() == "":
            est_vide = True
        return est_vide

    def champs_partie2_vides(self):
        est_vide = False
        if self.get_type_tarif() == "":
            est_vide = True
        return est_vide

    def listbox_est_vide(self):
        return self.organisations.size() == 0

    def activer_champs_partie1(self):
        self.num_facture.config(state="normal")
        self.num_bon.config(state="normal")
        self.organisations.config(state="normal")
        self.montant_total.config(state="normal")
        self.nombre_adherents.config(state="normal")
        self.valider.config(state="normal")

    def desactiver_champs_partie1(self):
        self.num_facture.config(state="disabled")
        self.num_bon.config(state="disabled")
        self.organisations.config(state="disabled")
        self.montant_total.config(state="disabled")
        self.nombre_adherents.config(state="disabled")
        self.valider.config(state="disabled")

    def activer_champs_partie2(self):
        self.type_tarif.config(state="normal")
        self.adherents.config(state="normal")
        self.ajouter.config(state="normal")

    def activer_generer(self):
        self.generer.config(state="normal")

    def desactiver_generer(self):
        self.generer.config(state="disabled")

    def desactiver_champs_partie2(self):
        self.type_tarif.config(state="disabled")
        self.adherents.config(state="disabled")
        self.ajouter.config(state="disabled")

    def vider_champs_partie2(self):
        self.str_type_tarif.set("")
        self.adherents.select_set(0)

    def get_numero_bon(self):
        return self.num_bon.get()

    def get_numero_facture(self):
        return self.num_facture.get()

    def get_destinataire(self):
        return self.organisations.get(ANCHOR)

    def get_montant_total(self):
        return self.montant_total.get()

    def get_nombre_adherents(self):
        return self.int_nombre.get()

    def get_type_tarif(self):
        return self.type_tarif.get()

    def get_adherent_selectionne(self):
        adherent = self.adherents.get(ANCHOR)
        self.adherents.delete(ANCHOR)
        return adherent

    def actualiser_liste_adherents_ajoutes(self, prenom, nom, type):
        self.adherents_ajoutes.insert('', 'end', prenom, text=prenom)
        self.adherents_ajoutes.set(prenom, 'prenom', prenom)
        self.adherents_ajoutes.set(prenom, 'nom', nom)
        self.adherents_ajoutes.set(prenom, 'tarif', type)

    def effacer_informations(self):
        self.ctrl_facture.nouvelle_facture()
        self.str_num_facture.set("")
        self.str_num_bon.set("")
        self.str_montant_total.set("")
        self.nombre_adherents.selection_to(0)
        self.str_type_tarif.set("")
        for i in self.adherents_ajoutes.get_children():
            self.adherents_ajoutes.delete(i)

    @staticmethod
    def get_fichier_path():
        filename = tk.filedialog.asksaveasfilename(defaultextension=".pdf")
        return filename

    @staticmethod
    def message_erreur_champs_vide():
        messagebox.showwarning(title="erreur de saisie", message="veuillez remplir tout les champs")

    @staticmethod
    def message_erreur_nombres_adherents():
        messagebox.showwarning(title="erreur de saisie", message="Il n'y a pas assez d'adhérents")

    @staticmethod
    def message_erreur_ajout_adherent():
        messagebox.showerror(title="erreur d'ajout", message="Vous ne pouvez pas ajouter plus d'adhérents")


class VueBonDeCommande(tk.Frame):
    def __init__(self, parent, ctrl_fenetre, ctrl_bon_commande):

        self.ctrl_bon_commande = ctrl_bon_commande

        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        conteneur_bouton_accueil = tk.Frame(self)
        conteneur_bouton_accueil.config(bg="skyblue")
        conteneur_bouton_accueil.rowconfigure(0, weight=1)
        conteneur_bouton_accueil.columnconfigure(0, weight=1)
        conteneur_bouton_accueil.grid(row=0, column=0, sticky="nsew")

        logo_btn_accueil = tk.PhotoImage(file='vue/images/accueil.png')
        accueil = ttk.Button(conteneur_bouton_accueil, text="accueil", image=logo_btn_accueil, style='my.TButton',
                             compound="left", command=lambda: ctrl_fenetre.bon_commande_accueil(Accueil))
        accueil.photo = logo_btn_accueil
        accueil.place(relx=0.5, rely=0.5, anchor=CENTER)

        titre = tk.Label(self, text="Generation Bon de commande")
        titre.config(font=("Courier", 20), bg="skyblue")
        titre.grid(row=0, column=1, columnspan=2, sticky='nsew')

        conteneur_milieu = Frame(self)
        conteneur_milieu.config(bg='skyblue')
        conteneur_milieu.rowconfigure(0, weight=1)
        conteneur_milieu.rowconfigure(1, weight=1)
        conteneur_milieu.columnconfigure(0, weight=1)
        conteneur_milieu.columnconfigure(1, weight=1)
        conteneur_milieu.columnconfigure(2, weight=1)
        conteneur_milieu.grid(row=1, column=0, columnspan=3, sticky="nsew")

        conteneur_formulaire_haut = Frame(conteneur_milieu, width=40)
        conteneur_formulaire_haut.config(bg='skyblue')
        conteneur_formulaire_haut.rowconfigure(0, weight=1)
        conteneur_formulaire_haut.rowconfigure(1, weight=1)
        conteneur_formulaire_haut.columnconfigure(0, weight=1)
        conteneur_formulaire_haut.columnconfigure(1, weight=1)
        conteneur_formulaire_haut.grid(row=0, column=0, columnspan=3, sticky="nsew")

        conteneur_num_bon = Frame(conteneur_formulaire_haut)
        conteneur_num_bon.config(bg='skyblue')
        conteneur_num_bon.rowconfigure(0, weight=1)
        conteneur_num_bon.columnconfigure(0, weight=1)
        conteneur_num_bon.columnconfigure(1, weight=1)
        conteneur_num_bon.grid(row=0, column=0)

        label_num_bon = Label(conteneur_num_bon, text="numéro bon de commande : ")
        label_num_bon.config(bg='skyblue')
        label_num_bon.grid(row=0, column=0, padx=(0, 15))
        self.str_num = tk.StringVar()
        self.str_num.set("")
        self.num_bon = Entry(conteneur_num_bon, textvariable=self.str_num, width=20)
        self.num_bon.grid(row=0, column=1)

        conteneur_organisations = Frame(conteneur_formulaire_haut)
        conteneur_organisations.config(bg='skyblue')
        conteneur_organisations.columnconfigure(0, weight=1)
        conteneur_organisations.columnconfigure(1, weight=1)
        conteneur_organisations.columnconfigure(2, weight=2)
        conteneur_organisations.rowconfigure(0, weight=1)
        conteneur_organisations.grid(row=1, column=0)

        lorganisations = Label(conteneur_organisations, text="destinataire :")
        lorganisations.config(bg='skyblue')
        lorganisations.grid(row=0, column=0, padx=(0, 15))
        self.organisations = tk.Listbox(conteneur_organisations, width=20, height=3)
        self.actualiser_liste_organisations()
        self.organisations.grid(row=0, column=1, padx=(0, 15))

        scrollbar = ttk.Scrollbar(conteneur_organisations)
        scrollbar.grid(row=0, column=2)
        self.organisations.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.organisations.yview)

        conteneur_montant_total = Frame(conteneur_formulaire_haut)
        conteneur_montant_total.config(bg='skyblue')
        conteneur_montant_total.rowconfigure(0, weight=1)
        conteneur_montant_total.columnconfigure(0, weight=1)
        conteneur_montant_total.columnconfigure(1, weight=1)
        conteneur_montant_total.grid(row=0, column=1, sticky='w')

        label_montant_total = Label(conteneur_montant_total, text="montant total : ")
        label_montant_total.config(bg='skyblue')
        label_montant_total.grid(row=0, column=0, padx=(0, 15))
        self.str_montant_total = tk.StringVar()
        self.str_montant_total.set("")
        self.montant_total = Entry(conteneur_montant_total, textvariable=self.str_montant_total, width=20)
        self.montant_total.grid(row=0, column=1)

        conteneur_nombre_adherents = Frame(conteneur_formulaire_haut)
        conteneur_nombre_adherents.config(bg='skyblue')
        conteneur_nombre_adherents.rowconfigure(0, weight=1)
        conteneur_nombre_adherents.columnconfigure(0, weight=1)
        conteneur_nombre_adherents.columnconfigure(1, weight=1)
        conteneur_nombre_adherents.columnconfigure(2, weight=1)
        conteneur_nombre_adherents.grid(row=1, column=1, sticky='w')

        label_nombre_adherents = Label(conteneur_nombre_adherents, text="nombre adhérents : ")
        label_nombre_adherents.config(bg='skyblue')
        label_nombre_adherents.grid(row=0, column=0, padx=(0, 15))
        self.int_nombre = tk.IntVar()
        self.int_nombre.set(0)
        self.nombre_adherents = Spinbox(conteneur_nombre_adherents, from_=1, to=10, textvariable=self.int_nombre)
        self.nombre_adherents.grid(row=0, column=1, padx=(0, 30))
        self.valider = ttk.Button(conteneur_nombre_adherents, text="valider", style='my.TButton',
                                  command=lambda: ctrl_bon_commande.valider_informations_generales_bon())
        self.valider.grid(row=0, column=2)

        conteneur_formulaire_bas = Frame(conteneur_milieu, width=600)
        conteneur_formulaire_bas.config(bg='skyblue')
        conteneur_formulaire_bas.rowconfigure(0, weight=1)
        conteneur_formulaire_bas.columnconfigure(0, weight=1)
        conteneur_formulaire_bas.columnconfigure(1, weight=1)
        conteneur_formulaire_bas.columnconfigure(2, weight=1)
        conteneur_formulaire_bas.grid(row=1, column=0, columnspan=3, sticky="nsew")

        conteneur_informations = Frame(conteneur_formulaire_bas)
        conteneur_informations.config(bg='skyblue')
        conteneur_informations.rowconfigure(0, weight=1)
        conteneur_informations.rowconfigure(1, weight=1)
        conteneur_informations.rowconfigure(2, weight=1)
        conteneur_informations.columnconfigure(0, weight=1)
        conteneur_informations.grid(row=0, column=0, sticky="e")

        conteneur_prix_unitaire = Frame(conteneur_informations)
        conteneur_prix_unitaire.config(bg='skyblue')
        conteneur_prix_unitaire.rowconfigure(0, weight=1)
        conteneur_prix_unitaire.columnconfigure(0, weight=1)
        conteneur_prix_unitaire.columnconfigure(1, weight=1)
        conteneur_prix_unitaire.grid(row=0, column=0, pady=(20, 20), sticky="e")
        label_prix_unitaire = Label(conteneur_prix_unitaire, text="prix unitaire : ")
        label_prix_unitaire.config(bg='skyblue')
        label_prix_unitaire.grid(row=0, column=0, padx=(0, 15))
        self.str_prix_unitaire = tk.StringVar()
        self.str_prix_unitaire.set("")
        self.prix_unitaire = Entry(conteneur_prix_unitaire, textvariable=self.str_prix_unitaire, width=20)
        self.prix_unitaire.config(state="disabled")
        self.prix_unitaire.grid(row=0, column=1)

        conteneur_quantite = Frame(conteneur_informations)
        conteneur_quantite.config(bg='skyblue')
        conteneur_quantite.rowconfigure(0, weight=1)
        conteneur_quantite.columnconfigure(0, weight=1)
        conteneur_quantite.columnconfigure(1, weight=1)
        conteneur_quantite.grid(row=1, column=0, pady=(20, 20), sticky="e")
        label_quantite = Label(conteneur_quantite, text="quantité : ")
        label_quantite.config(bg='skyblue')
        label_quantite.grid(row=0, column=0, padx=(0, 15))
        self.quantite = Spinbox(conteneur_quantite, from_=1, to=10)
        self.quantite.config(state="disabled")
        self.quantite.grid(row=0, column=1)

        conteneur_montant_ht = Frame(conteneur_informations)
        conteneur_montant_ht.config(bg='skyblue')
        conteneur_montant_ht.rowconfigure(0, weight=1)
        conteneur_montant_ht.columnconfigure(0, weight=1)
        conteneur_montant_ht.columnconfigure(1, weight=1)
        conteneur_montant_ht.grid(row=2, column=0, pady=(20, 20), sticky="e")
        label_montant_ht = Label(conteneur_montant_ht, text="montant HT : ")
        label_montant_ht.config(bg='skyblue')
        label_montant_ht.grid(row=0, column=0, padx=(0, 15))
        self.str_montant_ht = tk.StringVar()
        self.str_montant_ht.set("")
        self.montant_ht = Entry(conteneur_montant_ht, textvariable=self.str_montant_ht, width=20)
        self.montant_ht.config(state="disabled")
        self.montant_ht.grid(row=0, column=1)

        conteneur_adherents = Frame(conteneur_formulaire_bas)
        conteneur_adherents.config(bg='skyblue')
        conteneur_adherents.rowconfigure(0, weight=1)
        conteneur_adherents.rowconfigure(1, weight=1)
        conteneur_adherents.columnconfigure(0, weight=1)
        conteneur_adherents.grid(row=0, column=1, sticky="nsew")

        self.adherents = tk.Listbox(conteneur_adherents, width=40)
        self.adherents.config(state='disabled')
        # self.actualiser_liste_adherents()
        self.adherents.grid(row=0, column=0)

        conteneur_informations_droite = tk.Frame(conteneur_formulaire_bas)
        conteneur_informations_droite.config(bg='skyblue')
        conteneur_informations_droite.rowconfigure(0, weight=1)
        conteneur_informations_droite.rowconfigure(1, weight=1)
        conteneur_informations_droite.columnconfigure(0, weight=1)
        conteneur_informations_droite.grid(row=0, column=2, sticky="nsew")

        conteneur_remarque = tk.Frame(conteneur_informations_droite)
        conteneur_remarque.config(bg='skyblue')
        conteneur_remarque.rowconfigure(0, weight=1)
        conteneur_remarque.rowconfigure(1, weight=1)
        conteneur_remarque.columnconfigure(0, weight=1)
        conteneur_remarque.grid(row=0, column=0)

        label_remarque = Label(conteneur_remarque, text=" remarque : ")
        label_remarque.config(bg='skyblue')
        label_remarque.grid(row=0, column=0, pady=(0, 15))
        self.remarque = tk.Text(conteneur_remarque, width=20, height=4)
        self.remarque.config(state="disabled")
        self.remarque.grid(row=1, column=0)

        self.ajouter = ttk.Button(conteneur_informations_droite, text="ajouter", style='my.TButton',
                                  command=lambda: ctrl_bon_commande.ajouter_informations_adherents_bon())
        self.ajouter.config(state='disabled')
        self.ajouter.grid(row=1, column=0)

        ligne_bas = Frame(self)
        ligne_bas.config(bg='skyblue')
        ligne_bas.rowconfigure(0, weight=1)
        ligne_bas.rowconfigure(1, weight=1)
        ligne_bas.columnconfigure(0, weight=1)
        ligne_bas.grid(row=2, column=0, columnspan=3, sticky="nsew")

        self.adherents_ajoutes = ttk.Treeview(ligne_bas,
                                              columns=(
                                              'designation', 'prix_unitaire', 'quantite', 'montant_HT', 'remarques'))
        self.adherents_ajoutes.heading('designation', text='Désignation')
        self.adherents_ajoutes.heading('prix_unitaire', text='Prix unitaire')
        self.adherents_ajoutes.heading('quantite', text='Quantité')
        self.adherents_ajoutes.heading('montant_HT', text='Montant HT')
        self.adherents_ajoutes.heading('remarques', text='Remarques')
        self.adherents_ajoutes['show'] = 'headings'
        self.adherents_ajoutes.grid(row=0, column=0)

        self.generer = ttk.Button(ligne_bas, text="générer bon de commande", style='my.TButton',
                                  command=lambda: ctrl_bon_commande.generer())
        self.generer.config(state='disabled')
        self.generer.grid(row=1, column=0)

    def actualiser_liste_adherents(self, liste):
        self.adherents.delete(0, END)
        cpt = 1
        for adherent in liste:
            self.adherents.insert(cpt, adherent)
            cpt += 1
        self.adherents.select_set(0)

    def actualiser_liste_organisations(self):
        self.organisations.delete(0, END)
        liste = self.ctrl_bon_commande.actualiser_liste_organisations_noms()
        self.organisations.insert(1, "indépendants")
        cpt = 2
        for organisation in liste:
            self.organisations.insert(cpt, organisation)
            cpt += 1
        self.organisations.select_set(0)

    def nombre_adherents_liste(self):
        return self.adherents.size()

    def champs_partie1_vides(self):
        est_vide = False
        if self.get_numero_bon() == "":
            est_vide = True
        if self.get_montant_total() == "":
            est_vide = True
        return est_vide

    def champs_partie2_vides(self):
        est_vide = False
        if self.get_montant_ht() == "":
            est_vide = True
        if self.get_quantite() == "":
            est_vide = True
        return est_vide

    def listbox_est_vide(self):
        return self.organisations.size() == 0

    def activer_champs_partie1(self):
        self.num_bon.config(state="normal")
        self.organisations.config(state="normal")
        self.montant_total.config(state="normal")
        self.nombre_adherents.config(state="normal")
        self.valider.config(state="normal")

    def desactiver_champs_partie1(self):
        self.num_bon.config(state="disabled")
        self.organisations.config(state="disabled")
        self.montant_total.config(state="disabled")
        self.nombre_adherents.config(state="disabled")
        self.valider.config(state="disabled")

    def activer_champs_partie2(self):
        self.prix_unitaire.config(state="normal")
        self.quantite.config(state="normal")
        self.montant_ht.config(state="normal")
        self.adherents.config(state="normal")
        self.remarque.config(state="normal")
        self.ajouter.config(state="normal")
        self.generer.config(state="normal")

    def activer_generer(self):
        self.generer.config(state="normal")

    def desactiver_generer(self):
        self.generer.config(state="disabled")

    def desactiver_champs_partie2(self):
        self.prix_unitaire.config(state="disabled")
        self.quantite.config(state="disabled")
        self.montant_ht.config(state="disabled")
        self.adherents.config(state="disabled")
        self.remarque.config(state="disabled")
        self.ajouter.config(state="disabled")
        self.generer.config(state="disabled")

    def vider_champs_partie2(self):
        self.str_prix_unitaire.set("")
        self.quantite.selection_to(0)
        self.str_montant_ht.set("")
        self.adherents.select_set(0)
        self.remarque.delete(1.0, END)

    def get_numero_bon(self):
        return self.num_bon.get()

    def get_destinataire(self):
        return self.organisations.get(ANCHOR)

    def get_montant_total(self):
        return self.montant_total.get()

    def get_nombre_adherents(self):
        return self.int_nombre.get()

    def get_montant_ht(self):
        return self.montant_ht.get()

    def get_quantite(self):
        return self.quantite.get()

    def get_prix_unitaire(self):
        return self.prix_unitaire.get()

    def get_remarque(self):
        return self.remarque.get("1.0", "end")[:-1]

    def get_adherent_selectionne(self):
        adherent = self.adherents.get(ANCHOR)
        self.adherents.delete(ANCHOR)
        return adherent

    def actualiser_liste_adherents_ajoutes(self, designation, prix_unitaire, quantite, montant_ht, remarque):
        self.adherents_ajoutes.insert('', 'end', designation, text=designation)
        self.adherents_ajoutes.set(designation, 'designation', designation)
        self.adherents_ajoutes.set(designation, 'prix_unitaire', prix_unitaire)
        self.adherents_ajoutes.set(designation, 'quantite', quantite)
        self.adherents_ajoutes.set(designation, 'montant_HT', montant_ht)
        self.adherents_ajoutes.set(designation, 'remarques', remarque)

    def effacer_informations(self):
        self.ctrl_bon_commande.nouveau_bon_de_commande()
        self.str_num.set("")
        self.str_montant_total.set("")
        self.nombre_adherents.selection_to(0)
        self.str_prix_unitaire.set("")
        self.str_montant_ht.set("")
        for i in self.adherents_ajoutes.get_children():
            self.adherents_ajoutes.delete(i)

    @staticmethod
    def get_fichier_path():
        filename = tk.filedialog.asksaveasfilename(defaultextension=".pdf")
        return filename

    @staticmethod
    def message_erreur_champs_vide():
        messagebox.showwarning(title="erreur de saisie", message="veuillez remplir tout les champs")

    @staticmethod
    def message_erreur_nombres_adherents():
        messagebox.showwarning(title="erreur de saisie", message="Il n'y a pas assez d'adhérents")

    @staticmethod
    def message_erreur_ajout_adherent():
        messagebox.showerror(title="erreur d'ajout", message="Vous ne pouvez pas ajouter plus d'adhérents")

class VueBilan(tk.Frame):

    def __init__(self, parent, ctrl_fenetre, ctrl_bilan):

        self.ctrlBilan = ctrl_bilan
        self.ctrlFenetre = ctrl_fenetre

        tk.Frame.__init__(self, parent)
        self.config(bg="skyblue")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # Bouton Accueil
        conteneur_bouton_accueil = tk.Frame(self)
        conteneur_bouton_accueil.config(bg="skyblue")
        # La grille est de 1 par 1
        conteneur_bouton_accueil.rowconfigure(0, weight=1)
        conteneur_bouton_accueil.columnconfigure(0, weight=1)
        # On place ce conteneur à la première case du conteneur ligne_haut
        conteneur_bouton_accueil.grid(row=0, column=0, sticky="nsew")

        logo_btn_accueil = tk.PhotoImage(file='vue/images/accueil.png')
        accueil = ttk.Button(conteneur_bouton_accueil, text="accueil", image=logo_btn_accueil, style='my.TButton',
                             compound="left", command=lambda: ctrl_fenetre.show_frame(Accueil))
        accueil.photo = logo_btn_accueil
        accueil.place(relx=0.5, rely=0.5, anchor=CENTER)

        titre = tk.Label(self, text="Gestion du bilan financier")
        titre.config(font=("Courier", 20), bg="skyblue")
        titre.grid(row=0, column=1, columnspan=2, sticky='nsew')

        conteneur_milieu_gauche = Frame(self)
        conteneur_milieu_gauche.config(bg='skyblue')
        conteneur_milieu_gauche.columnconfigure(0, weight=1)
        conteneur_milieu_gauche.rowconfigure(0, weight=1)
        conteneur_milieu_gauche.rowconfigure(1, weight=1)
        conteneur_milieu_gauche.rowconfigure(2, weight=1)
        conteneur_milieu_gauche.grid(row=1, column=0, sticky="nsew")

        formulaire = Frame(conteneur_milieu_gauche)
        formulaire.config(bg='skyblue')
        formulaire.columnconfigure(0, weight=1)
        formulaire.rowconfigure(0, weight=1)
        formulaire.rowconfigure(1, weight=1)
        formulaire.rowconfigure(2, weight=1)
        formulaire.rowconfigure(3, weight=1)
        formulaire.rowconfigure(4, weight=1)
        formulaire.rowconfigure(5, weight=1)
        formulaire.grid(row=1, column=1, sticky="nsew")

        conteneur_radio = Frame(formulaire)
        conteneur_radio.config(bg='skyblue')
        conteneur_radio.columnconfigure(0, weight=1)
        conteneur_radio.columnconfigure(1, weight=1)
        conteneur_radio.rowconfigure(0, weight=1)
        conteneur_radio.grid(row=0, column=0, sticky="nsew")

        self.choix = StringVar()
        self.choix.set("type")

        conteneur_categorie = Frame(formulaire)
        self.categorie = tk.Listbox(conteneur_categorie, width=20, height=3)

        self.radio1 = Radiobutton(conteneur_radio, takefocus=0, variable=self.choix, text="dépense",
                                  value="depense", tristatevalue=0, highlightthickness=0, command=lambda: self.actualiser_liste_categorie('depense'))
        self.radio1.config(bg='skyblue', activebackground='skyblue')
        self.radio1.grid(row=0, column=0, sticky="nsew")
        self.radio1.invoke()

        self.radio2 = Radiobutton(conteneur_radio, variable=self.choix, takefocus=0, text="recette",
                                  value="recette", tristatevalue=0, highlightthickness=0, command=lambda: self.actualiser_liste_categorie('recette'))
        self.radio2.config(bg='skyblue', activebackground='skyblue')
        self.radio2.grid(row=0, column=1, sticky="nsew")


        conteneur_categorie.config(bg='skyblue')
        conteneur_categorie.columnconfigure(0, weight=1)
        conteneur_categorie.columnconfigure(1, weight=1)
        conteneur_categorie.columnconfigure(2, weight=1)
        conteneur_categorie.rowconfigure(0, weight=1)
        conteneur_categorie.grid(row=4, column=0, sticky="nsew")

        lcategorie = Label(conteneur_categorie, text="categorie :")
        lcategorie.config(bg='skyblue')
        lcategorie.grid(row=0, column=0, padx=(0, 15))
        self.actualiser_liste_categorie('depense')
        self.categorie.grid(row=0, column=1)

        scrollbar = ttk.Scrollbar(conteneur_categorie)
        scrollbar.grid(row=0, column=2)
        self.categorie.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.categorie.yview)

        conteneur_date = Frame(formulaire)
        conteneur_date.config(bg='skyblue')
        conteneur_date.columnconfigure(0, weight=1)
        conteneur_date.columnconfigure(1, weight=1)
        conteneur_date.rowconfigure(0, weight=1)
        conteneur_date.grid(row=1, column=0, sticky="nsew")

        ldate = Label(conteneur_date, text="date :")
        ldate.config(bg='skyblue')
        ldate.grid(row=0, column=0, padx=(0, 15))
        self.str_date = tk.StringVar()
        self.str_date.set("")
        self.date = Entry(conteneur_date, textvariable=self.str_date, width=20)
        self.date.grid(row=0, column=1)

        conteneur_montant = Frame(formulaire)
        conteneur_montant.config(bg='skyblue')
        conteneur_montant.columnconfigure(0, weight=1)
        conteneur_montant.columnconfigure(1, weight=1)
        conteneur_montant.rowconfigure(0, weight=1)
        conteneur_montant.grid(row=2, column=0, sticky="nsew")

        lmontant = Label(conteneur_montant, text="montant :")
        lmontant.config(bg='skyblue')
        lmontant.grid(row=0, column=0, padx=(0, 15))
        self.str_montant = tk.StringVar()
        self.str_montant.set("")
        self.montant = Entry(conteneur_montant, textvariable=self.str_montant, width=20)
        self.montant.grid(row=0, column=1)


        conteneur_description = Frame(formulaire)
        conteneur_description.config(bg='skyblue')
        conteneur_description.columnconfigure(0, weight=1)
        conteneur_description.columnconfigure(1, weight=1)
        conteneur_description.rowconfigure(0, weight=1)
        conteneur_description.grid(row=3, column=0, sticky="nsew")

        ldescription = Label(conteneur_description, text="description :")
        ldescription.config(bg='skyblue')
        ldescription.grid(row=0, column=0, padx=(0, 15))
        self.str_description = tk.StringVar()
        self.str_description.set("")
        self.description = Entry(conteneur_description, textvariable=self.str_description, width=20)
        self.description.grid(row=0, column=1)

        ajouter = ttk.Button(formulaire, text="ajouter opération", style='my.TButton',
                             command=lambda: ctrl_bilan.ajouter_operation())
        ajouter.grid(row=5, column=0)

        conteneur_milieu = Frame(self)
        conteneur_milieu.config(bg='skyblue')
        conteneur_milieu.rowconfigure(0, weight=1)
        conteneur_milieu.rowconfigure(1, weight=1)
        conteneur_milieu.columnconfigure(0, weight=1)
        conteneur_milieu.grid(row=1, column=1, sticky="nsew")

        conteneur_depenses = Frame(conteneur_milieu)
        conteneur_depenses.config(bg='skyblue')
        conteneur_depenses.rowconfigure(0, weight=1)
        conteneur_depenses.rowconfigure(1, weight=1)
        conteneur_depenses.columnconfigure(0, weight=1)
        conteneur_depenses.columnconfigure(1, weight=1)
        conteneur_depenses.grid(row=0, column=0, sticky="nsew")

        ldepenses = Label(conteneur_depenses, text="Dépenses")
        ldepenses.config(bg='skyblue')
        ldepenses.grid(row=0, column=0, columnspan=2, padx=(0, 15))
        self.depenses = tk.Listbox(conteneur_depenses, width=60)
        self.actualiser_liste_depenses()
        self.depenses.grid(row=1, column=0, sticky="ens")

        scrollbar = ttk.Scrollbar(conteneur_depenses)
        scrollbar.grid(row=1, column=1, sticky="wns")
        self.depenses.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.depenses.yview)

        conteneur_supprimer = tk.Frame(conteneur_milieu)
        conteneur_supprimer.config(bg='skyblue')
        conteneur_supprimer.rowconfigure(0, weight=1)
        conteneur_supprimer.columnconfigure(0, weight=1)
        conteneur_supprimer.columnconfigure(1, weight=1)
        conteneur_supprimer.grid(row=1, column=0)

        supprimer = ttk.Button(conteneur_supprimer, text="supprimer dépense", style='my.TButton',
                               command=lambda: ctrl_bilan.supprimer_operation('depense'))
        supprimer.grid(row=0, column=0, padx=(0, 15))

        modifier = ttk.Button(conteneur_supprimer, text="modifier depense", style='my.TButton',
                              command=lambda: ctrl_bilan.modifier_operation('depense'))
        modifier.grid(row=0, column=1, padx=(0, 15))

        conteneur_droite = Frame(self)
        conteneur_droite.config(bg='skyblue')
        conteneur_droite.rowconfigure(0, weight=1)
        conteneur_droite.rowconfigure(1, weight=1)
        conteneur_droite.columnconfigure(0, weight=1)
        conteneur_droite.grid(row=1, column=2, sticky="nsew")

        conteneur_recettes = Frame(conteneur_droite)
        conteneur_recettes.config(bg='skyblue')
        conteneur_recettes.rowconfigure(0, weight=1)
        conteneur_recettes.rowconfigure(1, weight=1)
        conteneur_recettes.columnconfigure(0, weight=1)
        conteneur_recettes.columnconfigure(1, weight=1)
        conteneur_recettes.grid(row=0, column=0, sticky="nsew")

        lrecettes = Label(conteneur_recettes, text="Recettes")
        lrecettes.config(bg='skyblue')
        lrecettes.grid(row=0, column=0, columnspan=2, padx=(0, 15))
        self.recettes = tk.Listbox(conteneur_recettes, width=60)
        self.actualiser_liste_recettes()
        self.recettes.grid(row=1, column=0, sticky="ens")

        scrollbar = ttk.Scrollbar(conteneur_recettes)
        scrollbar.grid(row=1, column=1, sticky="wns")
        self.recettes.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.recettes.yview)

        conteneur_supprimer = tk.Frame(conteneur_droite)
        conteneur_supprimer.config(bg='skyblue')
        conteneur_supprimer.rowconfigure(0, weight=1)
        conteneur_supprimer.columnconfigure(0, weight=1)
        conteneur_supprimer.columnconfigure(1, weight=1)
        conteneur_supprimer.grid(row=1, column=0)

        supprimer = ttk.Button(conteneur_supprimer, text="supprimer recette", style='my.TButton',
                               command=lambda: ctrl_bilan.supprimer_operation('recette'))
        supprimer.grid(row=0, column=0, padx=(0, 15))

        modifier = ttk.Button(conteneur_supprimer, text="modifier recette", style='my.TButton',
                              command=lambda: ctrl_bilan.modifier_operation('recette'))
        modifier.grid(row=0, column=1, padx=(0, 15))

        conteneur_bas_milieu = Frame(self)
        conteneur_bas_milieu.config(bg='skyblue')
        conteneur_bas_milieu.rowconfigure(0, weight=1)
        conteneur_bas_milieu.rowconfigure(1, weight=1)
        conteneur_bas_milieu.columnconfigure(0, weight=1)
        conteneur_bas_milieu.grid(row=2, column=1, sticky="nsew")

        conteneur_categories = tk.Frame(conteneur_bas_milieu)
        conteneur_categories.config(bg='skyblue')
        conteneur_categories.rowconfigure(0, weight=1)
        conteneur_categories.columnconfigure(0, weight=1)
        conteneur_categories.columnconfigure(1, weight=1)
        conteneur_categories.grid(row=0, column=0)

        categories = ttk.Button(conteneur_categories, text="Gestion & Résumé catégories", style='my.TButton',
                               command=lambda: ctrl_fenetre.show_frame(VueBilan_categories))
        categories.grid(row=0, column=0, padx=(0, 15))

    def actualiser_liste_recettes(self):
        self.recettes.delete(0, END)
        liste = self.ctrlBilan.actualiser_liste_recettes()
        cpt = 1
        for operation in liste:
            self.recettes.insert(cpt, operation)
            cpt += 1
        self.recettes.select_set(0)

    def actualiser_liste_depenses(self):
        self.depenses.delete(0, END)
        liste = self.ctrlBilan.actualiser_liste_depenses()
        cpt = 1
        for operation in liste:
            self.depenses.insert(cpt, operation)
            cpt += 1
        self.depenses.select_set(0)

    def actualiser_liste_categorie(self, type):
        self.categorie.delete(0, END)
        liste = self.ctrlBilan.actualiser_liste_categorie(type)
        cpt = 1
        for categorie1 in liste:
            self.categorie.insert(cpt, categorie1)
            cpt += 1
        self.categorie.select_set(0)

    def get_categorie(self):
        return self.categorie.get(ANCHOR)

    def get_montant(self):
        return self.montant.get()

    def get_choix_selectionne(self):
        return self.choix.get()

    def get_date(self):
        return self.date.get()

    def get_description(self):
        return self.description.get()

    def get_selected_operation(self, type):
        if type == 'recette' and self.recettes.get(ANCHOR) is not None:
            return self.recettes.get(ANCHOR)
        elif type == 'depense' and self.depenses.get(ANCHOR) is not None:
            return self.depenses.get(ANCHOR)
        else:
            self.message_erreur_suppression()

    def viderChamps(self):
        self.str_date.set("")
        self.str_montant.set("")
        self.str_description.set("")

    def champ_vide(self):
        est_vide = False
        if self.categorie.get(ANCHOR) is None:
            est_vide = True
        if self.get_choix_selectionne() == "":
            est_vide = True
        if self.get_date() == "":
            est_vide = True
        if self.get_montant() == "":
            est_vide = True
        return est_vide

    def validation_date(self, date):
        chiffres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if len(date) == 10:
            for i in range(9):
                if i == 2 or i == 5:
                    if date[i] != '/':
                        return False
                elif not chiffres.__contains__(date[i]):
                    return False
            if date[0] == '0' and date[1] == '0':
                return False
            elif date[0] == '3' and date[1] > '1':
                return False
            if date[3] == '0' and date[4] == '0':
                return False
            elif date[3] == '1' and date[4] > '2':
                return False
        else:
            return False
        return True

    def validation_montant(self, montant):
        if montant[-3] != '.':
            return False
        try:
            float(montant)
        except ValueError:
            return False
        return True

    @staticmethod
    def message_erreur_suppression():
        messagebox.showerror(title="erreur de suppression", message="Il n'y a plus d'opération")

    @staticmethod
    def message_erreur_champs_vide():
        messagebox.showwarning(title="erreur de saisie", message="veuillez remplir tous les champs")

    @staticmethod
    def message_erreur_choix_vide():
        messagebox.showwarning(title="erreur de saisie", message="veuillez selectionner une catégorie")

    @staticmethod
    def message_erreur_validation():
        messagebox.showerror(title="erreur de validité", message="le format de l'opération n'est pas conforme")

    @staticmethod
    def message_erreur_ajout():
        messagebox.showerror(title="erreur d'ajout", message="l'opération n'a pas pu être créée")

class VueBilan_categories(tk.Frame):

    def __init__(self, parent, ctrl_fenetre, ctrl_bilan):

        self.ctrlBilan = ctrl_bilan

        tk.Frame.__init__(self, parent)
        self.config(bg="skyblue")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        conteneur_bouton_retour = tk.Frame(self)
        conteneur_bouton_retour.config(bg="skyblue")
        conteneur_bouton_retour.rowconfigure(0, weight=1)
        conteneur_bouton_retour.columnconfigure(0, weight=1)
        conteneur_bouton_retour.grid(row=0, column=0, sticky="nsew")

        retour = ttk.Button(conteneur_bouton_retour, text="retour", style='my.TButton',
                            compound="left", command=lambda: ctrl_fenetre.show_frame(VueBilan))
        retour.place(relx=0.5, rely=0.5, anchor=CENTER)

        titre = tk.Label(self, text="Gestion des catégories")
        titre.config(font=("Courier", 20), bg="skyblue")
        titre.grid(row=0, column=1, columnspan=2, sticky='nsew')

        conteneur_gauche = Frame(self)
        conteneur_gauche.config(bg='skyblue')
        conteneur_gauche.columnconfigure(0, weight=1)
        conteneur_gauche.rowconfigure(0, weight=1)
        conteneur_gauche.grid(row=1, column=0, sticky="nsew")

        formulaire = Frame(conteneur_gauche)
        formulaire.config(bg='skyblue')
        formulaire.columnconfigure(0, weight=1)
        formulaire.rowconfigure(0, weight=1)
        formulaire.rowconfigure(1, weight=1)
        formulaire.rowconfigure(2, weight=1)
        formulaire.grid(row=0, column=0, sticky="nsew")

        conteneur_radio = Frame(formulaire)
        conteneur_radio.config(bg='skyblue')
        conteneur_radio.columnconfigure(0, weight=1)
        conteneur_radio.columnconfigure(1, weight=1)
        conteneur_radio.rowconfigure(0, weight=1)
        conteneur_radio.grid(row=0, column=0, sticky="nsew")

        self.choix = StringVar()
        self.choix.set("type")

        self.radio1 = Radiobutton(conteneur_radio, takefocus=0, variable=self.choix, text="dépense",
                                  value="depense", tristatevalue=0, highlightthickness=0)
        self.radio1.config(bg='skyblue', activebackground='skyblue')
        self.radio1.grid(row=0, column=0, sticky="nsew")

        self.radio2 = Radiobutton(conteneur_radio, variable=self.choix, takefocus=0, text="recette",
                                  value="recette", tristatevalue=0, highlightthickness=0)
        self.radio2.config(bg='skyblue', activebackground='skyblue')
        self.radio2.grid(row=0, column=1, sticky="nsew")

        conteneur_categorie = Frame(formulaire)
        conteneur_categorie.config(bg='skyblue')
        conteneur_categorie.columnconfigure(0, weight=1)
        conteneur_categorie.columnconfigure(1, weight=1)
        conteneur_categorie.rowconfigure(0, weight=1)
        conteneur_categorie.grid(row=1, column=0, sticky="nsew")

        lcategorie = Label(conteneur_categorie, text="nom de categorie :")
        lcategorie.config(bg='skyblue')
        lcategorie.grid(row=0, column=0, padx=(0, 15))
        self.str_categorie = tk.StringVar()
        self.str_categorie.set("")
        self.categorie = Entry(conteneur_categorie, textvariable=self.str_categorie, width=20)
        self.categorie.grid(row=0, column=1)

        conteneur_ajouter = tk.Frame(formulaire)
        conteneur_ajouter.config(bg='skyblue')
        conteneur_ajouter.rowconfigure(0, weight=1)
        conteneur_ajouter.columnconfigure(0, weight=1)
        conteneur_ajouter.columnconfigure(1, weight=1)
        conteneur_ajouter.grid(row=2, column=0)

        ajouter = ttk.Button(conteneur_ajouter, text="Ajouter catégorie", style='my.TButton',
                               command=lambda: ctrl_bilan.ajouter_categorie())
        ajouter.grid(row=0, column=0, padx=(0, 15))

        conteneur_milieu = Frame(self)
        conteneur_milieu.config(bg='skyblue')
        conteneur_milieu.columnconfigure(0, weight=1)
        conteneur_milieu.rowconfigure(0, weight=1)
        conteneur_milieu.rowconfigure(1, weight=1)
        conteneur_milieu.rowconfigure(2, weight=1)
        conteneur_milieu.grid(row=1, column=1, sticky="nsew")

        lcategorie = Label(conteneur_milieu, text="Catégories")
        lcategorie.config(bg='skyblue')
        lcategorie.grid(row=0, column=0, columnspan=2, padx=(0, 15))
        self.categories = tk.Listbox(conteneur_milieu, width=60)
        self.actualiser_liste_categories()
        self.categories.grid(row=1, column=0, sticky="ens")

        scrollbar = ttk.Scrollbar(conteneur_milieu)
        scrollbar.grid(row=1, column=1, sticky="wns")
        self.categories.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.categories.yview)

        conteneur_supprimer = tk.Frame(conteneur_milieu)
        conteneur_supprimer.config(bg='skyblue')
        conteneur_supprimer.rowconfigure(0, weight=1)
        conteneur_supprimer.columnconfigure(0, weight=1)
        conteneur_supprimer.columnconfigure(1, weight=1)
        conteneur_supprimer.grid(row=2, column=0)

        supprimer = ttk.Button(conteneur_supprimer, text="Supprimer catégorie", style='my.TButton',
                             command=lambda: ctrl_bilan.supprimer_categorie())
        supprimer.grid(row=0, column=0, padx=(0, 15))

    def actualiser_liste_categories(self):
        self.categories.delete(0, END)
        liste = self.ctrlBilan.actualiser_liste_categories()
        cpt = 1
        for categorie in liste:
            self.categories.insert(cpt, categorie)
            cpt += 1
        self.categories.select_set(0)

    def get_type(self):
        return self.choix.get()

    def get_categorie(self):
        return self.categorie.get()

    def get_categorie_selectionner(self):
        categorie1 = self.categories.get(ANCHOR)

        return categorie1

    def champ_vide(self):
        if self.categorie.get() == "":
            return True
        elif self.choix.get() == "":
            return True
        else:
            return False

    def viderChamps(self):
        self.str_categorie.set("")

    @staticmethod
    def message_erreur_suppression():
        messagebox.showerror(title="erreur de suppression", message="Il n'y a plus de catégorie")

    @staticmethod
    def message_erreur_champs_vide():
        messagebox.showwarning(title="erreur de saisie", message="veuillez remplir tous les champs")

    @staticmethod
    def message_erreur_choix_vide():
        messagebox.showwarning(title="erreur de saisie", message="veuillez selectionner une catégorie")

    @staticmethod
    def message_erreur_ajout():
        messagebox.showerror(title="erreur d'ajout", message="la catégorie n'a pas pu être créée")