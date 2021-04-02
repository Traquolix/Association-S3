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
        return self.stockagebilan.lire_fichier("recette")

    def actualiser_liste_depenses(self):
        return self.stockagebilan.lire_fichier("depenses")

    def ajouter_operation(self):

        if self.vue_bilan().champ_vide():
            self.vue_bilan().message_erreur_champs_vide()
        else:
            operation = Operation()
            operation.set_type(self.vue_bilan().get_choix_selectionne())
            operation.set_categorie(self.vue_bilan().get_categorie())
            operation.set_date(self.vue_bilan().get_date())
            operation.set_montant(self.vue_bilan().get_montant())
            operation.set_description(self.vue_bilan().get_description())
            if operation.get_type() == 'depense':
                self.bilan.ajouter_depenses(operation.toString())
                self.stockagebilan.ajouter_operation(operation)
            else:
                self.bilan.ajouter_recettes(operation.toString())

    def supprimer_operation(self):
        if not self.vue_bilan().listbox_bilan_est_vide():
            ligne = self.vue_bilan().get_selected_operation()
            operation = Operation()
            operation.set_type(ligne[0])
            operation.set_categorie(ligne[1])
            operation.set_date(ligne[2])
            operation.set_montant(ligne[3])
            operation.set_description(ligne[4])
            if operation.get_type() == 'recette':
                self.bilan_csv.supprimer_operation()
                self.vue_bilan().actualiser_liste_recettes()
            else:
                self.vue_bilan().acutaliser_liste_depenses()
        else:
            self.vue_bilan().message_erreur_suppression()

