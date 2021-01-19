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
        test = "18112385"
        test2 = "Dans ma ville"
        getsomme = "10 000"
        année = "2021"
        x = "1"
        y = "12"
        nom = "Jean Kevin"
        nom2 = " Jean Patrice"
        numbdc = "FIUZIUFZIUNHAOJIFZ"
        date = "19/01/2021"

        compt = 155

        c = canvas.Canvas("test.pdf", pagesize=(210, 297), bottomup=0)
        c.translate(10, 40)
        c.scale(1, -1)
        # c.drawImage(path, 0, 0, width=50, height=30)
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
        c.drawString(10, 65, "Mémoire valant facture numéro " + test)
        c.setFont("Helvetica-Bold", 5)
        c.drawString(10, 75, "ATALA : Association pour le Traitement Automatique des Langues")
        c.setFont("Helvetica-Bold", 4)
        c.drawString(10, 85,
                     "Non astreint à l'inscription au registre de commerce, T.V.A non applicable, article 293 B du CGI")
        c.setFont("Helvetica-Bold", 4)
        c.drawString(10, 120, "Mémoire")
        c.drawString(50, 120, "DOIT :    " + test2)
        c.drawString(10, 150,
                     "La somme de " + getsomme + " €, cotisation à l'ATALA pour l'année " + année + " de " + x + " adhérent tarif proffessionnel : ")
        for i in range(3):
            c.drawString(10, compt, "- " + nom + " -")
            compt += 5
        c.drawString(10, compt, " Et de " + y + " adhérent tarif étudiant : ")
        compt += 5
        for i in range(3):
            c.drawString(10, compt, "- " + nom2 + " -")
            compt += 5
        c.setFont("Helvetica-Bold", 5)
        c.drawCentredString(105, compt + 5, "correspondant au bon de commande : " + numbdc)
        c.setFont("Helvetica-Bold", 4)
        c.drawRightString(180, compt + 20, "À Nantes, le " + date)
        c.drawRightString(180, compt + 40, "Pour l'ATALA, ")
        c.drawRightString(180, compt + 45, "La trésorière, ")
        c.drawRightString(180, compt + 50, "Solen QUINIOU ")

        c.line(10, compt + 80, 200, compt + 80)

        # End the Page and Start with new
        c.showPage()
        # Saving the PDF
        c.save()