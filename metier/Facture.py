import os

from modèle.GenererFacture import GenererFacture

class Facture:

    def __init__(self, nom):
        self.id = Facture.genererId()

    @staticmethod
    def genererId():
        return 12 #voir comment générer le numéro de facture

    @classmethod
    def genererFacture(cls, param, param1, param2, param3):

        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logo.png')

        GenererFacture.genererFacture(path, param, param1, param2, param3)
        pass