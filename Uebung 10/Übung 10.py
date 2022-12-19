# Aufgabe 1
class Auto:
    anzahlAutomatik = 0
    anzahlNichtAutomatik = 0

    def __init__(self, kilometerstand, marke, farbe, leistung, anzahlTueren, automatik, autoradio):
        self.__kilometerstand = kilometerstand
        self.marke:str = marke
        self.farbe:str = farbe
        self.leistung = leistung
        self.anzahlTueren = anzahlTueren
        self.automatik:bool = automatik
        self.autoradio:Autoradio=autoradio
        if (automatik):
            Auto.anzahlAutomatik +=1
        else:
            Auto.anzahlNichtAutomatik +=1

    @staticmethod
    def zeigeAutos():
        print("Autos mit Automatik: "+str(Auto.anzahlAutomatik)+"\nAutos OHNE Automatik: "+str(Auto.anzahlNichtAutomatik))

    def zeige_daten(self):
        print("Kilometerstand: " + str(
            self.__kilometerstand) + "\nMarke: " + self.marke + "\nFarbe: " + self.farbe + "\nLeistung: " + str(
            self.leistung) + "\nAnzahl der Türen: " + str(self.anzahlTueren) + "\nAutomatik: " + str(
            self.automatik) + "\nAutoradio: " + self.autoradio.zeige_daten() + "\n\n")

    def strecke_fahren(self,kilometer):
        self.__kilometerstand +=kilometer

class Autoradio():
    def __init__(self,marke,hatCDPlayer):
        self.marke=marke
        self.hatCDPlayer:bool = hatCDPlayer

    def zeige_daten(self):
        #print("Marke: "+str(self.marke)+"\nHat einen CD Player: "+str(self.hatCDPlayer))
        return str("Marke: "+str(self.marke)+"\nHat einen CD Player: "+str(self.hatCDPlayer))


autoradioJBL = Autoradio("JBL",False)
autoradioBang = Autoradio("Bang&Olufsen",True)

auto1 = Auto(10000,"Audi","schwarz",222,5,True,autoradioJBL)
auto2 = Auto(100000,"VW","rot",112,3,False,autoradioBang)

auto1.zeige_daten()
auto2.zeige_daten()

auto1.strecke_fahren(999)
auto1.zeige_daten()

auto2.strecke_fahren(9999)
auto2.zeige_daten()

# Aufgabe 2
# class Schrank:
#     anzahlSchraenke = 0
#
#     def __init__(self, name, abmessung, preis):
#         self.__modellname = name
#         self.__abmessung: tuple = abmessung
#         self.__preis = preis
#         Schrank.anzahlSchraenke += 1
#
#     @staticmethod
#     def einheitsschrank1():
#         return Schrank("Ikea", (2, 0.8, 2), 699)
#
#     @staticmethod
#     def einheitsschrank2():
#         return Schrank("Design Schreiner", (1.8, 0.75, 1.9), 1399)
#
#     def get_modellname(self):
#         return self.__modellname
#
#     def get_abmessung(self):
#         return self.__abmessung
#
#     def get_preis(self):
#         return self.__preis
#
#     def set_modellname(self, neuerName):
#         self.__modellname = neuerName
#
#     def set_abmessung(self, neueAbmessung):
#         self.__abmessung = neueAbmessung
#
#     def set_preis(self, neuerPreis):
#         self.__preis = neuerPreis
#
#     modellname = property(get_modellname, set_modellname)
#     abmessung = property(get_abmessung, set_abmessung)
#     preis = property(get_preis, set_preis)
#
#     def getVolumen(self):
#         return self.abmessung[0] * self.abmessung[1] * self.abmessung[2]
#
#     def getVolumenPreis(self):
#         self.__preis = self.getVolumen() * 100
#         return self.preis
#
#     def getInfo(self):
#         return "Modellname: " + self.modellname + " Abmessungen: " + str(self.abmessung) + (
#                     " Preis: " + str(self.preis) + " Euro")
#
#     def getAnzahl(self):
#         return Schrank.anzahlSchraenke
#
#
# eigenerSchrank = Schrank("Eigenbau", (1, 2, 3), 50)
# eigenerSchrank2 = Schrank("Geklaut", (1.5, 1, 3), 100)
# eigenerSchrank3 = Schrank("Sperrmüll", (1, 1, 1), 0)
# fertigSchrank = Schrank.einheitsschrank1()
# fertigSchrank2 = Schrank.einheitsschrank2()
#
# print(fertigSchrank.getInfo())
# print(eigenerSchrank.modellname)
# print(eigenerSchrank.getVolumen())
# print(eigenerSchrank.getInfo())
# print(eigenerSchrank.getAnzahl())