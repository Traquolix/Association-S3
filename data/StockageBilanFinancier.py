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
        with open(self.fichier_bilan, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in csvreader:
                if len(row) == 5:
                    operation = Operation()
                    operation.set_type(row[0])
                    operation.set_categorie(row[1])
                    operation.set_date(row[2])
                    operation.set_montant(row[3])
                    operation.set_description(row[4])
                    if operation.get_type() == 'recette':
                        self.bilan.ajouter_recettes(operation.toString())
                    else:
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

        with open(self.fichier_bilan, 'a', newline='') as csvfile:
            fieldnames = ['type','categorie','date', 'montant', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writerow({'type' : type,'categorie' : categorie,'date': date, 'montant' : montant, 'description' : description})

    def contient_operation(self, operation):

        contient = False
        type = operation.get_type()
        categorie = operation.get_categorie()
        date = operation.get_date()
        montant = operation.get_montant()
        description = operation.get_description()

        with open(self.fichier_bilan, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in csvreader:
                if len(row) == 5:
                    if row[0] == type and row[1] == categorie and row[2] == date and row[3] == montant and row[4] == description:
                        contient = True
                        return contient
        return contient

    def supprimer_operation(self, operation):
        bilan = self.lire_fichier(operation.get_type())
        self.initialiser_fichier()
        for row in bilan:
            operation1 = Operation()
            operation1.set_type(row[0])
            operation1.set_categorie(row[1])
            operation1.set_date(row[2])
            operation1.set_montant(row[3])
            operation1.set_description(row[4])
            if operation != operation1:
                if operation1.get_type() == 'recette':
                    self.bilan.ajouter_recettes(operation1.toString())
                else:
                    self.bilan.ajouter_depenses(operation1.toString())

    def modifier_operation(self, operation1, operation2):  # categorie 1 a remplacer par categorie 2
        bilan = self.lire_fichier()
        ligne = [operation1.toString()]
        bilan.insert(operation2.toString(), operation1.toString())
        bilan.remove(ligne)