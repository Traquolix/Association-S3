import csv

from metier.Adherent import Adherent


class StockageAdherentCsv:

    def __init__(self):
        self.fichierAdherent = "data/adherents.csv"

    def lirefichier(self):
        adherents = []
        with open(self.fichierAdherent, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cpt = 0
            for row in csvreader:
                if cpt != 0:
                    adherents.append(row)
                cpt = cpt + 1
        return adherents

    def contientAdherents(self, adherent):
        with open(self.fichierAdherent, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csvreader:
                if row[0] == adherent.getPrenom() and row[1] == adherent.getNom():
                    return True
        return False

    def initialiserfichier(self):
        with open(self.fichierAdherent, 'w', newline='') as csvfile:
            fieldnames = ['prenom', 'nom', 'laboratoire']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    def ecrirefichier(self, adherent):
        nom = adherent.nom
        prenom = adherent.prenom
        labo = adherent.labo

        with open(self.fichierAdherent, 'a', newline='') as csvfile:
            fieldnames = ['prenom', 'nom', 'laboratoire']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'prenom' : prenom, 'nom' : nom, 'laboratoire' : labo})

    def supprimer(self, supp_adherent):
        adherents = self.lirefichier()
        ligne = [supp_adherent[0], supp_adherent[1], supp_adherent[2]]
        adherents.remove(ligne)
        self.initialiserfichier()
        for nv_ligne in adherents:
            adherent = Adherent(nv_ligne[0], nv_ligne[1], nv_ligne[2])
            self.ecrirefichier(adherent)
