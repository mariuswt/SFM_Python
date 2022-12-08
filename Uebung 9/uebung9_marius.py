# Übung 9

# Aufgabe 1
# Schreiben Sie eine Klasse „Auto“ in Python. Initialisieren Sie im Konstruktor die
# folgenden Instanzvariablen:
# Kilometerstand, Marke, Farbe, Leistung, Anzahl der Türen.
# Definieren Sie die Methoden
# zeige_daten(), welche de Instanzvariablen auf dem Bildschirm ausgibt und
# strecke_fahren(kilometer), die den Kilometerstand um den Wert des
# Parameters erhöht.
# Schreiben Sie auch eine main()_Methode, die 2 Autos anlegt, beide Autos
# fahren lässt (Kilometerstand erhöht sich) und die jeweiligen Fahrzeug-Daten
# ausgibt.


class Auto:
    def __init__(self, marke, kilometerstand, farbe, leistung, anzahl_tueren):
        self.marke: str = marke  # public
        self._kilometerstand: int = kilometerstand  # protected
        self.__farbe: str = farbe  # private
        self.leistung: int = leistung
        self.anzahl_tueren: int = anzahl_tueren

    def zeige_daten(self):
        print(f"\n{self.marke}\n"
              f"{self._kilometerstand}\n"
              f"{self.__farbe}\n"
              f"{self.leistung}\n"
              f"{self.anzahl_tueren}\n")

    def strecke_fahren(self, kilometer):
        self._kilometerstand += kilometer

    @property
    def kilometerstand(self):
        print(self._kilometerstand)
        return self._kilometerstand

    @kilometerstand.setter
    def kilometerstand(self, value):
        self.kilometerstand = value


def main_auto():
    a = Auto("VW", 100, "gruen", 100, 2)
    b = Auto("Audi", 100000, "blau", 100, 22)

    a.strecke_fahren(500)
    b.strecke_fahren(50)

    a.zeige_daten()
    b.zeige_daten()


main_auto()


# Aufgabe 2
# Verändern Sie das Python-Programm Bank aus Übung 7, Aufgabe 2. Verteilen
# Sie die vorhandenen Funktionen in ein Objekt-orientiertes Design mit 3
# Klassen: Bank, Konto und Menü. Überlegen Sie, welche Instanzvariable jede
# der 3 Klassen haben soll.

class Menue:
    def __init__(self):
        self.menuewahl = 1
        self.bank = Bank("Kapitalbank")

        # 1. Konto neu anlegen
        # 2. Einzahlen
        # 3. Abheben
        # 4. Zinsen gutschreiben
        # 5. Kontendaten ausgeben

    def menue_anzeigen(self):
        self.menuewahl = int(input("\n0. Beenden\n"
                                   "1. Konto neu anlegen\n"
                                   "2. Einzahlen\n"
                                   "3. Abheben\n"
                                   "4. Zinsen gutschreiben\n"
                                   "5. Kontendaten ausgeben\n\n"))
        return self.menuewahl

    def konto_anlegen(self):
        inhaber = str(input("Kontoinhaber: "))
        blz = input("BLZ: ")
        kontonummer = input("Kontonummer: ")
        kontostand = 0.00
        zinssatz = float(input("Zinssatz: "))
        self.bank.konto_anlegen(Konto(inhaber, blz, kontonummer, kontostand, zinssatz))

    def konto_einzahlen(self):
        betrag = abs(float(input("Betrag zum Einzahlen: ")))
        self.bank.konto_einzahlen(betrag)

    def konto_abheben(self):
        betrag = abs(float(input("Betrag zum Auszahlen: ")))
        self.bank.konto_abheben(betrag)

    def zinsen_gutschreiben(self):
        self.bank.konto_zinsen_gutschreiben()

    def konto_anzeigen(self):
        self.bank.alle_kontodaten_ausgeben()


class Konto:
    def __init__(self, kontoinhaber, bankleitzahl, kontonummer, kontostand, zinssatz):
        self.kontoinhaber = kontoinhaber
        self.bankleitzahl = bankleitzahl
        self.kontonummer = kontonummer
        self.__kontostand = kontostand
        self.zinssatz = zinssatz

    def einzahlen(self, betrag):
        self.__kontostand += betrag

    def abheben(self, betrag):
        if self.__kontostand - betrag >= 0:
            self.__kontostand -= betrag
        else:
            print("Kontostand wird negativ!")

    def zinsen_gutschreiben(self):
        self.__kontostand = round(self.__kontostand * (1 + (self.zinssatz / 100)), 2)

    def kontodaten_ausgeben(self):
        print(self.kontoinhaber,
              self.bankleitzahl,
              self.kontonummer,
              self.__kontostand,
              self.zinssatz)


class Bank:
    def __init__(self, name):
        self.__konto = None
        self.name = name

    def konto_anlegen(self, konto):
        self.__konto = konto

    def konto_einzahlen(self, betrag):
        self.__konto.einzahlen(betrag)

    def konto_abheben(self, betrag):
        self.__konto.abheben(betrag)

    def konto_zinsen_gutschreiben(self):
        self.__konto.zinsen_gutschreiben()

    def alle_kontodaten_ausgeben(self):
        self.__konto.kontodaten_ausgeben()


first_run = True
eingabe = 1
menue = Menue()
while eingabe != 0:

    eingabe = menue.menue_anzeigen()
    if eingabe == 0:
        break
    if eingabe == 1 or first_run:
        menue.konto_anlegen()
        first_run = False
    if eingabe == 2:
       menue.konto_einzahlen()
    if eingabe == 3:
        menue.konto_abheben()
    if eingabe == 4:
        menue.zinsen_gutschreiben()
    if eingabe == 5:
        menue.konto_anzeigen()

# Schreiben Sie ein Python-Script, das ein Bankkonto verwaltet und
# verschiedene selbstdefinierte Funktionen verwendet.
# Dabei soll ein Konto die folgenden Eigenschaften (Variable) besitzen:
# Kontoinhaber, Bankleitzahl, Kontonummer, Kontostand und Zinssatz.
# Prof. Dr. Christian Cseh, Fakultät Wirtschaftsingenieurwesen
# SFM2, http://moodle.hs-esslingen.de/moodle/ Seite 2
# Der Benutzer soll über ein einfaches Konsolenmenü die möglichen
# Operationen auswählen können:
# 1. Konto neu anlegen
# 2. Einzahlen
# 3. Abheben
# 4. Zinsen gutschreiben
# 5. Kontendaten ausgeben
# Dabei soll immer nur ein Konto gleichzeitig aktiv sein. D.h. wenn der
# Benutzer die Option 1 „Konto neu anlegen“ wählt, werden die Eigenschaften
# neu abgefragt, die alten Werte überschrieben und der Kontostand auf 0.-
# gesetzt. Achten Sie darauf, dass der Kontostand nicht negativ werden darf.
