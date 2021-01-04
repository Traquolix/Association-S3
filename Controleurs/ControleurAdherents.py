from data import StockageAdherentCsv
from data import StockageLaboratoireCsv
from metier.Adherent import Adherent


class ControleurAdherents:

    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.adherents_csv = StockageAdherentCsv.StockageAdherentCsv()
        self.laboratoire_csv = StockageLaboratoireCsv.StockageLaboratoireCsv()
        self.vue_adherents = None

    def setVue(self, vue_adherent):
        self.vue_adherents = vue_adherent

    def actualiser_liste_adherents(self):
        return sorted(self.adherents_csv.lirefichier())

    def ajouterAdherent(self):
        prenom = self.vue_adherents.getPrenom()
        nom = self.vue_adherents.getNom()
        labo = self.vue_adherents.getLabo()
        adherent = Adherent(prenom, nom, labo)
        if not self.adherents_csv.contientAdherents(adherent) and nom != "" and prenom != "":
            self.adherents_csv.ecrirefichier(adherent)
            self.vue_adherents.initialiserListe()
            self.vue_adherents.viderChamps()

    def supprimerAdherent(self):
        if not self.vue_adherents.listBoxEstVide():
            a = self.vue_adherents.getSelectedAdherent()
            self.adherents_csv.supprimer(a)
            self.vue_adherents.initialiserListe()

    def actualiser_liste_laboratoire(self):
        return sorted(self.laboratoire_csv.lire_fichier_nom())
