class Adherent:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.labo = None

    def setLaboratoire(self, labo):
        self.labo = labo

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
