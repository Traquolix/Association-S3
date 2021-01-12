import csv

from modele.Adherent import Adherent


class StockageAdherentCsv:

    def __init__(self):
        self.fichierAdherent = "data/adherents.csv"

    def initialiser_fichier(self):
        with open(self.fichierAdherent, 'w', newline='') as csvfile:
            fieldnames = ['prenom', 'nom', 'laboratoire']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    def lire_fichier(self):
        adherents = []
        with open(self.fichierAdherent, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cpt = 0
            for row in csvreader:
                if cpt != 0:
                    adherent = Adherent()
                    adherent.set_prenom(row[0])
                    adherent.set_nom(row[1])
                    adherent.set_laboratoire(row[2])
                    adherents.append(adherent)
                cpt = cpt + 1
        return adherents  # retourne une liste d'adhérents

    def lire_fichier_complets(self):
        adherents = []
        with open(self.fichierAdherent, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cpt = 0
            for row in csvreader:
                if cpt != 0:
                    adherents.append(row)
                cpt = cpt + 1
        return adherents

    def lire_fichier_labo(self, nom_labo):
        adherents = []
        with open(self.fichierAdherent, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cpt = 0
            for row in csvreader:
                if cpt != 0:
                    if row[2] == nom_labo:
                        ligne = row[0] + " " + row[1]
                        adherents.append(ligne)
                cpt = cpt + 1
        return adherents

    def contient_adherent(self, adherent):
        contient = False
        with open(self.fichierAdherent, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csvreader:
                if row[0] == adherent.get_prenom() and row[1] == adherent.get_nom():
                    contient = True
                    return contient
        return contient

    def ajouter_adherent(self, adherent):
        prenom = adherent.get_prenom()
        nom = adherent.get_nom()
        laboratoire = adherent.get_laboratoire()

        with open(self.fichierAdherent, 'a', newline='') as csvfile:
            fieldnames = ['prenom', 'nom', 'laboratoire']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'prenom': prenom, 'nom': nom, 'laboratoire': laboratoire})

    def supprimer_adherent(self, adherent):
        adherents = self.lire_fichier_complets()
        ligne = [adherent.get_prenom(), adherent.get_nom(), adherent.get_laboratoire()]
        adherents.remove(ligne)
        self.initialiser_fichier()
        for nv_ligne in adherents:
            adh = Adherent()
            adh.set_prenom(nv_ligne[0])
            adh.set_nom(nv_ligne[1])
            adh.set_laboratoire(nv_ligne[2])
            self.ajouter_adherent(adh)
