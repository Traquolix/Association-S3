from metier.Adherent import Adherent
from data.StockageAdherentCsv import StockageAdherentCsv


class GestionAdherents:

    def __init__(self):
        self.stockage = StockageAdherentCsv()

    def ajouterAdherent(self, prenom, nom):
        adherent = Adherent(nom, prenom)
        if not self.stockage.contientAdherents(adherent):
            self.stockage.ecrirefichier(adherent)

