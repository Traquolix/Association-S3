
from locals import *
from EventHandler import *

class GUIManager:
    margins = 50
    associationName = "Association pour le Traitement Automatique des Langues"
    associationAdress = "45 rue d'Ulm"
    associationTown = "75230 Paris Cedex 5"
    associationSiret = "393 902 721 00017"

    fileName = 'C:\\Users\\Milo\\Desktop\\MyDoc.pdf'
    documentTitle = 'Document title!'
    title = 'Tasmanian devil'
    subTitle = 'The largest carnivorous marsupial'

    textLines = [
        'The Tasmanian devil (Sarcophilus harrisii) is',
        'a carnivorous marsupial of the family',
        'Dasyuridae.'
    ]



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
        doc = SimpleInvoice(GUIManager.fileName)
        doc.invoice_info = InvoiceInfo(1023, datetime.now(), datetime.now())  # Invoice info, optional

        # Service Provider Info, optional
        doc.service_provider_info = ServiceProviderInfo(
            name='PyInvoice',
            street='My Street',
            city='My City',
            state='My State',
            country='My Country',
            post_code='222222',
            vat_tax_number='Vat/Tax number'
        )

        # Client info, optional
        doc.client_info = ClientInfo(email='client@example.com')

        # Add Item
        doc.add_item(Item('Item', 'Item desc', 1, '1.1'))
        doc.add_item(Item('Item', 'Item desc', 2, '2.2'))
        doc.add_item(Item('Item', 'Item desc', 3, '3.3'))

        # Tax rate, optional
        doc.set_item_tax_rate(20)  # 20%

        # Transactions detail, optional
        doc.add_transaction(Transaction('Paypal', 111, datetime.now(), 1))
        doc.add_transaction(Transaction('Stripe', 222, date.today(), 2))

        # Optional
        doc.set_bottom_tip("Email: example@example.com<br />Don't hesitate to contact us for any questions.")

        doc.finish()
