from modele.BilanFinancier import BilanFinancier
from data.StockageBilanFinancier import StockageBilanFinancier
from modele.Operation import Operation


class ControleurBilan:

    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.stockagebilan = StockageBilanFinancier()
        self.bilan = BilanFinancier()
        self.vue_bilan = None
        self.vue_bilan_categorie = None

    def set_vue_bilan(self, vue_bilan):
        self.vue_bilan = vue_bilan

    def set_vue_bilan_categorie(self, vue_bilan_categorie):
        self.vue_bilan_categorie = vue_bilan_categorie

    def actualiser_liste_recettes(self):
        return sorted(self.stockagebilan.lire_fichier_recettes())

    def actualiser_liste_depenses(self):
        return sorted(self.stockagebilan.lire_fichier_depenses())

    def actualiser_liste_categories(self):
        return sorted(self.stockagebilan.lire_fichier_categories())

    def actualiser_liste_categorie(self, type):
        return sorted(self.stockagebilan.lire_fichier_categorie(type))

    def ajouter_categorie(self):
        if self.vue_bilan_categorie.champ_vide():
            self.vue_bilan_categorie.message_erreur_champs_vide()
        else:
            operation = Operation()
            operation.set_type(self.vue_bilan_categorie.get_type())
            operation.set_categorie(self.vue_bilan_categorie.get_categorie())
            if not self.stockagebilan.contient_categorie(self.vue_bilan_categorie.get_categorie()):
                self.stockagebilan.ajouter_operation(operation)
                self.vue_bilan_categorie.viderChamps()
                self.vue_bilan_categorie.actualiser_liste_categories()
                self.vue_bilan.actualiser_liste_categorie(self.vue_bilan_categorie.get_type())
            else:
                self.vue_bilan_categorie.message_erreur_ajout()

    def ajouter_operation(self):

        if self.vue_bilan.champ_vide():
            self.vue_bilan.message_erreur_champs_vide()
        elif not self.vue_bilan.validation_date(self.vue_bilan.get_date()):
            self.vue_bilan.message_erreur_validation()
        elif not self.vue_bilan.validation_montant(self.vue_bilan.get_montant()):
            self.vue_bilan.message_erreur_validation()
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
                    self.vue_bilan_categorie.actualiser_liste_categories()
                else:
                    self.stockagebilan.ajouter_operation(operation)
                    self.vue_bilan.actualiser_liste_recettes()
                    self.vue_bilan.viderChamps()
                    self.vue_bilan_categorie.actualiser_liste_categories()
            else:
                self.vue_bilan.message_erreur_ajout()

    def supprimer_categorie(self):
        ligne = self.vue_bilan_categorie.get_categorie_selectionner()
        if ligne == '':
            self.vue_bilan_categorie.message_erreur_suppression()
        else:
            self.stockagebilan.supprimer_categorie(self.vue_bilan_categorie.get_categorie_selectionner())
            self.vue_bilan_categorie.actualiser_liste_categories()
            self.vue_bilan.actualiser_liste_recettes()
            self.vue_bilan.actualiser_liste_depenses()
            self.vue_bilan.actualiser_liste_categorie('recette')
            self.vue_bilan.actualiser_liste_categorie('depense')

    def supprimer_operation(self, type):
        ligne = self.vue_bilan.get_selected_operation(type)
        if ligne == '':
            self.vue_bilan.message_erreur_suppression()
        else:
            operation = Operation()
            operation.set_type(type)
            operation.set_categorie(ligne[0])
            operation.set_date(ligne[1])
            operation.set_montant(ligne[2])
            operation.set_description(ligne[3])
            if operation.get_type() == 'recette':
                self.stockagebilan.supprimer_operation(operation)
                self.vue_bilan.actualiser_liste_recettes()
                self.vue_bilan_categorie.actualiser_liste_categories()
            else:
                self.stockagebilan.supprimer_operation(operation)
                self.vue_bilan.actualiser_liste_depenses()
                self.vue_bilan_categorie.actualiser_liste_categories()

    def modifier_operation(self, type):
        if self.vue_bilan.get_selected_operation(type) is None:
            self.vue_bilan.message_erreur_suppression()
        elif self.vue_bilan.champ_vide():
            self.vue_bilan.message_erreur_champs_vide()
        else:
            ligne = self.vue_bilan.get_selected_operation(type)
            operation1 = Operation()
            operation1.set_type(type)
            operation1.set_categorie(ligne[0])
            operation1.set_date(ligne[1])
            operation1.set_montant(ligne[2])
            operation1.set_description(ligne[3])

            operation2 = Operation()
            operation2.set_type(operation1.get_type())
            operation2.set_categorie(operation1.get_categorie())
            operation2.set_date(self.vue_bilan.get_date())
            operation2.set_montant(self.vue_bilan.get_montant())
            operation2.set_description(self.vue_bilan.get_description())

            if operation1.get_type() == 'recette':
                self.stockagebilan.supprimer_operation(operation1)
                self.stockagebilan.ajouter_operation(operation2)
                self.vue_bilan.actualiser_liste_recettes()
                self.vue_bilan.viderChamps()
                self.vue_bilan_categorie.actualiser_liste_categories()
            else:
                self.stockagebilan.supprimer_operation(operation1)
                self.stockagebilan.ajouter_operation(operation2)
                self.vue_bilan.actualiser_liste_depenses()
                self.vue_bilan.viderChamps()
                self.vue_bilan_categorie.actualiser_liste_categories()

