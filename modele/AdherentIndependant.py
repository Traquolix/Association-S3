class AdherentIndependant:

    def __init__(self):
        self.prenom = ""
        self.nom = ""
        self.adresse = ""
        self.ville = ""

    def get_prenom(self):
        return self.prenom

    def set_prenom(self, nv_prenom):
        self.prenom = nv_prenom

    def get_nom(self):
        return self.nom

    def set_nom(self, nv_nom):
        self.nom = nv_nom

    def set_adresse(self, nv_adresse):
        self.adresse = nv_adresse

    def get_adresse(self):
        return self.adresse

    def get_ville(self):
        return self.ville

    def set_ville(self, nv_ville):
        self.ville = nv_ville
