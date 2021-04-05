class Operation:

    def __init__(self):
        self.type = ""
        self.categorie = ""
        self.date = ""
        self.montant = ""
        self.description = ""

    def set_type(self, nv_type):
        self.type = nv_type

    def set_categorie(self, nv_categorie):
        self.categorie = nv_categorie

    def set_montant(self, nv_montant):
        self.montant = nv_montant

    def set_date(self, nv_date):
        self.date = nv_date

    def set_description(self, nv_description):
        self.description = nv_description

    def get_categorie(self):
        return self.categorie

    def get_montant(self):
        return self.montant

    def get_date(self):
        return self.date

    def get_description(self):
        return self.description

    def get_type(self):
        return self.type

    def toString(self):
        return self.categorie + " " + self.date + " " + self.montant + " " + self.description

