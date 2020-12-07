import csv


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

    def contientAdherents(self,adherent):
        with open(self.fichierAdherent, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csvreader:
                if row[0] == adherent.getPrenom() and row[1] == adherent.getNom() and row[2] == adherent.labo:
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
        labo = adherent.labo.getLabo()

        with open(self.fichierAdherent, 'a', newline='') as csvfile:
            fieldnames = ['prenom', 'nom', 'laboratoire']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'prenom' : prenom, 'nom' : nom, 'laboratoire' : labo})
