class Organisation:

    def __init__(self):
        self.nom = ""
        self.adresse = ""
        self.ville = ""

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_adresse(self):
        return self.adresse

    def set_adresse(self, adresse):
        self.adresse = adresse

    def get_ville(self):
        return self.ville

    def set_ville(self, ville):
        self.ville = ville

    def __str__(self):
        return "nom : " + self.nom + "\nadresse : " + self.adresse + "\nville : " + self.ville