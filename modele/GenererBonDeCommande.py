import os

import sys
import os.path
import reportlab
from pathlib import Path
import datetime
import pathlib
from reportlab.pdfgen import canvas
pathlib.Path(__file__).parent.absolute()


class GenererBonDeCommande:

    @staticmethod
    def genererBonDeCommande(path, bon_de_commande):

        c = canvas.Canvas("invoice.pdf", pagesize=(200, 250), bottomup=0)
        c.translate(10, 40)
        c.scale(1, -1)
        c.drawImage(path, 0, 0, width=50, height=30)
        c.scale(1, -1)
        c.translate(-10, -40)
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(125, 20, "BON DE COMMANDE")
        c.line(70, 22, 180, 22)
        c.setFont("Helvetica-Bold", 5)
        c.drawCentredString(125, 30, "45 rue d'Ulm")
        c.drawCentredString(125, 35, "75230 Paris Cedex 5")
        c.setFont("Helvetica-Bold", 6)
        c.drawCentredString(125, 42, "Siret : 393 902 721 00017")
        c.line(5, 45, 195, 45)
        c.setFont("Courier-Bold", 4)
        c.drawCentredString(100, 55, "Association pour le Traitement Automatique des Langues")

        c.roundRect(15, 63, 170, 40, 10, stroke=1, fill=0)
        c.setFont("Times-Bold", 5)
        c.drawRightString(70, 70, "COMMANDE N°:" + bon_de_commande.get_numero_bon())
        c.drawRightString(70, 80, "DATE :" + str(datetime.date.day) + "/" + str(datetime.date.month) + "/" + str(datetime.date.year))
        c.drawRightString(70, 90, "NOM DU CLIENT :" + bon_de_commande.get_nom_labo())
        c.drawRightString(70, 100, "ADRESSE:" + bon_de_commande.get_adresse_labo())

        c.roundRect(15, 108, 170, 130, 10, stroke=1, fill=0)
        c.line(15, 120, 185, 120)
        c.drawCentredString(30, 118, "Désignation")
        c.drawCentredString(80, 118, "Prix unitaire")
        c.drawCentredString(110, 118, "Quantité")
        c.drawCentredString(150, 118, "Remarques")

        # Drawing table for Item Description
        c.line(15, 210, 15, 210)
        c.line(65, 108, 65, 220)
        c.line(98, 108, 98, 220)
        c.line(135, 108, 135, 220)

        c.line(15, 220, 185, 220)
        c.drawRightString(180, 235, "Signature")

        # End the Page and Start with new
        c.showPage()
        # Saving the PDF
        c.save()