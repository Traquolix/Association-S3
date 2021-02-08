import os

import sys
import os.path
import reportlab
from pathlib import Path
import datetime
import pathlib
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
pathlib.Path(__file__).parent.absolute()


class GenererFacture:

    @staticmethod
    def genererFacture(path,facture):
        image = 'modele/image/atala_logo.png'
        compt = 425
        tab_adh = facture.get_adherents()
        taille = len(tab_adh)
        now = datetime.datetime.now()
        separateur = 0

        c = canvas.Canvas(path, pagesize=A4, bottomup=0)
        c.translate(15, 150)
        c.scale(1, -1)
        c.drawImage(image, 0, 0, width=180, height=125)
        c.scale(1, -1)
        c.translate(-15, -120)
        c.setFont("Helvetica-Bold", 23)
        c.drawCentredString(420, 10, "Association pour le Traitement")
        c.setFont("Helvetica-Bold", 23)
        c.drawCentredString(394, 30, "Automatique des Langues")
        c.setFont("Helvetica-Bold", 19)
        c.drawCentredString(420, 60, "45 rue d'Ulm")
        c.drawCentredString(420, 80, "75230 Paris Cedex 5")
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(350, 110, "Siret : 393 902 721 00017")
        c.setFont("Helvetica-Bold", 26)
        c.drawString(10, 180, "Mémoire valant facture numéro " + facture.get_numFacture())
        c.setFont("Helvetica-Bold", 15)
        c.drawString(10, 210, "ATALA : Association pour le Traitement Automatique des Langues")
        c.setFont("Helvetica-Bold", 11)
        c.drawString(10, 240, "Non astreint à l'inscription au registre de commerce, T.V.A non applicable, article 293 B du CGI")
        c.setFont("Helvetica-Bold", 16)
        c.drawString(25, 350, "Mémoire")
        c.drawString(315, 290, facture.get_nom_organisation())
        c.drawString(315, 320, facture.get_adresse_organisation())
        c.drawString(250, 350, "DOIT :    " + facture.get_ville_organisation())
        c.setFont("Helvetica-Bold", 13)
        c.drawString(10, 400, "La somme de " + facture.get_montant() + " €, cotisation à l'ATALA pour l'année " + now.strftime("%Y") + " de " + str(facture.get_nbAdh()) + " adhérent : ")

        if taille <= 10:
            c.setFont("Helvetica-Bold", 15)
            for adh in tab_adh:
                c.drawString(10, compt, "- " + adh[0] + " - " + adh[1] + " - " + adh[2] + " - ")
                compt += 20

        if taille > 10 and taille <= 20:
            c.setFont("Helvetica-Bold", 12)
            for adh in tab_adh:
                if separateur % 2 == 0:
                    c.drawString(10, compt, "- " + adh[0] + " - " + adh[1] + " - " + adh[2] + " - ")
                if separateur % 2 == 1:
                    c.drawString(300, compt, "- " + adh[0] + " - " + adh[1] + " - " + adh[2] + " - ")
                    compt += 20

        if taille > 20 and taille <= 40:
            c.setFont("Helvetica-Bold", 9)
            for adh in tab_adh:
                if separateur % 3 == 0:
                    c.drawString(10, compt, "- " + adh[0] + " - " + adh[1] + " - " + adh[2] + " - ")
                if separateur % 3 == 1:
                    c.drawString(210, compt, "- " + adh[0] + " - " + adh[1] + " - " + adh[2] + " - ")
                if separateur % 3 == 2:
                    c.drawString(410, compt, "- " + adh[0] + " - " + adh[1] + " - " + adh[2] + " - ")
                    compt += 20
                separateur = separateur + 1

        c.setFont("Helvetica-Bold", 19)
        c.drawCentredString(300, compt + 20, "correspondant au bon de commande : " + facture.get_refBdc())
        c.setFont("Helvetica-Bold", 14)
        c.drawRightString(550, compt + 50, "À Nantes, le " + now.strftime("%d/%m/%Y"))
        c.drawRightString(550, compt + 70, "Pour l'ATALA, ")
        c.drawRightString(550, compt + 90, "La trésorière, ")
        c.drawRightString(550, compt + 110, "Solen QUINIOU ")

        c.line(10, compt + 120, 580, compt + 120)

        # End the Page and Start with new
        c.showPage()
        # Saving the PDF
        c.save()