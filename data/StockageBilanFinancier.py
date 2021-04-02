import csv
import pandas as ps
import numpy as np

from modele.BilanFinancier import BilanFinancier
from modele.Operation import Operation


class StockageBilanFinancier:

    def __init__(self):
        self.fichier_bilan = "data/Bilan_financier_2020/budget_2019.csv"
        self.bilan = BilanFinancier()

    def initialiser_fichier(self):
        with open(self.fichier_bilan, 'w', newline='') as csvfile:
            fieldnames = ['date', 'montant', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    def lire_fichier(self, type):
        depensesCat = []
        recettesCat = []
        with open(self.fichier_bilan, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            boolean = False
            for row in csvreader:
                if len(row) == 1:
                    if row[0] == 'ï»¿DÃ‰PENSES':
                        boolean = False
                    elif row[0] == 'RECETTES':
                        boolean = True
                    elif boolean == False:
                        depensesCat.append(row[0])
                    elif boolean == True:
                        recettesCat.append(row[0])
                elif len(row) == 3:
                    operation = Operation()
                    operation.set_date(row[0])
                    operation.set_montant(row[1])
                    operation.set_description(row[2])
                    if boolean == True:
                        operation.set_type('Recette')
                        operation.set_categorie(recettesCat[len(recettesCat)-1])
                        self.bilan.ajouter_recettes(operation.toString())
                    else:
                        operation.set_type('Dépense')
                        operation.set_categorie(depensesCat[len(depensesCat)-1])
                        self.bilan.ajouter_depenses(operation.toString())
        if type == 'recette':
            return self.bilan.recettes
        else:
            return self.bilan.depenses


    def ajouter_operation(self, operation):

        type = operation.get_type()
        categorie = operation.get_categorie()
        date = operation.get_date()
        montant = operation.get_montant()
        description = operation.get_description()
        boolean = False

        with open(self.fichier_bilan, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='|')
            writer.writerow(operation.toString())
            if type == 'recette':
                self.bilan.ajouter_recettes(operation.toString())
            else:
                self.bilan.ajouter_depenses(operation.toString())
            self.initialiser_fichier()
            """for row in csvreader:
                if row[0] == categorie:
                    boolean = True
                if boolean == True and row[0] == None:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow(
                        {'date': date, 'montant': montant, 'description': description})
                    if type == 'recette':
                        self.bilan.ajouter_recettes(operation.toString())
                    else:
                        self.bilan.ajouter_depenses(operation.toString())"""

    def supprimer_operation(self, operation):
        bilan = self.lire_fichier(operation.get_type())
        ligne = [operation.get_categorie(), operation.get_date(), operation.get_montant(),
                 operation.get_description()]
        bilan.remove(ligne)
        self.initialiser_fichier()

    def modifier_operation(self, operation1, operation2):  # categorie 1 a remplacer par categorie 2
        bilan = self.lire_fichier()
        ligne = [operation1.get_type(), operation1.get_categorie(), operation1.get_date(), operation1.get_montant(),
                 operation1.get_description()]
        bilan.insert(operation2, operation1)
        bilan.remove(ligne)
        self.initialiser_fichier()