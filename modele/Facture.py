class Facture:

    def __init__(self):
        self.numFacture = ""
        self.refBdc = ""
        self.montant = ""
        self.nbAdh = ""
        self.typeTarif = ""

    def set_numFacture(self, numfact):
        self.numFacture = numfact

    def get_numFacture(self):
        return self.numFacture

    def set_refBdc(self, numBdc):
        self.refBdc = numBdc

    def get_refBdc(self):
        return self.refBdc

    def set_montant(self, montant):
        self.montant = montant

    def get_montant(self):
        return self.montant

    def set_nbAdh(self, nbAdh):
        self.nbAdh = nbAdh

    def get_nbAdh(self):
        return self.nbAdh

    def set_typeTarif(self, typeTarif):
        self.typeTarif = typeTarif

    def het_typeTarif(self):
        return self.typeTarif