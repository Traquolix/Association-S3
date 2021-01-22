from data.StockageAdherentCsv import StockageAdherentCsv
from data.StockageOrganisationCsv import StockageOrganisationCsv
from modele.BonDeCommande import BonDeCommande
from modele.GenererBonDeCommande import GenererBonDeCommande


class ControleurBonDeCommande:

    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.adherents_csv = StockageAdherentCsv()
        self.organisations_csv = StockageOrganisationCsv()
        self.generateur_bon_de_commande = GenererBonDeCommande()
        self.vue_bon_commande = None
        self.bon_de_commande = None

    def nouveau_bon_de_commande(self):
        self.bon_de_commande = BonDeCommande()
        self.vue_bon_commande.activer_champs_partie1()
        self.vue_bon_commande.desactiver_champs_partie2()
        self.vue_bon_commande.desactiver_generer()

    def set_vue_bon_commande(self, vue_bon_commande):
        self.vue_bon_commande = vue_bon_commande

    def valider_informations_generales_bon(self):
        if self.vue_bon_commande.champs_partie1_vides():
            self.vue_bon_commande.message_erreur_champs_vide()
        else:
            numero_bon = self.vue_bon_commande.get_numero_bon()
            destinataire = self.vue_bon_commande.get_destinataire()
            montant_total = self.vue_bon_commande.get_montant_total()
            nombre_adherents = self.vue_bon_commande.get_nombre_adherents()
            if len(self.actualiser_liste_adherents_independants_nom()) < nombre_adherents and destinataire == "indépendants":
                self.vue_bon_commande.message_erreur_nombres_adherents()
            elif len(self.actualiser_liste_adherents_noms(destinataire)) < nombre_adherents and destinataire != "indépendants":
                self.vue_bon_commande.message_erreur_nombres_adherents()
            else:
                self.nouveau_bon_de_commande()
                self.bon_de_commande.set_numero_bon(numero_bon)
                self.bon_de_commande.set_montant_total(montant_total)
                if destinataire != "indépendants":
                    self.bon_de_commande.set_nom_organisation(destinataire)
                    self.bon_de_commande.set_adresse_organisation(self.organisations_csv.get_adresse(destinataire))
                    self.bon_de_commande.set_ville_organisation(self.organisations_csv.get_ville(destinataire))
                else :
                    self.bon_de_commande.set_nom_organisation("indépendants")
                self.vue_bon_commande.activer_champs_partie2()
                self.vue_bon_commande.desactiver_champs_partie1()

                if destinataire == "indépendants":
                    liste = self.actualiser_liste_adherents_independants_nom()
                else:
                    liste = self.actualiser_liste_adherents_noms(destinataire)
                self.vue_bon_commande.actualiser_liste_adherents(liste)

    def ajouter_informations_adherents_bon(self):
        if self.bon_de_commande.get_nombre_ajoute() == self.vue_bon_commande.get_nombre_adherents():
            self.vue_bon_commande.message_erreur_ajout_adherent()
        elif self.vue_bon_commande.champs_partie2_vides():
            self.vue_bon_commande.message_erreur_champs_vide()
        else:
            if self.bon_de_commande.get_nombre_ajoute() == self.vue_bon_commande.get_nombre_adherents() - 1:
                self.vue_bon_commande.activer_generer()
            designation = self.vue_bon_commande.get_adherent_selectionne()
            prix_unitaire = self.vue_bon_commande.get_prix_unitaire()
            montant_ht = self.vue_bon_commande.get_montant_ht()
            quantite = self.vue_bon_commande.get_quantite()
            remarque = self.vue_bon_commande.get_remarque()
            if self.bon_de_commande.get_nom_organisation() == "indépendants":
                self.bon_de_commande.set_nom_organisation(str(designation[0] + " " + designation[1]))
                self.bon_de_commande.set_ville_organisation(self.adherents_csv.get_ville_independant(designation))
                self.bon_de_commande.set_adresse_organisation(self.adherents_csv.get_adresse_independant(designation))
            self.bon_de_commande.ajouter_adherent(designation, prix_unitaire, quantite, montant_ht, remarque)
            self.vue_bon_commande.actualiser_liste_adherents_ajoutes(designation, prix_unitaire, quantite, montant_ht, remarque)
            self.vue_bon_commande.vider_champs_partie2()

    def generer(self):
        path = self.vue_bon_commande.get_fichier_path()
        self.generateur_bon_de_commande.genererBonDeCommande(path, self.bon_de_commande)
        self.vue_bon_commande.effacer_informations()

    def actualiser_liste_adherents_noms(self, nom_organisation):
        return sorted(self.adherents_csv.lire_fichier_organisations(nom_organisation))

    def actualiser_liste_adherents_independants_nom(self):
        return sorted(self.adherents_csv.lire_fichier_noms_independants())

    def actualiser_liste_organisations_noms(self):
        return sorted(self.organisations_csv.lire_fichier_noms())
