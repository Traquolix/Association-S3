class Operation:

    def __init__(self):
        self.type = ""
        self.categorie = ""
        self.montant = 0
        self.date = ""
        self.description = ""

    def set_categorie(self, categorie):
        self.categorie = categorie

    def set_montant(self, montant):
        self.montant = montant

    def set_date(self, date):
        self.date = date

    def set_description(self, description):
        self.description = description

    def set_type(self, type):
        self.type = type

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


