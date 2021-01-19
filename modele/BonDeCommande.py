import datetime


class BonDeCommande:

    def __init__(self, nb_designation):

        # ---------------------------------------Partie haute bon de commande----------------------------- #
        self.numero_bon = ""
        # ---------------------------------------Partie en haut tableau gauche---------------------------- #
        """self.info_ATALA1 = "Association pour le traitement Automatique des Langues"
        self.info_ATALA2 = "45 rue d'Ulm"
        self.info_ATALA3 = "75230 Paris Cedex 5"
        self.info_ATALA4 = "Siret : 393 902 721 00014"""""
        # ---------------------------------------Partie en haut tableau droite---------------------------- #
        self.nom_labo = "Prendre le nom de l'entreprise de destination"
        self.adresse_labo = "Prendre la rue de l'entreprise de destination"
        self.ville_labo = "Prendre le code postal et la ville"

        """infoSociete1_aff = "A :            " + self.infoSociete1
        infoSociete2_aff = "Adresse :      " + self.infoSociete2
        infoSociete3_aff = "" + self.infoSociete3"""
        # ---------------------------------------Date----------------------------------------------------- #
        """date = datetime.datetime.now()
        date_aff = "Date :         " + date.strftime("%y/%m/%d")"""
        # ---------------------------------------Titre colones tableau------------------------------------ #
        """designation_titre = "Désignation"
        prix_unitaire_titre = "Prix unitaire"
        quantite_titre = "Quantite"
        montantHT_titre = "Montant HT"
        remarque_titre = "Remarque"""""
        # ------------------------------Tableau avec les infos donné (Une seul ligne)--------------------- #
        self.adherents = []
        self.ajoute = 0
        """for i in range(0, nb_designation):
            ligne = []
            designation = ""
            ligne.append(self.designation)
            self.prix_unitaire = ""
            ligne.append(self.prix_unitaire)
            self.quantite = ""
            ligne.append(self.quantite)
            self.montantHT = ""
            ligne.append(self.montantHT)
            self.remarque = """""
        # ---------------------------------------Totaux--------------------------------------------------- #
        self.totalHT = 0  # + tout les autres
        """totalHT_aff = "TOTAL € HT       " + str(self.totalHT)
        cond_paye = "Conditions de paiement :"
        totalTTC = self.totalHT  # car la TVA est à 0%
        # totalTTC_aff = "TTC       " + totalTTC
        conclusion = "Solen Quiniou, trésorière adjointe de l'ATALA"""""
        # ------------------------------------------------------------------------------------------------ #

    def set_numero_bon(self, numero_bon):
        self.numero_bon = numero_bon

    def get_numero_bon(self):
        return self.numero_bon

    def set_nom_labo(self, nom_labo):
        self.nom_labo = nom_labo

    def set_adresse_labo(self, adresse):
        self.adresse_labo = adresse

    def get_nom_labo(self):
        return self.nom_labo

    def get_adresse(self):
        return self.adresse_labo

    def set_ville_labo(self, ville):
        self.ville_labo = ville

    def set_montant_total(self, montant):
        self.totalHT = montant

    def get_nombre_ajoute(self):
        return self.ajoute

    def get_adherents(self):
        return self.adherents

    def ajouter_adherent(self, designation, prix_unitaire, quantite, montant, remarque):
        adherent = [designation, prix_unitaire, quantite, montant, remarque]
        self.adherents.append(adherent)
        self.ajoute += 1

    def __str__(self):
        return "numéro bon de commande : " + self.numero_bon + "\nnom destinataire : " + self.nom_labo + "\nadresse destinataire : " + self.adresse_labo + "\nville destinataire : " + self.ville_labo + "\nmontant total : " + str(self.totalHT) + "\n" +self.adherents.__str__()
