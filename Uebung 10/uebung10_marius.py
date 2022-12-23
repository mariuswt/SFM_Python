# Prof. Dr. Christian Cseh, Fakultät Wirtschaftsingenieurwesen
# SFM2, http://moodle.hs-esslingen.de/moodle/ Seite 1
# SFM2 Python Programmierung
# Übung 10
# Aufgabe 1
# Verändern Sie die Klasse „Auto“ aus der letzten Übung 9, Aufgabe 1:
# - Schützen Sie die Instanzvariable „Kilometerstand“ als private Variable
# durch eine entsprechende property.
# Ergänzen Sie die vorhandenen Instanzvariablen um:
# - eine Klassenvariable „automatik“, die im Konstruktor über einen weiteren
# Parameter von Typ bool belegt wird. Zählen Sie die neu erzeugten AutoObjekte mit und ohne Automatik.
# Schreiben Sie eine statische Methode,
# welche die Anzahl der Autos mit und ohne Automatik ausgibt.
# - eine Referenz auf ein Autoradio. Das Programm soll also zusätzlich zu der
# Klasse „Auto“ noch über eine Klasse „Autoradio“ verfügen. Der __init__()-
# Methode der Klasse „Autoradio“ soll der Markenname des Radios sowie ein
# bool-Argument übergeben werden. Dieses bestimmt, ob das Autoradio noch
# über einen CD-Player verfügt (True) oder nicht (False). Zudem soll eine
# Methode namens zeige_daten() eingebaut werden, die Informationen zu
# dem Markennamen und der Ausstattung (CD-Player) ausgibt.
# In der main()-Methode sollen zunächst drei Instanzen der Klasse Autoradio
# erzeugt werden, die sich in Markenname und Ausstattung (CD-Player)
# unterscheiden. Erzeugen Sie im Anschluss noch drei Instanzen der Klasse Auto
# und weisen Sie ihnen unterschiedliche Attribute und Autoradios zu. Lassen Sie
# sich zum Schluss noch die Daten aller Autos mittels der Methode zeige_daten()
# ausgeben.
class Autoradio:
    def __init__(self, markenname: str, cd_player: bool):
        self.markenname = markenname
        self.cd_player = cd_player

    def zeige_daten(self):
        print(f"Radiomarke : {self.markenname}"
              f"CD-Player  : {self.cd_player}")


class Auto:
    def __init__(self, marke: str, kilometerstand: int, farbe: str, leistung: int, anzahl_tueren: int,
                 automatik: bool, autoradio: Autoradio):
        self.marke: str = marke  # public
        self.__kilometerstand: int = kilometerstand  # private
        self._farbe: str = farbe  # protected
        self.leistung: int = leistung
        self.anzahl_tueren: int = anzahl_tueren
        self.automatik: bool = automatik
        self.autoradio = autoradio

    def zeige_daten(self):
        print(f"\n{self.marke}\n"
              f"{self.__kilometerstand}\n"
              f"{self._farbe}\n"
              f"{self.leistung}\n"
              f"{self.anzahl_tueren}\n"
              f"Automatik = {self.automatik}\n")

    def strecke_fahren(self, kilometer):
        self.__kilometerstand += kilometer

    @property
    def kilometerstand(self):
        return self.__kilometerstand

    @kilometerstand.setter
    def kilometerstand(self, value):
        self.__kilometerstand = value

    @staticmethod
    def automatik_zaehlen(args):
        counter_automatik, counter_ohne_automatik = 0, 0
        for auto in args:
            if auto.automatik:
                counter_automatik += 1
            else:
                counter_ohne_automatik += 1
        print(f"Automatik:  {counter_automatik}\n"
              f"Ohne Autom.:{counter_ohne_automatik}")


def main_auto():
    radio = Autoradio("Yamaha", True)
    a = Auto("VW", 100, "gruen", 100, 2, True, radio)
    b = Auto("Audi", 100000, "blau", 100, 22, False, radio)

    autos = [Auto("VW", 100, "gruen", 100, 2, True, radio),
             Auto("Audi", 100000, "blau", 100, 22, False, radio),
             Auto("Porsche", 1000, "silber", 100, 22, True, radio)]

    autos[0].strecke_fahren(500)
    autos[1].strecke_fahren(50)

    for auto in autos:
        auto.zeige_daten()

    autos[0].automatik_zaehlen(autos)


#main_auto()


# Aufgabe 2
# Implementieren Sie eine Klasse Schrank mit den Instanzvariablen name für den
# Modellnamen, einem Tupel abmessung für die Breite, Tiefe und Höhe und
# preis für den Preis. Erstellen Sie 2 statische Methoden für zwei
# Einheitsschränke sowie für einen Konstruktor für einen allgemeinen
# Schranktyp. Schreiben Sie neben den notwendigen Getter- und SetterMethoden noch die folgenden Methoden:
# • getVolumen()
# Berechnen des Volumens eines Schrankes.
# • getPreis()
# Berechnen des Preises eines Schrankes über die Formel preis = cbm*100.-€
# aus dem Volumen.
# • getInfo()
# Rückgabe der vollständigen Schrankeigenschaften als Zeichenkette.
# • getAnzahl()
# Rückgabe der Anzahl der definierten Schränke mit Hilfe der Klassenvariablen
# zaehler.
# Testen Sie anschließend diese Klasse mit mehreren definierten
# Schrankobjekten.

class Schrank:
    zaehler = 0

    def __init__(self, modellname, breite, tiefe, hoehe):
        self.name = modellname
        self.__abmessung = (breite, tiefe, hoehe)
        self.__preis = self.getPreis()
        Schrank.zaehler += 1

    @staticmethod
    def einheitsschrank1():
        print(f"Das ist ein normaler Standartschrank: {'Malmoe'}, {'30x100x200'}, {199}€")
        Schrank.zaehler += 1

    @staticmethod
    def einheitsschrank2():
        print(f"Das ist ein normaler Standartschrank: {'Paloe'}, {'50x50x100'}, {79}€")
        Schrank.zaehler += 1

    def getVolumen(self):
        return (self.__abmessung[0] * self.__abmessung[1] * self.__abmessung[2]) / 1000000

    def getPreis(self):
        return self.getVolumen() * 100

    def get__abmessung(self):
        return self.__abmessung

    def get__preis(self):
        return self.__preis

    def getInfo(self):
        return (f"Name : {self.name}\n"
                f"Abmessungen b,t,h : {self.get__abmessung()}\n"
                f"Preis : {self.get__preis()}")

    @classmethod
    def getAnzahl(cls):
        return Schrank.zaehler


def main_schrank():
    schrank1 = Schrank("Schrank1", 30, 40, 100)
    schrank2 = Schrank("Schrank2", 100, 100, 200)

    print(schrank1.getInfo())
    print(schrank2.getInfo())
    Schrank.einheitsschrank1()
    Schrank.einheitsschrank2()

    print(Schrank.getAnzahl())

main_schrank()

