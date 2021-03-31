class BilanFinancier:

    def __init__(self):
        self.depenses = []
        self.recettes = []

    def ajouter_depenses(self, operation):
        self.depenses.append(operation)

    def supprimer_depenses(self, operation):
        self.depenses.remove(operation)

    def ajouter_recettes(self, operation):
        self.recettes.append(operation)

    def supprimer_recettes(self, operation):
        self.recettes.remove(operation)