from metier import Adherent
from metier import Laboratoire
from data import StockageAdherentCsv

stock = StockageAdherentCsv.StockageAdherentCsv()
stock.initialiserfichier()


a = Adherent.Adherent("paol","luap")
a.setLaboratoire(Laboratoire.Laboratoire("ls2n"))


adherents = stock.lirefichier()

for row in adherents:
    print(row)

stock.ecrirefichier(a)

print(stock.contientAdherents(a))

adherents = stock.lirefichier()

for row in adherents:
    print(row)
