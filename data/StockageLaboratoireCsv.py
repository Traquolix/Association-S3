import csv

from metier.Adherent import Adherent


class StockageLaboratoireCsv:

    def __init__(self):
        self.fichier_laboratoire = "data/laboratoire.csv"

    def lire_fichier_nom(self):
        laboratoires = []
        with open(self.fichier_laboratoire, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cpt = 0
            for row in csvreader:
                if cpt != 0:
                    laboratoires.append(row[0])
                cpt = cpt + 1
        return laboratoires

    def initialiserfichier(self):
        with open(self.fichier_laboratoire, 'w', newline='') as csvfile:
            fieldnames = ['nom', 'adresse']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
