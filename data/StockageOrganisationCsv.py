import csv

from modele.Organisation import Organisation


class StockageOrganisationCsv:

    def __init__(self):
        self.fichier_organisations = "data/organisations.csv"

    def initialiser_fichier(self):
        with open(self.fichier_organisations, 'w', newline='') as csvfile:
            fieldnames = ['nom', 'adresse', 'ville']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    def lire_fichier(self):
        organisations = []
        with open(self.fichier_organisations, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cpt = 0
            for row in csvreader:
                if cpt != 0:
                    organisation = Organisation()
                    organisation.set_nom(row[0])
                    organisation.set_adresse(row[1])
                    organisation.set_ville(row[2])
                    organisations.append(organisation)
                cpt = cpt + 1
        return organisations  # return une liste d' instances des organisations

    def lire_fichier_noms(self):
        organisations = []
        with open(self.fichier_organisations, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cpt = 0
            for row in csvreader:
                if cpt != 0:
                    organisations.append(row[0])
                cpt = cpt + 1
        return organisations

    def lire_fichier_complets(self):
        organisations = []
        with open(self.fichier_organisations, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cpt = 0
            for row in csvreader:
                if cpt != 0:
                    organisations.append(row)
                cpt = cpt + 1
        return organisations

    def get_adresse(self, nom_organisation):
        adresse = ""
        with open(self.fichier_organisations, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csvreader:
                if nom_organisation == row[0]:
                    adresse = row[1]
        return adresse

    def get_ville(self, nom_organisation):
        ville = ""
        with open(self.fichier_organisations, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csvreader:
                if nom_organisation == row[0]:
                    ville = row[2]
        return ville

    def contient_organisation(self, organisation):
        contient = False
        with open(self.fichier_organisations, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csvreader:
                if row[0] == organisation.get_nom():
                    contient = True
                    return contient
        return contient

    def ajouter_organisation(self, organisation):
        nom = organisation.get_nom()
        adresse = organisation.get_adresse()
        ville = organisation.get_ville()

        with open(self.fichier_organisations, 'a', newline='') as csvfile:
            fieldnames = ['nom', 'adresse', 'ville']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'nom': nom, 'adresse': adresse, 'ville': ville})

    def supprimer_organisation(self, organisation):
        organisations = self.lire_fichier_complets()
        ligne = [organisation.get_nom(), organisation.get_adresse(), organisation.get_ville()]
        organisations.remove(ligne)
        self.initialiser_fichier()
        for nv_ligne in organisations:
            organisation = Organisation()
            organisation.set_nom(nv_ligne[0])
            organisation.set_adresse(nv_ligne[1])
            organisation.set_ville(nv_ligne[2])
            self.ajouter_organisation(organisation)
