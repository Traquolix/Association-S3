import datetime

class BonDeCommande:

    def __init__(self, id, nom, infoATALA1, infoATALA2, infoATALA3, infoATALA4, infoSociete1, infoSociete2, infoSociete3, date, infoDate,  ):
        self.id = "Prendre le numéro du bon de commande"
        # ---------------------------------------Partie en haut à gauche---------------------------------- #
        self.infoATALA1 = "Association pour le traitement Automatique des Lagues"
        self.infoATALA2 = "45 rue d'Ulm"
        self.infoATALA3 = "75230 Paris Cedex 5"
        self.infoATALA4 = "Siret : 393 902 721 00014"
        # ---------------------------------------Partie en haut à droite---------------------------------- #
        self.infoSociete1 = "A :            " + "Prendre le nom de l'entreprise de destination"
        self.infoSociete2 = "Adresse :      " + "Prendre la rue de l'entreprise de destination"
        self.infoSociete3 = "               " + "Prendre le code postal et la ville"
        # ---------------------------------------date----------------------------------------------------- #
        self.date = datetime.datetime.now()
        self.infoDate = "Date :         " + date.strftime("%y/%m/%d")
        # ------------------------------------------------------------------------------------------------ #



