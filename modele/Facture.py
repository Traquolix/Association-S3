class Facture:

    def __init__(self):
        self.numFacture = ""
        self.refBdc = ""
        self.montant = 0
        self.nbAdh = 0
        self.nom_organisation = ""
        self.adresse_organisation = ""
        self.ville_organisation = ""
        self.adherents = []
        self.ajoute = 0 # Compteur juste utilisé par l'interface

    def set_numFacture(self, numfact):
        self.numFacture = numfact

    def get_numFacture(self):
        return self.numFacture

    def set_refBdc(self, num_bdc):
        self.refBdc = num_bdc

    def get_refBdc(self):
        return self.refBdc

    def set_montant(self, montant):
        self.montant = montant

    def get_montant(self):
        return self.montant

    def set_nbAdh(self, nb_adh):
        self.nbAdh = nb_adh

    def get_nbAdh(self):
        return self.nbAdh

    def get_ajoute(self):
        return self.ajoute

    def set_nom_organisation(self, nom_organisation):
        self.nom_organisation = nom_organisation

    def get_nom_organisation(self):
        return self.nom_organisation

    def set_adresse_organisation(self, adresse_organisation):
        self.adresse_organisation = adresse_organisation

    def get_adresse_organisation(self):
        return self.adresse_organisation

    def set_ville_organisation(self, ville_organisation):
        self.ville_organisation = ville_organisation

    def get_ville_organisation(self):
        return self.ville_organisation

    def get_adherents(self):
        return self.adherents

    def ajouter_adherent(self, prenom, nom, type_tarif):
        adherent = [prenom, nom, type_tarif]
        self.adherents.append(adherent)
        self.ajoute += 1
