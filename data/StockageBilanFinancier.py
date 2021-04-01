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
            fieldnames = ['categorie', 'montant', 'date', 'description']
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
                        operation.set_type('Recettes')
                        operation.set_categorie(recettesCat[len(recettesCat)-1])
                        self.bilan.ajouter_recettes(operation)
                    else:
                        operation.set_type('Dépense')
                        operation.set_categorie(depensesCat[len(depensesCat) - 1])
                        self.bilan.ajouter_depenses(operation)
        if type == 'recette':
            return self.bilan.recettes
        else:
            return self.bilan.depenses

        """
        with open(self.fichier_bilan, newline='') as csvfile:
            cpt = 0

            if nom_categorie == "Revue TAl":
                csvreader = ps.read_csv(csvfile, skiprows=2, nrows=11)
                for row in csvreader:
                    categorie = Operation();
                    categorie.set_date(row[0])
                    categorie.set_montant(row[1])
                    categorie.set_description(row[2])
                    categorie.append(categorie)
                    self.bilan.ajouter_depenses(categorie)
                    cpt += 1

            elif nom_categorie == "Site ATA":
                csvreader = ps.read_csv(csvfile, skiprows=15, nrows=4)
                for row in csvreader:
                    categorie = Operation();
                    categorie.set_date(row[0])
                    categorie.set_montant(row[1])
                    categorie.set_description(row[2])
                    categorie.append(categorie)
                    self.bilan.ajouter_depenses(categorie)
                    cpt += 1

            elif nom_categorie == "Missions":
                csvreader = ps.read_csv(csvfile, skiprows=22, nrows=2)
                for row in csvreader:
                    categorie = Operation();
                    categorie.set_date(row[0])
                    categorie.set_montant(row[1])
                    categorie.set_description(row[2])
                    categorie.append(categorie)
                    self.bilan.ajouter_depenses(categorie)
                    cpt += 1

            elif nom_categorie == "Bourses ATALA":
                csvreader = ps.read_csv(csvfile, skiprows=27, nrows=2)
                for row in csvreader:
                    categorie = Operation();
                    categorie.set_date(row[0])
                    categorie.set_montant(row[1])
                    categorie.set_description(row[2])
                    categorie.append(categorie)
                    self.bilan.ajouter_depenses(categorie)
                    cpt += 1

            elif nom_categorie == "Journées ATALA":
                csvreader = ps.read_csv(csvfile, skiprows=33, nrows=3)
                for row in csvreader:
                    categorie = Operation();
                    categorie.set_date(row[0])
                    categorie.set_montant(row[1])
                    categorie.set_description(row[2])
                    categorie.append(categorie)
                    self.bilan.ajouter_depenses(categorie)
                    cpt += 1

            elif nom_categorie == "Organisation TALN":
                csvreader = ps.read_csv(csvfile, skiprows=39, nrows=3)
                for row in csvreader:
                    categorie = Operation();
                    categorie.set_date(row[0])
                    categorie.set_montant(row[1])
                    categorie.set_description(row[2])
                    categorie.append(categorie)
                    self.bilan.ajouter_depenses(categorie)
                    cpt += 1

            elif nom_categorie == "Frais gestion":
                csvreader = ps.read_csv(csvfile, skiprows=46, nrows=4)
                for row in csvreader:
                    categorie = Operation();
                    categorie.set_date(row[0])
                    categorie.set_montant(row[1])
                    categorie.set_description(row[2])
                    categorie.append(categorie)
                    self.bilan.ajouter_depenses(categorie)
                    cpt += 1

            elif nom_categorie == "TOTAL DEPENSES":
                csvreader = ps.read_csv(csvfile, skiprows=52, nrows=1)
                for row in csvreader:
                    categorie = Operation();
                    categorie.set_date(row[0])
                    categorie.set_montant(row[1])
                    categorie.set_description(row[2])
                    categorie.append(categorie)
                    self.bilan.ajouter_depenses(categorie)
                    cpt += 1

            elif nom_categorie == "Adhésions":
                csvreader = ps.read_csv(csvfile, skiprows=56, nrows=13)
                for row in csvreader:
                    categorie = Operation();
                    categorie.set_date(row[0])
                    categorie.set_montant(row[1])
                    categorie.set_description(row[2])
                    categorie.append(categorie)
                    self.bilan.ajouter_depenses(categorie)
                    cpt += 1

            elif nom_categorie == "Bénéfice TALN":
                csvreader = ps.read_csv(csvfile, skiprows=71, nrows=1)
                for row in csvreader:
                    categorie = Operation();
                    categorie.set_date(row[0])
                    categorie.set_montant(row[1])
                    categorie.set_description(row[2])
                    categorie.append(categorie)
                    self.bilan.ajouter_depenses(categorie)
                    cpt += 1

            elif nom_categorie == "Subventions":
                csvreader = ps.read_csv(csvfile, skiprows=75, nrows=2)
                for row in csvreader:
                    categorie = Operation();
                    categorie.set_date(row[0])
                    categorie.set_montant(row[1])
                    categorie.set_description(row[2])
                    categorie.append(categorie)
                    self.bilan.ajouter_depenses(categorie)
                    cpt += 1

            elif nom_categorie == "Intérêts":
                csvreader = ps.read_csv(csvfile, skiprows=81, nrows=1)
                for row in csvreader:
                    categorie = Operation();
                    categorie.set_date(row[0])
                    categorie.set_montant(row[1])
                    categorie.set_description(row[2])
                    categorie.append(categorie)
                    self.bilan.ajouter_depenses(categorie)
                    cpt += 1

            elif nom_categorie == "TOTAL RECETTES":
                csvreader = ps.read_csv(csvfile, skiprows=83, nrows=1)
                for row in csvreader:
                    categorie = Operation();
                    categorie.set_date(row[0])
                    categorie.set_montant(row[1])
                    categorie.set_description(row[2])
                    categorie.append(categorie)
                    self.bilan.ajouter_depenses(categorie)
                    cpt += 1

            elif nom_categorie == "Commissions CB":
                csvreader = ps.read_csv(csvfile, skiprows=86, nrows=14)
                for row in csvreader:
                    categorie = Operation();
                    categorie.set_date(row[0])
                    categorie.set_montant(row[1])
                    categorie.append(categorie)
                    self.bilan.ajouter_depenses(categorie)
                    cpt += 1
        return self.bilan  # retourne le bilan
        """

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
            writer.writerow(
                {'type': type, 'categorie': categorie, 'date': date, 'montant': montant, 'description': description})

    def supprimer_operation(self, operation):
        bilan = self.lire_fichier()
        ligne = [operation.get_type(), operation.get_categorie(), operation.get_date(), operation.get_montant(),
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