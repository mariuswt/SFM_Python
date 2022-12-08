# Aufgabe 2
"""
Aufgabe 2
Verändern Sie das Python-Programm Bank aus Übung 7, Aufgabe 2. Verteilen Sie die vorhandenen Funktionen in ein
Objekt-orientiertes Design mit 3 Klassen: Bank, Konto und Menü. Überlegen Sie, welche Instanzvariable jede der 3 Klassen
haben soll.
"""

class Bank:
    def main():
        while (True):
            dictionary_konten ={}
            auswahl_konto = None
            try:
                auswahl = Menü.Menü()
                if (auswahl == 1):
                    k = Konto.konto_anlegen()
                    dictionary_konten[k.kontonummer] = k
                elif (auswahl == 2):
                    betrag = float(input("Betrag: "))
                    k.einzahlen(betrag)
                elif (auswahl == 3):
                    betrag = float(input("Betrag: "))
                    k.abheben(betrag)
                elif (auswahl == 4):
                    k.zinsen_gutschrift()
                elif (auswahl == 5):
                    k.daten_ausgabe()
                elif (auswahl == 7):
                    break
            except ValueError:
                print("Wählen Sie bitte eine Zahl von 1 bis 5!")


class Konto:
    anzahl_konto = 0
    def __init__(self, kontoinhb,kontonr,kontostnd, zinsen):
        self.kontoinhaber = kontoinhb
        self.kontonummer = kontonr
        self.saldo = kontostnd
        self.zinssatz = zinsen
        Konto.anzahl_konto += 1
        self.konto_anzahl = Konto.anzahl_konto

    def einzahlen(self,betrag):
        try:
            self.saldo += abs(betrag)
        except ValueError:
            print("Es können nur Zahlen eingegeben werden")

    def abheben(self, betrag):
        try:
            if (self.saldo - abs(betrag) < 0):
                print(("Nicht genügend Saldo auf dem Konto!"))
            else:
                self.saldo -= abs(betrag)
        except ValueError:
            print("Es können nur Zahlen eingegeben werden")

    def zinsen_gutschrift(self):
        try:
            zinsen = self.saldo * (self.zinssatz / 100)
            print("Zinsgutschrift: ", zinsen)
            self.saldo += zinsen
        except ValueError:
            print("Es können nur Zahlen eingegeben werden")

    def daten_ausgabe(self):
        print("Kontodaten\n=========")
        print("Kontoinhaber: ", self.kontoinhaber)
        print("Kontonummer: ", self.kontonummer)
        print("Kontoguthaben: ", self.saldo)
        print("Zinssatz: ", self.zinssatz)

    def konto_anlegen():
        kontoinhaber = input("Kontoinhaber: ")
        kontonummer = int(input("Kontonummer: "))
        saldo = float(input("Kontoguthaben: "))
        zinssatz = (float(input("Zinssatz: ")))
        return Konto (kontoinhaber,kontonummer,saldo,zinssatz)


class Menü:
    def Menü():
        print("=========")
        print("(1) Konto neu anlegen")
        print("(2) Einzahlen")
        print("(3) Abheben")
        print("(4) Zinsgutschrift")
        print("(5) Datenausgabe")
        #print("(6) Auswahl Bankkonto")
        print("(7) Beenden")
        auswahl = int(input("=========\nWählen Sie bitte eine Option aus: "))
        return auswahl

Bank.main()


"""
                    kontonr = int(input("Welches Bankkonto soll ausgewählt werden? (Bitte Kontonummer eingeben)"))
                    #auswahl_konto = [x for x in liste_bankkonten if x == kontonr]
                    for x in liste_bankkonten:
                        if (x==konto):
                            auswahl_konto = liste_bankkonten[k.kontonummer]
                    print("Folgendes Konto wurde ausgewählt")
                    auswahl_konto.daten_ausgabe()
"""

"""elif (auswahl == 6):
                    kontonr = int(input("Welches Bankkonto soll ausgewählt werden? (Bitte Kontonummer eingeben)"))
                    for x in dictionary_konten.keys():
                        if (x==kontonr):
                            auswahl_konto = dictionary_konten[x]
                            print("Folgendes Konto wurde ausgewählt")
                            auswahl_konto.daten_ausgabe()"""