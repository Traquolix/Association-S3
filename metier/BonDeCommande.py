import datetime

class BonDeCommande:

    def __init__(self, id, infoSociete1, infoSociete2, infoSociete3, designation, prix_unitaire, quantite, remarque):
		
		# ---------------------------------------Partie haute bon de commande----------------------------- #
        self.id = Prendre le numéro du bon de commande
        id_aff = "BON DE COMMANDE N° " + id
        # ---------------------------------------Partie en haut tableau gauche---------------------------- #
        infoATALA1 = "Association pour le traitement Automatique des Lagues"
        infoATALA2 = "45 rue d'Ulm"
        infoATALA3 = "75230 Paris Cedex 5"
        infoATALA4 = "Siret : 393 902 721 00014"
        # ---------------------------------------Partie en haut tableau droite---------------------------- #
        self.infoSociete1 = "Prendre le nom de l'entreprise de destination"
        self.infoSociete2 = "Prendre la rue de l'entreprise de destination"
        self.infoSociete3 = "Prendre le code postal et la ville"

        infoSociete1_aff = "A :            " + infoSociete1
        infoSociete2_aff = "Adresse :      " + infoSociete2
        infoSociete3_aff = "               " + infoSociete3
        # ---------------------------------------Date----------------------------------------------------- #
        date = datetime.datetime.now()
        date_aff = "Date :         " + date.strftime("%y/%m/%d")
        # ---------------------------------------Titre colones tableau------------------------------------ #
        designation_titre = "Désignation"
        prix_unitaire_titre = "Prix unitaire"
        quantite_titre = "Quantite"
        montantHT_titre = "Montant HT"
        remarque_titre = "Remarque"
        # ------------------------------Tableau avec les infos donné (Une seul ligne)--------------------- #
        self.designation = "Prendre la designation entrée"
        self.prix_unitaire = Prendre le prix entré
        self.quantite = Prendre la quantite de cette designation
        montantHT = prix_unitaire * quantite
        self.remarque = "Prendre la remarque de cette designation"
        # ---------------------------------------Totaux--------------------------------------------------- #
        totalHT = montantHT # + tout les autres
        totalHT_aff = "TOTAL € HT       " + totalHT
        cond_paye = "Conditions de paiement :"
        totalTTC = totalHT # car la TVA est à 0%
		totalTTC_aff = "TTC       " + totalTTC
		conclusion = "Solen Quiniou, trésorière adjointe de l'ATALA"
        # ------------------------------------------------------------------------------------------------ #

        
