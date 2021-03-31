import csv

from modele.BilanFinancier import BilanFinancier
from modele.Operation import Operation

class StockageBilanFinancier:

    def __init__(self):
        self.fichier_bilan = "data/bilan.csv"
        self.bilan = BilanFinancier()

    def initialiser_fichier(self):
        with open(self.fichier_bilan, 'w', newline='') as csvfile:
            fieldnames = ['categorie','montant','date','description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    def lire_fichier(self):
        with open(self.fichier_bilan, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csvreader:
                categorie = Operation()


                #Lire le csv


                self.bilan.ajouter_depenses(categorie)
        return self.bilan  # retourne le bilan

    def ajouter_operation(self, operation):

        # Assigner la nouvelle opération à une opération déja existante
        type = operation.get_type()
        categorie = operation.get_categorie()
        date = operation.get_date()
        montant = operation.get_montant()
        description = operation.get_description()

        with open(self.fichier_bilan, 'a', newline='') as csvfile:
            fieldnames = ['type', 'categorie', 'date', 'montant', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'type': type, 'categorie': categorie, 'date': date, 'montant': montant,'description': description})

    def supprimer_operation(self, operation):
        bilan = self.lire_fichier()
        ligne = [operation.get_type(), operation.get_categorie(), operation.get_date(), operation.get_montant(), operation.get_description()]
        bilan.remove(ligne)
        self.initialiser_fichier()

    def modifier_operation(self, operation1, operation2): #categorie 1 a remplacer par categorie 2
        bilan = self.lire_fichier()
        ligne = [operation1.get_type(), operation1.get_categorie(), operation1.get_date(), operation1.get_montant(), operation1.get_description()]
        bilan.insert(operation2,operation1)
        bilan.remove(ligne)
        self.initialiser_fichier()
