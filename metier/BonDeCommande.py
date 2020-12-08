import datetime

class BonDeCommande:

    def __init__(self, id, id_aff, infoATALA1, infoATALA2, infoATALA3, infoATALA4, infoSociete1, infoSociete2, infoSociete3, date, date_aff, designation_titre, prix_unitaire_titre, quantite_titre, montantHT_titre, remarque_titre, designation, prix_unitaire, quantite, montantHT, remarque, totalHT, totalHT_aff, cond_paye, totalTTC, totalTTC_aff, conclusion):
		
		# ---------------------------------------Partie haute bon de commande----------------------------- #
        self.id = Prendre le numéro du bon de commande
        self.id_aff = "BON DE COMMANDE N° " + id
        # ---------------------------------------Partie en haut tableau gauche---------------------------- #
        self.infoATALA1 = "Association pour le traitement Automatique des Lagues"
        self.infoATALA2 = "45 rue d'Ulm"
        self.infoATALA3 = "75230 Paris Cedex 5"
        self.infoATALA4 = "Siret : 393 902 721 00014"
        # ---------------------------------------Partie en haut tableau droite---------------------------- #
        self.infoSociete1 = "A :            " + "Prendre le nom de l'entreprise de destination"
        self.infoSociete2 = "Adresse :      " + "Prendre la rue de l'entreprise de destination"
        self.infoSociete3 = "               " + "Prendre le code postal et la ville"
        # ---------------------------------------Date----------------------------------------------------- #
        self.date = datetime.datetime.now()
        self.date_aff = "Date :         " + date.strftime("%y/%m/%d")
        # ---------------------------------------Titre colones tableau------------------------------------ #
        self.designation_titre = "Désignation"
        self.prix_unitaire_titre = "Prix unitaire"
        self.quantite_titre = "Quantite"
        self.montantHT_titre = "Montant HT"
        self.remarque_titre = "Remarque"
        # ---------------------------------------Tableau avec les infos donné----------------------------- #
        self.designation = "Prendre la designation entrée"
        self.prix_unitaire = Prendre le prix entré
        self.quantite = Prendre la quantite de cette designation
        self.montantHT = prix_unitaire * quantite
        self.remarque = "Prendre la remarque de cette designation"
        # ---------------------------------------Totaux--------------------------------------------------- #
        self.totalHT = montantHT # + tout les autres
        self.totalHT_aff = "TOTAL € HT       " + totalHT
        self.cond_paye = "Conditions de paiement :"
        self.totalTTC = totalHT # car la TVA est à 0%
		self.totalTTC_aff = "TTC       " + totalTTC
		self.conclusion = "Solen Quiniou, trésorière adjointe de l'ATALA"