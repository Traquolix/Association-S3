from modele.Operation import Operation

class BilanFinancier:

    def __init__(self):
        self.actif = []
        self.passif = []

    def ajouter_actif(self, categorie):
        self.actif.append(categorie)

    def supprimer_actif(self, categorie):
        self.actif.remove(categorie)

    def ajouter_passif(self, categorie):
        self.passif.append(categorie)

    def supprimer_passif(self, categorie):
        self.passif.remove(categorie)