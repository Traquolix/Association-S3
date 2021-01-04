from metier.Laboratoire import Laboratoire


class Adherent:

    def __init__(self, prenom, nom, labo):
        self.prenom = prenom
        self.nom = nom
        self.labo = labo

    def setLaboratoire(self, labo):
        self.labo = labo

    def getLaboratoire(self):
        return self.labo

    def getNom(self):
        return self.nom

    def setNom(self, nvNom):
        self.nom = nvNom

    def getPrenom(self):
        return self.prenom

    def setPrenom(self, nvPrenom):
        self.prenom = nvPrenom

    def __str__(self):
        return "prenom : " + self.prenom + "\nnom : " + self.nom
