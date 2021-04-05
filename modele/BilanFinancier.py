from modele.Operation import Operation

class BilanFinancier:

    def __init__(self):
        self.operations = []

    def ajouter_operation(self, operation):
        self.operations.append(operation)

    def supprimer_operation(self, operation):
        self.operations.remove(operation)
