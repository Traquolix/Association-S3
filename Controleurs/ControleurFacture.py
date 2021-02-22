from data.StockageAdherentCsv import StockageAdherentCsv
from data.StockageOrganisationCsv import StockageOrganisationCsv
from modele.Facture import Facture
from modele.GenererFacture import GenererFacture


class ControleurFacture:

    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.adherents_csv = StockageAdherentCsv()
        self.organisations_csv = StockageOrganisationCsv()
        self.vue_facture = None
        self.facture = None
        self.generateur_facture = GenererFacture()

    def nouvelle_facture(self):
        self.facture = Facture()
        self.vue_facture.activer_champs_partie1()
        self.vue_facture.desactiver_champs_partie2()
        self.vue_facture.desactiver_generer()

    def set_vue_facture(self, vue_facture):
        self.vue_facture = vue_facture

    def valider_informations_generales_facture(self):
        if self.vue_facture.champs_partie1_vides():
            self.vue_facture.message_erreur_champs_vide()
        else:
            numero_facture = self.vue_facture.get_numero_facture()
            numero_bon = self.vue_facture.get_numero_bon()
            destinataire = self.vue_facture.get_destinataire()
            montant_total = self.vue_facture.get_montant_total()
            nombre_adherents = self.vue_facture.get_nombre_adherents()
            if len(self.actualiser_liste_adherents_independants_nom()) < nombre_adherents and destinataire == "indépendants":
                self.vue_facture.message_erreur_nombres_adherents()
            elif len(self.actualiser_liste_adherents_noms(destinataire)) < nombre_adherents and destinataire != "indépendants":
                self.vue_facture.message_erreur_nombres_adherents()
            else:
                self.nouvelle_facture()
                self.facture.set_numFacture(numero_facture)
                self.facture.set_refBdc(numero_bon)
                self.facture.set_nbAdh(nombre_adherents)
                self.facture.set_montant(montant_total)
                if destinataire != "indépendants":
                    self.facture.set_nom_organisation(destinataire)
                    self.facture.set_adresse_organisation(self.organisations_csv.get_adresse(destinataire))
                    self.facture.set_ville_organisation(self.organisations_csv.get_ville(destinataire))
                else:
                    self.facture.set_nom_organisation("indépendants")
                self.vue_facture.activer_champs_partie2()
                self.vue_facture.desactiver_champs_partie1()

                if destinataire == "indépendants":
                    liste = self.actualiser_liste_adherents_independants_nom()
                else:
                    liste = self.actualiser_liste_adherents_noms(destinataire)
                self.vue_facture.actualiser_liste_adherents(liste)

    def ajouter_informations_adherents_facture(self):
        if self.facture.get_ajoute() == self.vue_facture.get_nombre_adherents():
            self.vue_facture.message_erreur_ajout_adherent()
        elif self.vue_facture.champs_partie2_vides():
            self.vue_facture.message_erreur_champs_vide()
        else:
            if self.facture.get_ajoute() == self.vue_facture.get_nombre_adherents() - 1:
                self.vue_facture.activer_generer()
            designation = self.vue_facture.get_adherent_selectionne()
            prenom = designation[0]
            nom = designation[1]
            type = self.vue_facture.get_type_tarif()
            if self.facture.get_nom_organisation() == "indépendants":
                self.facture.set_nom_organisation(str(prenom + " " + nom))
                self.facture.set_ville_organisation(self.adherents_csv.get_ville_independant(designation))
                self.facture.set_adresse_organisation(self.adherents_csv.get_adresse_independant(designation))
            self.facture.ajouter_adherent(prenom, nom, type)
            self.vue_facture.actualiser_liste_adherents_ajoutes(prenom, nom, type)
            self.vue_facture.vider_champs_partie2()

    def generer(self):
        path = self.vue_facture.get_fichier_path()
        self.generateur_facture.genererFacture(path, self.facture)
        self.vue_facture.effacer_informations()

    def actualiser_liste_adherents_noms(self, nom_organisation):
        return sorted(self.adherents_csv.lire_fichier_organisations(nom_organisation))

    def actualiser_liste_adherents_independants_nom(self):
        return sorted(self.adherents_csv.lire_fichier_noms_independants())

    def actualiser_liste_organisations_noms(self):
        return sorted(self.organisations_csv.lire_fichier_noms())