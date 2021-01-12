class Facture:

    def __init__(self, nom):
        self.id = Facture.genererId()

    @staticmethod
    def genererId():
        return 12 #voir comment générer le numéro de facture
