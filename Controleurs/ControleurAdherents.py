class ControleurAdherents:

    def __init__(self,vue, adherentsCsv):
        self.vue = vue
        self.adherentsCsv = adherentsCsv

    def refreshList(self):
        self.vue.initialiserVue()