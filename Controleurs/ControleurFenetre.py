class ControleurFenetre:

    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.vue_bon_commande = None

    def set_vue_bon_de_commande(self, vue_bon_de_commande):
        self.vue_bon_commande = vue_bon_de_commande

    def show_frame(self, vue):
        self.fenetre.show_frame(vue)

    def bon_commande_accueil(self, vue_accueil):
        self.vue_bon_commande.effacer_informations()
        self.show_frame(vue_accueil)
