import os

import sys
import os.path
import reportlab
from pathlib import Path
import datetime
import pathlib
from reportlab.pdfgen import canvas
pathlib.Path(__file__).parent.absolute()

class GenererFacture:

    def genererFacture(path, facture):
        test2 = "Dans ma ville"
        test3 = "Mon université"
        test4 = "Dans ma ville"
        prenom = "Jean"
        nom = "Benois"
        typeTarif = "tarif étudiant"

        image = 'image/atala_logo.png'
        compt = 155

        c = canvas.Canvas("test.pdf", pagesize=(210, 297), bottomup=0)
        c.translate(10, 40)
        c.scale(1, -1)
        c.drawImage(image, 0, 0, width=70, height=45)
        c.scale(1, -1)
        c.translate(-10, -40)
        c.setFont("Helvetica-Bold", 7)
        c.drawCentredString(135, 10, "Association pour le Traitement")
        c.setFont("Helvetica-Bold", 7)
        c.drawCentredString(127, 17, "Automatique des Langues")
        c.setFont("Helvetica-Bold", 5)
        c.drawCentredString(125, 25, "45 rue d'Ulm")
        c.drawCentredString(125, 31, "75230 Paris Cedex 5")
        c.setFont("Helvetica-Bold", 4)
        c.drawCentredString(125, 37, "Siret : 393 902 721 00017")
        c.setFont("Helvetica-Bold", 8)
        c.drawString(10, 65, "Mémoire valant facture numéro " + facture.get_numFacture())
        c.setFont("Helvetica-Bold", 5)
        c.drawString(10, 75, "ATALA : Association pour le Traitement Automatique des Langues")
        c.setFont("Helvetica-Bold", 4)
        c.drawString(10, 85,
                     "Non astreint à l'inscription au registre de commerce, T.V.A non applicable, article 293 B du CGI")
        c.setFont("Helvetica-Bold", 4)
        c.drawString(10, 120, "Mémoire")
        c.drawString(66, 110, test2)
        c.drawString(66, 115, test3)
        c.drawString(50, 120, "DOIT :    " + test4)

        c.drawString(10, 150,"La somme de " + facture.get_montant() + " €, cotisation à l'ATALA pour l'année " + str(datetime.date.year) + " de " + facture.get_nbAdh() + " adhérent : ")
        for i in range(8):  # a remplacer par un for each
            c.drawString(10, compt, "- " + nom + " - " + prenom + " - " + typeTarif + " -")
            compt += 5
        c.setFont("Helvetica-Bold", 5)
        c.drawCentredString(105, compt + 5, "correspondant au bon de commande : " + facture.get_refBdc())
        c.setFont("Helvetica-Bold", 4)
        c.drawRightString(180, compt + 20, "À Nantes, le " + str(datetime.date.day) + "/" + str(datetime.date.month) + "/" + str(datetime.date.year))
        c.drawRightString(180, compt + 40, "Pour l'ATALA, ")
        c.drawRightString(180, compt + 45, "La trésorière, ")
        c.drawRightString(180, compt + 50, "Solen QUINIOU ")

        c.line(10, compt + 80, 200, compt + 80)

        # End the Page and Start with new
        c.showPage()
        # Saving the PDF
        c.save()