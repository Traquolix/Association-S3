from modele.BilanFinancier import BilanFinancier
from data.StockageBilanFinancier import StockageBilanFinancier
from modele.Operation import Operation


class ControleurBilan:

    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.stockagebilan = StockageBilanFinancier()
        self.bilan = BilanFinancier()
        self.vue_bilan = None
        self.vue_bilan_modification = None

    def set_vue_bilan(self, vue_bilan):
        self.vue_bilan = vue_bilan

    def set_vue_bilan_modification(self, vue_bilan_modification):
        self.vue_bilan_modification = vue_bilan_modification

    def actualiser_liste_recettes(self):
        return sorted(self.stockagebilan.lire_fichier("recette"))

    def actualiser_liste_depenses(self):
        return sorted(self.stockagebilan.lire_fichier("depenses"))

    def ajouter_operation(self):

        if self.vue_bilan.champ_vide():
            self.vue_bilan.message_erreur_champs_vide()
        else:
            operation = Operation()
            operation.set_type(self.vue_bilan.get_choix_selectionne())
            operation.set_categorie(self.vue_bilan.get_categorie())
            operation.set_date(self.vue_bilan.get_date())
            operation.set_montant(self.vue_bilan.get_montant())
            operation.set_description(self.vue_bilan.get_description())
            if not self.stockagebilan.contient_operation(operation):
                if operation.get_type() == 'depense':
                    self.stockagebilan.ajouter_operation(operation)
                    self.vue_bilan.actualiser_liste_depenses()
                    self.vue_bilan.viderChamps()
                else:
                    self.bilan.ajouter_recettes(operation.toString())
                    self.vue_bilan.actualiser_liste_recettes()
                    self.vue_bilan.viderChamps()
            else:
                self.vue_bilan.message_erreur_ajout()

    def supprimer_operation(self):
        if self.vue_bilan.get_selected_operation() is not None:
            ligne = self.vue_bilan.get_selected_operation()
            operation = Operation()
            operation.set_type(ligne[0])
            operation.set_categorie(ligne[1])
            operation.set_date(ligne[2])
            operation.set_montant(ligne[3])
            operation.set_description(ligne[4])
            if operation.get_type() == 'recette':
                self.stockagebilan.supprimer_operation(operation)
                self.vue_bilan.actualiser_liste_recettes()
            else:
                self.stockagebilan.supprimer_operation(operation)
                self.vue_bilan.actualiser_liste_depenses()
        else:
            self.vue_bilan.message_erreur_suppression()

