from data.StockageOrganisationCsv import StockageOrganisationCsv
from data.StockageAdherentCsv import StockageAdherentCsv
from modele.Organisation import Organisation
from modele.Adherent import Adherent
from modele.AdherentIndependant import AdherentIndependant


class ControleurAdherents:

    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.adherents_csv = StockageAdherentCsv()
        self.organisations_csv = StockageOrganisationCsv()
        self.vue_adherents = None
        self.vue_organisations = None
        self.vue_bon_commande = None
        self.vue_facture = None

    def set_vue_adherents(self, vue_adherents):
        self.vue_adherents = vue_adherents

    def set_vue_organisations(self, vue_organisations):
        self.vue_organisations = vue_organisations

    def set_vue_bon_commande(self, vue_bon_commande):
        self.vue_bon_commande = vue_bon_commande

    def set_vue_facture(self, vue_facture):
        self.vue_facture = vue_facture

    def actualiser_liste_adherents(self):
        return sorted(self.adherents_csv.lire_fichier_complets())

    def actualiser_liste_adherents_independants(self):
        return sorted(self.adherents_csv.lire_fichier_complets_independants())

    def ajouter_adherent(self):
        if self.vue_adherents.champ_vide():
            self.vue_adherents.message_erreur_champs_vide()
        elif self.vue_adherents.listbox_organisations_est_vide():
            self.vue_adherents.message_erreur_organisation_vide()
        else:
            if self.vue_adherents.get_choix_selectionne() == "organisation":
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

            if self.vue_adherents.get_choix_selectionne() == "indépendant":
                prenom = self.vue_adherents.get_prenom()
                nom = self.vue_adherents.get_nom()
                adresse = self.vue_adherents.get_adresse()
                ville = self.vue_adherents.get_ville()
                adherent = AdherentIndependant()
                adherent.set_prenom(prenom)
                adherent.set_nom(nom)
                adherent.set_adresse(adresse)
                adherent.set_ville(ville)
                if not self.adherents_csv.contient_adherent_independant(adherent):
                    self.adherents_csv.ajouter_adherent_independant(adherent)
                    self.vue_adherents.actualiser_liste_adherents()
                    self.vue_adherents.viderChamps()
                else:
                    self.vue_adherents.message_erreur_ajout()

    def supprimer_adherent(self):
        if not self.vue_adherents.listbox_adherent_est_vide():
            ligne = self.vue_adherents.get_selected_adherent()
            if len(ligne) == 3:
                adherent = Adherent()
                adherent.set_prenom(ligne[0])
                adherent.set_nom(ligne[1])
                adherent.set_organisation(ligne[2])
                self.adherents_csv.supprimer_adherent(adherent)
                self.vue_adherents.actualiser_liste_adherents()
            elif len(ligne) == 4:
                adherent = AdherentIndependant()
                adherent.set_prenom(ligne[0])
                adherent.set_nom(ligne[1])
                adherent.set_adresse((ligne[2]))
                adherent.set_ville(ligne[3])
                self.adherents_csv.supprimer_adherent_independant(adherent)
                self.vue_adherents.actualiser_liste_adherents()
        else:
            self.vue_adherents.message_erreur_suppression()

    def supprimer_tout_adherents(self):
        if not self.vue_adherents.listbox_adherent_est_vide():
            self.adherents_csv.initialiser_fichier()
            self.adherents_csv.initialiser_fichier_independants()
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
            if not self.organisations_csv.contient_organisation(organisation):
                self.organisations_csv.ajouter_organisation(organisation)
                self.vue_organisations.actualiser_liste_organisations()
                self.vue_adherents.actualiser_liste_organisations()
                self.vue_bon_commande.actualiser_liste_organisations()
                self.vue_facture.actualiser_liste_organisations()
                self.vue_organisations.viderChamps()
            else:
                self.vue_organisations.message_erreur_ajout()

    def supprimer_organisation(self):
        if not self.vue_organisations.listbox_organisations_est_vide():
            ligne = self.vue_organisations.get_selected_organisation()
            organisation = Organisation()
            organisation.set_nom(ligne[0])
            organisation.set_adresse(ligne[1])
            organisation.set_ville(ligne[2])
            self.organisations_csv.supprimer_organisation(organisation)
            self.vue_adherents.actualiser_liste_organisations()
            self.vue_organisations.actualiser_liste_organisations()
            self.vue_bon_commande.actualiser_liste_organisations()
            self.vue_facture.actualiser_liste_organisations()

        else:
            self.vue_organisations.message_erreur_suppression()

    def supprimer_tout_organisations(self):
        if not self.vue_organisations.listbox_organisations_est_vide():
            self.organisations_csv.initialiser_fichier()
            self.vue_organisations.actualiser_liste_organisations()
            self.vue_adherents.actualiser_liste_organisations()
            self.vue_bon_commande.actualiser_liste_organisations()
        else:
            self.vue_organisations.message_erreur_suppression()

    def actualiser_liste_organisations_noms(self):
        return sorted(self.organisations_csv.lire_fichier_noms())

    def actualiser_liste_organisations_complets(self):
        return sorted(self.organisations_csv.lire_fichier_complets())
