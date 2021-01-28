import os

import sys
import os.path
import reportlab
from pathlib import Path
import datetime
import pathlib
from reportlab.pdfgen import canvas

pathlib.Path(__file__).parent.absolute()
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm


class GenererBonDeCommande:

    @staticmethod
    def genererBonDeCommande(path, bon_de_commande):
        image = 'vue/images/atala_clean.png'

        c = canvas.Canvas(path, pagesize=A4, bottomup=0)
        # top
        c.translate(15, 150)
        c.scale(1, -1)
        c.drawImage(image, 0, 0, width=295 * (2 / 3), height=197 * (2 / 3))
        c.scale(1, -1)
        c.translate(-15, -120)
        c.setFont("Helvetica-Bold", 17)
        c.drawString(250, 50, "BON DE COMMANDE N°" + bon_de_commande.get_numero_bon())
        # reset origin
        c.translate(15, 120)
        c.translate(-15, -150)
        # Interface haut
        c.line(20, 160, 570, 160)
        c.line(20, 260, 570, 260)
        c.line(20, 160, 20, 260)
        c.line(570, 160, 570, 260)
        c.line(285, 160, 285, 260)
        # top left text
        c.setFont("Courier-Bold", 11)
        c.drawString(35, 188, "Association pour le Traitement")
        c.drawString(35, 197, "Automatique des Langues")
        c.setFont("Helvetica-Bold", 11)
        c.drawString(35, 215, "45 rue d'Ulm")
        c.drawString(35, 230, "75230 Paris Cedex 5")
        c.setFont("Helvetica-Bold", 11)
        c.drawString(35, 245, "Siret : 393 902 721 00017")

        # top right text
        c.drawString(290, 190, "A :            " + bon_de_commande.get_nom_organisation())
        c.drawString(290, 205, "Adresse :            " + bon_de_commande.get_adresse())

        # date
        c.setFont("Helvetica-Bold", 11)
        c.drawString(20, 280, "Date : " + datetime.date.today().strftime("%d/%d/%Y"))

        # Categories
        c.setFillColorRGB(128, 128, 128, None)
        c.rect(20, 290, 550, 15, fill=1)
        c.setFillColorRGB(0, 0, 0, None)
        c.drawString(22, 301, "Désignation")
        c.line(200, 290, 200, 305)
        c.drawString(205,301, "Prix unitaire")
        c.line(275, 290, 275, 305)
        c.drawString(295, 301, "Quantité")
        c.line(365, 290, 365, 305)
        c.drawString(375, 301, "Montant HT")
        c.line(450, 290, 450, 305)
        c.drawString(480, 301, "Remarques")

        adh = bon_de_commande.get_adherents()
        lastvalue = 0

        c.setFont("Helvetica", 11)
        for x in range(len(bon_de_commande.get_adherents())):
            c.rect(20, 320 + (x*70), 550, 70)
            c.line(200, 320 + (x*70), 200, 390 + (x*70))
            c.line(275, 320 + (x*70), 275, 390 + (x*70))
            c.line(365, 320 + (x*70), 365, 390 + (x*70))
            c.line(450, 320 + (x*70), 450, 390 + (x*70))

            courant = adh[x]

            nomprenom = courant[0]

            c.drawString(22, 358 + (x*70), nomprenom[0] + " " + nomprenom[1])
            c.drawString(205, 358 + (x*70), courant[1])
            c.drawString(280, 358 + (x*70), courant[2])
            c.drawString(370, 358 + (x*70), courant[3])
            c.drawString(455, 358 + (x*70), courant[4])
            lastvalue = 390 + (x*70)

        c.rect(200, lastvalue + 10, 250, 25)
        c.rect(250, lastvalue + 35, 200, 25)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(205, lastvalue + 27, "TOTAL €   HT")
        c.drawRightString(445 , lastvalue + 27, bon_de_commande.get_montant_total())
        c.drawString(255, lastvalue + 52, "TTC")
        c.setFont("Helvetica", 11)
        c.drawString(20, lastvalue + 52, "Conditions de paiement :")
        c.setFont("Courier-Bold", 9)
        c.drawString(20, lastvalue + 90, "Solen Quiniou, Trésorière adjointe de l'ATALA.")

        # End the Page and Start with new
        c.showPage()
        # Saving the PDF
        c.save()
