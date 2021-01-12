import csv

from modele.Laboratoire import Laboratoire


class StockageLaboratoireCsv:

    def __init__(self):
        self.fichier_laboratoire = "data/laboratoire.csv"

    def initialiser_fichier(self):
        with open(self.fichier_laboratoire, 'w', newline='') as csvfile:
            fieldnames = ['nom', 'adresse']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    def lire_fichier(self):
        laboratoires = []
        with open(self.fichier_laboratoire, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cpt = 0
            for row in csvreader:
                if cpt != 0:
                    laboratoire = Laboratoire()
                    laboratoire.set_nom(row[0])
                    laboratoire.set_adresse(row[1])
                    laboratoires.append(laboratoire)
                cpt = cpt + 1
        return laboratoires  # return une liste d' instances de laboratoire

    def lire_fichier_noms(self):
        laboratoires = []
        with open(self.fichier_laboratoire, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cpt = 0
            for row in csvreader:
                if cpt != 0:
                    laboratoires.append(row[0])
                cpt = cpt + 1
        return laboratoires

    def lire_fichier_complets(self):
        laboratoires = []
        with open(self.fichier_laboratoire, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cpt = 0
            for row in csvreader:
                if cpt != 0:
                    laboratoires.append(row)
                cpt = cpt + 1
        return laboratoires

    def get_adresse(self, nom_labo):
        adresse = ""
        with open(self.fichier_laboratoire, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csvreader:
                if nom_labo == row[0]:
                    adresse = row[1]
        return adresse

    def contient_laboratoire(self, laboratoire):
        contient = False
        with open(self.fichier_laboratoire, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csvreader:
                if row[0] == laboratoire.get_nom():
                    contient = True
                    return contient
        return contient

    def ajouter_laboratoire(self, laboratoire):
        nom = laboratoire.get_nom()
        adresse = laboratoire.get_adresse()

        with open(self.fichier_laboratoire, 'a', newline='') as csvfile:
            fieldnames = ['nom', 'adresse']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'nom': nom, 'adresse': adresse})

    def supprimer_laboratoire(self, laboratoire):
        laboratoires = self.lire_fichier_complets()
        ligne = [laboratoire.get_nom(), laboratoire.get_adresse()]
        laboratoires.remove(ligne)
        self.initialiser_fichier()
        for nv_ligne in laboratoires:
            labo = Laboratoire()
            labo.set_nom(nv_ligne[0])
            labo.set_adresse(nv_ligne[1])
            self.ajouter_laboratoire(labo)
