class BonDeCommande:

    def __init__(self):
        self.numero_bon = ""
        self.nom_organisation = ""
        self.adresse_organisation = ""
        self.ville_organisation = ""
        self.adherents = []
        self.nb_adherents = 0
        self.ajoute = 0
        self.totalHT = 0

    def set_numero_bon(self, numero_bon):
        self.numero_bon = numero_bon

    def get_numero_bon(self):
        return self.numero_bon

    def set_nom_organisation(self, nom_organisation):
        self.nom_organisation = nom_organisation

    def get_nom_organisation(self):
        return self.nom_organisation

    def set_adresse_organisation(self, adresse):
        self.adresse_organisation = adresse

    def get_adresse(self):
        return self.adresse_organisation

    def set_ville_organisation(self, ville):
        self.ville_organisation = ville

    def get_ville_organisation(self):
        return self.ville_organisation

    def set_montant_total(self, montant):
        self.totalHT = montant

    def get_montant_total(self):
        return self.totalHT

    def get_nombre_ajoute(self):
        return self.ajoute

    def get_adherents(self):
        return self.adherents

    def ajouter_adherent(self, designation, prix_unitaire, quantite, montant, remarque):
        adherent = [designation, prix_unitaire, quantite, montant, remarque]
        self.adherents.append(adherent)
        self.ajoute += 1
