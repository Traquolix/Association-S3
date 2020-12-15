from data import StockageAdherentCsv
from metier.Adherent import Adherent


class ControleurAdherents:

    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.adherentsCsv = StockageAdherentCsv.StockageAdherentCsv()
        self.vueAdherents = None

    def setVue(self, vueAdherent):
        self.vueAdherents = vueAdherent

    def refreshList(self):
        return sorted(self.adherentsCsv.lirefichier())

    def ajouterAdherent(self):
        prenom = self.vueAdherents.getPrenom()
        nom = self.vueAdherents.getNom()
        labo = self.vueAdherents.getLabo()
        adherent = Adherent(prenom, nom, labo)
        if not self.adherentsCsv.contientAdherents(adherent) and nom != "" and prenom != "":
            self.adherentsCsv.ecrirefichier(adherent)
            self.vueAdherents.initialiserListe()
            self.vueAdherents.viderChamps()

    def supprimerAdherent(self):
        if not self.vueAdherents.listBoxEstVide():
            a = self.vueAdherents.getSelectedAdherent()
            self.adherentsCsv.supprimer(a)
            self.vueAdherents.initialiserListe()
