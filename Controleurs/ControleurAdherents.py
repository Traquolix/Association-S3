from data.StockageLaboratoireCsv import StockageLaboratoireCsv
from data.StockageAdherentCsv import StockageAdherentCsv
from modele.Laboratoire import Laboratoire
from modele.Adherent import Adherent


class ControleurAdherents:

    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.adherents_csv = StockageAdherentCsv()
        self.laboratoire_csv = StockageLaboratoireCsv()
        self.vue_adherents = None
        self.vue_laboratoires = None
        self.vue_bon_commande = None

    def set_vue_adherents(self, vue_adherents):
        self.vue_adherents = vue_adherents

    def set_vue_laboratoires(self, vue_laboratoires):
        self.vue_laboratoires = vue_laboratoires

    def set_vue_bon_commande(self, vue_bon_commande):
        self.vue_bon_commande = vue_bon_commande

    def actualiser_liste_adherents(self):
        return sorted(self.adherents_csv.lire_fichier_complets())

    def ajouter_adherent(self):
        if self.vue_adherents.champ_vide():
            self.vue_adherents.message_erreur_champs_vide()
        elif self.vue_adherents.listbox_labo_est_vide():
            self.vue_adherents.message_erreur_labo_vide()
        else:
            prenom = self.vue_adherents.get_prenom()
            nom = self.vue_adherents.get_nom()
            labo = self.vue_adherents.get_laboratoire()
            adherent = Adherent()
            adherent.set_prenom(prenom)
            adherent.set_nom(nom)
            adherent.set_laboratoire(labo)
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
            adherent.set_laboratoire(a[2])
            self.adherents_csv.supprimer_adherent(adherent)
            self.vue_adherents.actualiser_liste_adherents()
        else:
            self.vue_adherents.message_erreur_suppression()

    def ajouter_laboratoire(self):
        if self.vue_laboratoires.champ_vide():
            self.vue_laboratoires.message_erreur_champs_vide()
        else:
            nom = self.vue_laboratoires.get_nom()
            adresse = self.vue_laboratoires.get_adresse()
            laboratoire = Laboratoire()
            laboratoire.set_nom(nom)
            laboratoire.set_adresse(adresse)
            if not self.laboratoire_csv.contient_laboratoire(laboratoire):
                self.laboratoire_csv.ajouter_laboratoire(laboratoire)
                self.vue_laboratoires.actualiser_liste_laboratoires()
                self.vue_adherents.actualiser_liste_laboratoires()
                self.vue_laboratoires.viderChamps()
            else:
                self.vue_laboratoires.message_erreur_ajout()

    def supprimer_laboratoire(self):
        if not self.vue_laboratoires.listbox_est_vide():
            l = self.vue_laboratoires.get_selected_laboratoire()
            laboratoire = Laboratoire()
            laboratoire.set_nom(l[0])
            laboratoire.set_adresse(l[1])
            self.laboratoire_csv.supprimer_laboratoire(laboratoire)
            self.vue_adherents.actualiser_liste_laboratoires()
            self.vue_laboratoires.actualiser_liste_laboratoires()
        else:
            self.vue_laboratoires.message_erreur_suppression()

    def actualiser_liste_laboratoire_noms(self):
        return sorted(self.laboratoire_csv.lire_fichier_noms())

    def actualiser_liste_laboratoire_complets(self):
        return sorted(self.laboratoire_csv.lire_fichier_complets())
