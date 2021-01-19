from data.StockageOrganisationCsv import StockageOrganisationCsv
from data.StockageAdherentCsv import StockageAdherentCsv
from modele.Organisation import Organisation
from modele.Adherent import Adherent


class ControleurAdherents:

    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.adherents_csv = StockageAdherentCsv()
        self.organisations_csv = StockageOrganisationCsv()
        self.vue_adherents = None
        self.vue_organisations = None
        self.vue_bon_commande = None

    def set_vue_adherents(self, vue_adherents):
        self.vue_adherents = vue_adherents

    def set_vue_organisations(self, vue_organisations):
        self.vue_organisations = vue_organisations

    def set_vue_bon_commande(self, vue_bon_commande):
        self.vue_bon_commande = vue_bon_commande

    def actualiser_liste_adherents(self):
        return sorted(self.adherents_csv.lire_fichier_complets())

    def ajouter_adherent(self):
        if self.vue_adherents.champ_vide():
            self.vue_adherents.message_erreur_champs_vide()
        elif self.vue_adherents.listbox_organisations_est_vide():
            self.vue_adherents.message_erreur_labo_vide()
        else:
            prenom = self.vue_adherents.get_prenom()
            nom = self.vue_adherents.get_nom()
            orga = self.vue_adherents.get_organisation()
            adherent = Adherent()
            adherent.set_prenom(prenom)
            adherent.set_nom(nom)
            adherent.set_organisation(orga)
            if not self.adherents_csv.contient_adherent(adherent):
                self.adherents_csv.ajouter_adherent(adherent)
                self.vue_adherents.actualiser_liste_adherents()
                self.vue_adherents.viderChamps()
            else:
                self.vue_adherents.message_erreur_ajout()

    def supprimer_adherent(self):
        if not self.vue_adherents.listbox_adherent_est_vide():
            a = self.vue_adherents.get_selected_adherent()
            adherent = Adherent()
            adherent.set_prenom(a[0])
            adherent.set_nom(a[1])
            adherent.set_organisation(a[2])
            self.adherents_csv.supprimer_adherent(adherent)
            self.vue_adherents.actualiser_liste_adherents()
        else:
            self.vue_adherents.message_erreur_suppression()

    def supprimer_tout_adherents(self):
        if not self.vue_adherents.listbox_adherent_est_vide():
            self.adherents_csv.initialiser_fichier()
            self.vue_adherents.actualiser_liste_adherents()
        else:
            self.vue_adherents.message_erreur_suppression()

    def ajouter_organisation(self):
        if self.vue_organisations.champ_vide():
            self.vue_organisations.message_erreur_champs_vide()
        else:
            nom = self.vue_organisations.get_nom()
            adresse = self.vue_organisations.get_adresse()
            ville = self.vue_organisations.get_ville()
            organisation = Organisation()
            organisation.set_nom(nom)
            organisation.set_adresse(adresse)
            organisation.set_ville(ville)
            if not self.organisations_csv.contient_laboratoire(organisation):
                self.organisations_csv.ajouter_laboratoire(organisation)
                self.vue_organisations.actualiser_liste_organisations()
                self.vue_adherents.actualiser_liste_organisations()
                self.vue_bon_commande.actualiser_liste_organisations()
                self.vue_organisations.viderChamps()
            else:
                self.vue_organisations.message_erreur_ajout()

    def supprimer_laboratoire(self):
        if not self.vue_organisations.listbox_organisations_est_vide():
            l = self.vue_organisations.get_selected_organisation()
            laboratoire = Laboratoire()
            laboratoire.set_nom(l[0])
            laboratoire.set_adresse(l[1])
            laboratoire.set_ville(l[2])
            self.organisations_csv.supprimer_laboratoire(laboratoire)
            self.vue_adherents.actualiser_liste_organisations()
            self.vue_organisations.actualiser_liste_organisations()
            self.vue_bon_commande.actualiser_liste_organisations()
        else:
            self.vue_organisations.message_erreur_suppression()

    def supprimer_tout_organisations(self):
        if not self.vue_organisations.listbox_organisations_est_vide():
            self.organisations_csv.initialiser_fichier()
            self.vue_organisations.actualiser_liste_organisations()
        else:
            self.vue_organisations.message_erreur_suppression()

    def actualiser_liste_organisations_noms(self):
        return sorted(self.organisations_csv.lire_fichier_noms())

    def actualiser_liste_organisations_complets(self):
        return sorted(self.organisations_csv.lire_fichier_complets())
