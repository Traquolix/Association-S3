from metier import Adherent
from metier import Laboratoire
from metier import StockageAdhérentCsv

stock = StockageAdhérentCsv.StockageAdherentCsv()
stock.initialiserfichier()


a = Adherent.Adherent("paol","luap")
a.setLaboratoire(Laboratoire.Laboratoire("ls2n"))


adherents = stock.lirefichier()

for row in adherents:
    print(row)

stock.ecrirefichier(a)

print(stock.contientAdherents(a))
