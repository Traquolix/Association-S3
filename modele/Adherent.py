class Adherent:

    def __init__(self):
        self.prenom = ""
        self.nom = ""
        self.laboratoire = ""

    def get_prenom(self):
        return self.prenom

    def set_prenom(self, nv_prenom):
        self.prenom = nv_prenom

    def get_nom(self):
        return self.nom

    def set_nom(self, nv_nom):
        self.nom = nv_nom

    def set_laboratoire(self, nv_labo):
        self.laboratoire = nv_labo

    def get_laboratoire(self):
        return self.laboratoire
