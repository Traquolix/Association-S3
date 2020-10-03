from locals import *
from EventHandler import *

class GUIManager:
    margins = 50
    associationName = "Association pour le Traitement Automatique des Langues"
    associationAdress = "45 rue d'Ulm"
    associationTown = "75230 Paris Cedex 5"
    associationSiret = "393 902 721 00017"

    def __init__(self):
        self.fields = []
        self.window = Tk()
        self.evenHandler = EventHandler(self.window, self.fields)

        self.formGeneration()

    def formGeneration(self):
        self.window.title("Générateur de bon de commande")
        self.window.geometry('400x400')
        self.window.configure(background="white")

        a = Label(self.window, text="Numéro du bon de commande : ").grid(row=0, column=0)
        b = Label(self.window, text="Nom du destinataire : ").grid(row=1, column=0)
        c = Label(self.window, text="Adresse du destinataire").grid(row=2, column=0)
        d = Label(self.window, text="Date du jour").grid(row=3, column=0)

        a1 = Entry(self.window)
        self.fields.insert(0, a1)
        a1.grid(row=0, column=1)

        a2 = Entry(self.window)
        self.fields.insert(1, a2)
        a2.grid(row=1, column=1)

        a3 = Entry(self.window)
        self.fields.insert(2, a3)
        a3.grid(row=2, column=1)

        self.fields.insert(3,
                           DateEntry(self.window, locale='fr_FR', date_pattern='dd/mm/y', width=12, background='grey',
                                     foreground='white', borderwidth=2))
        self.fields[3].grid(row=3, column=1)

        btn = ttk.Button(self.window, text="Submit", command=self.generatePDF).grid(row=4, column=1)

        self.window.mainloop()

    def generatePDF(self):
        pdf = FPDF()

        pdf.add_page()

        pdf.image('C:\\Users\\Milo\\Desktop\\logo.png', 10, 10, 54.2, 35.2, "png")
        pdf.set_font('Arial', 'B', 22)

        pdf.cell(75, 30, "", 0, 0, 'M')  # Spacing

        pdf.cell(0, 30, "Bon de commande N°" + self.fields[0].get(), 0, 1, 'L')
        pdf.set_font('Arial', 'B', 10)

        pdf.ln(20)

        pdf.multi_cell(((pdf.w - (pdf.r_margin + pdf.l_margin)) / 2)+35, 10, "\n  " + self.associationName + "\n  " + self.associationAdress + "\n  " + self.associationTown + "\n  Siret : " + self.associationSiret + "\n", 1, 'L', 0)
        pdf.multi_cell(((pdf.w - (pdf.r_margin + pdf.l_margin)) / 2)-35, 30, "  A :        " + self.fields[1].get() + "\n  Adresse :     " + self.fields[2].get(), 1, 'L', 0, 0)

        pdf.output('C:\\Users\\Milo\\Desktop\\tuto1.pdf', 'F')