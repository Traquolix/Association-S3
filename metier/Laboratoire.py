class Laboratoire:

    def __init__(self, nom):
        self.nom = nom

    def getLabo(self):
        return self.nom

    def __str__(self):
        return "nom : " + self.nom

