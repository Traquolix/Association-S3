from data.StockageLaboratoireCsv import StockageLaboratoireCsv


class ControleurFacture:

    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.laboratoire_csv = StockageLaboratoireCsv()
        self.vue_facture = None

    def set_vue_facture(self, vue_facture):
        self.vue_facture = vue_facture

    def actualiser_liste_laboratoire_noms(self):
        return sorted(self.laboratoire_csv.lire_fichier_noms())