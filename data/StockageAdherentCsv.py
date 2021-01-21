import csv

from modele.Adherent import Adherent
from modele.AdherentIndependant import AdherentIndependant


class StockageAdherentCsv:

    def __init__(self):
        self.fichier_adherent = "data/adherents.csv"
        self.fichier_adherent_independant = "data/adherents_independants.csv"

    def initialiser_fichier(self):
        with open(self.fichier_adherent, 'w', newline='') as csvfile:
            fieldnames = ['prenom', 'nom', 'organisation']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    def initialiser_fichier_independants(self):
        with open(self.fichier_adherent_independant, 'w', newline='') as csvfile:
            fieldnames = ['prenom', 'nom', 'adresse', 'ville']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    def lire_fichier(self):
        adherents = []
        with open(self.fichier_adherent, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cpt = 0
            for row in csvreader:
                if cpt != 0:
                    adherent = Adherent()
                    adherent.set_prenom(row[0])
                    adherent.set_nom(row[1])
                    adherent.set_organisation(row[2])
                    adherents.append(adherent)
                cpt = cpt + 1
        return adherents  # retourne une liste d'adhérents

    def lire_fichier_independants(self):
        adherents = []
        with open(self.fichier_adherent_independant, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cpt = 0
            for row in csvreader:
                if cpt != 0:
                    adherent = AdherentIndependant()
                    adherent.set_prenom(row[0])
                    adherent.set_nom(row[1])
                    adherent.set_adresse(row[2])
                    adherent.set_ville(row[3])
                    adherents.append(adherent)
                cpt = cpt + 1
        return adherents  # retourne une liste d'adhérents indépendants

    def lire_fichier_complets(self):
        adherents = []
        with open(self.fichier_adherent, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cpt = 0
            for row in csvreader:
                if cpt != 0:
                    adherents.append(row)
                cpt = cpt + 1
        return adherents

    def lire_fichier_complets_independants(self):
        adherents = []
        with open(self.fichier_adherent_independant, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cpt = 0
            for row in csvreader:
                if cpt != 0:
                    adherents.append(row)
                cpt = cpt + 1
        return adherents

    def lire_fichier_organisations(self, nom_organisation):
        adherents = []
        with open(self.fichier_adherent, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cpt = 0
            for row in csvreader:
                if cpt != 0:
                    if row[2] == nom_organisation:
                        ligne = [row[0], row[1]]
                        adherents.append(ligne)
                cpt = cpt + 1
        return adherents

    def lire_fichier_noms_independants(self):
        adherents = []
        ligne = []
        with open(self.fichier_adherent_independant, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cpt = 0
            for row in csvreader:
                if cpt != 0:
                    ligne.append(row[0])
                    ligne.append(row[1])
                    adherents.append(ligne)
                cpt = cpt + 1
        return adherents

    def get_ville_independant(self, adherent):
        ville = ""
        with open(self.fichier_adherent_independant, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csvreader:
                if adherent[0] == row[0] and adherent[1] == row[1]:
                    ville = row[3]
        return ville

    def get_adresse_independant(self, adherent):
        adresse = ""
        with open(self.fichier_adherent_independant, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csvreader:
                if adherent[0] == row[0] and adherent[1] == row[1]:
                    adresse = row[2]
        return adresse

    def contient_adherent(self, adherent):
        contient = False
        with open(self.fichier_adherent, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csvreader:
                if row[0] == adherent.get_prenom() and row[1] == adherent.get_nom():
                    contient = True
                    return contient
        return contient

    def contient_adherent_independant(self, adherent_independant):
        contient = False
        with open(self.fichier_adherent_independant, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csvreader:
                if row[0] == adherent_independant.get_prenom() and row[1] == adherent_independant.get_nom():
                    contient = True
                    return contient
        return contient

    def ajouter_adherent(self, adherent):
        prenom = adherent.get_prenom()
        nom = adherent.get_nom()
        organisation = adherent.get_organisation()

        with open(self.fichier_adherent, 'a', newline='') as csvfile:
            fieldnames = ['prenom', 'nom', 'organisation']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'prenom': prenom, 'nom': nom, 'organisation': organisation})

    def ajouter_adherent_independant(self, adherent):
        prenom = adherent.get_prenom()
        nom = adherent.get_nom()
        adresse = adherent.get_adresse()
        ville = adherent.get_ville()

        with open(self.fichier_adherent_independant, 'a', newline='') as csvfile:
            fieldnames = ['prenom', 'nom', 'adresse', 'ville']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'prenom': prenom, 'nom': nom, 'adresse': adresse, 'ville': ville})

    def supprimer_adherent(self, adherent):
        adherents = self.lire_fichier_complets()
        ligne = [adherent.get_prenom(), adherent.get_nom(), adherent.get_organisation()]
        adherents.remove(ligne)
        self.initialiser_fichier()
        for nv_ligne in adherents:
            adh = Adherent()
            adh.set_prenom(nv_ligne[0])
            adh.set_nom(nv_ligne[1])
            adh.set_organisation(nv_ligne[2])
            self.ajouter_adherent(adh)

    def supprimer_adherent_independant(self, adherent):
        adherents = self.lire_fichier_complets_independants()
        ligne = [adherent.get_prenom(), adherent.get_nom(), adherent.get_adresse(), adherent.get_ville()]
        adherents.remove(ligne)
        self.initialiser_fichier_independants()
        for nv_ligne in adherents:
            adh = AdherentIndependant()
            adh.set_prenom(nv_ligne[0])
            adh.set_nom(nv_ligne[1])
            adh.set_adresse(nv_ligne[2])
            adh.set_ville(nv_ligne[3])
            self.ajouter_adherent_independant(adh)

