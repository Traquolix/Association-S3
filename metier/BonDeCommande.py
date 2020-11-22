class BonDeCommande:

    def __init__(self, nom):
        self.id = BonDeCommande.genererId()

    @staticmethod
    def genererId():
        return 12 #voir comment générer le numéro de facture
