class Adherent:

    def __init__(self):
        self.prenom = ""
        self.nom = ""
        self.organisation = ""

    def get_prenom(self):
        return self.prenom

    def set_prenom(self, nv_prenom):
        self.prenom = nv_prenom

    def get_nom(self):
        return self.nom

    def set_nom(self, nv_nom):
        self.nom = nv_nom

    def set_organisation(self, nv_orga):
        self.organisation = nv_orga

    def get_organisation(self):
        return self.organisation
