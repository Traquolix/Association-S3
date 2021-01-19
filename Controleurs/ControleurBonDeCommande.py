from data.StockageAdherentCsv import StockageAdherentCsv
from data.StockageOrganisationCsv import StockageOrganisationCsv
from modele.BonDeCommande import BonDeCommande
from modele.GenererBonDeCommande import GenererBonDeCommande


class ControleurBonDeCommande:

    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.adherents_csv = StockageAdherentCsv()
        self.laboratoire_csv = StockageOrganisationCsv()
        self.generateur_bon_de_commande = GenererBonDeCommande()
        self.vue_bon_commande = None
        self.bon_de_commande = None

    def nouveau_bon_de_commande(self, nb):
        self.bon_de_commande = BonDeCommande(nb)

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
            if len(self.actualiser_liste_adherents_noms(destinataire)) < nombre_adherents:
                self.vue_bon_commande.message_erreur_nombres_adherents()
            else:
                self.nouveau_bon_de_commande(nombre_adherents)
                self.bon_de_commande.set_numero_bon(numero_bon)
                self.bon_de_commande.set_montant_total(montant_total)
                self.bon_de_commande.set_nom_labo(destinataire)
                self.bon_de_commande.set_adresse_labo(self.laboratoire_csv.get_adresse(destinataire))
                self.bon_de_commande.set_ville_labo(self.laboratoire_csv.get_ville(destinataire))

                self.vue_bon_commande.activer_champs_partie2()
                self.vue_bon_commande.desactiver_champs_partie1()
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
            self.bon_de_commande.ajouter_adherent(designation, prix_unitaire, quantite, montant_ht, remarque)
            self.vue_bon_commande.actualiser_liste_adherents_ajoutes(designation, prix_unitaire, quantite, montant_ht, remarque)
            self.vue_bon_commande.vider_champs_partie2()

    def generer(self):
        print(self.bon_de_commande)
        path = self.vue_bon_commande.get_fichier_path()
        # self.generateur_bon_de_commande.genererBonDeCommande(path, self.bon_de_commande)

    def actualiser_liste_adherents_noms(self, nom_labo):
        return sorted(self.adherents_csv.lire_fichier_labo(nom_labo))

    def actualiser_liste_laboratoire_noms(self):
        return sorted(self.laboratoire_csv.lire_fichier_noms())
