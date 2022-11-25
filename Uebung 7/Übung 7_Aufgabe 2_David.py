# Aufgabe 2
"""

Schreiben Sie ein Python-Script, das ein Bankkonto verwaltet und verschiedene selbstdefinierte Funktionen verwendet.
Dabei soll ein Konto die folgenden Eigenschaften (Variable) besitzen: Kontoinhaber, Bankleitzahl, Kontonummer,
Kontostand und Zinssatz.
Der Benutzer soll über ein einfaches Konsolenmenü die möglichen Operationen auswählen können:
1. Konto neu anlegen
2. Einzahlen
3. Abheben
4. Zinsen gutschreiben
5. Kontendaten ausgeben
Dabei soll immer nur ein Konto gleichzeitig aktiv sein. D.h. wenn der Benutzer die Option 1 „Konto neu anlegen“ wählt,
werden die Eigenschaften neu abgefragt, die alten Werte überschrieben und der Kontostand auf 0.- gesetzt.
Achten Sie darauf, dass der Kontostand nicht negativ werden darf.

"""


def konto_anlegen():
    kontoinhaber = input("Kontoinhaber: ")
    kontonummer = int(input("Kontonummer: "))
    saldo = float(input("Kontoguthaben: "))
    zinssatz = (float(input("Zinssatz: ")))
    liste_konto = [kontoinhaber,kontonummer,saldo,zinssatz]
    return liste_konto



def einzahlen (saldo,betrag):
    return saldo + abs(betrag)

def abheben(saldo,betrag):
    if (saldo - abs(betrag) < 0):
        print(("Nicht genügend Saldo auf dem Konto!"))
    else:
         return saldo - abs(betrag)

def zinsen_gutschrift(saldo, zinsstz):
    zinsen = saldo * (zinsstz/100)
    print("Zinsgutschrift: ", zinsen)
    return saldo + zinsen

def daten_ausgabe(kontoinhaber,kontonummer, saldo, zinssatz):
    print("Kontodaten\n=========")
    print("Kontoinhaber: ",kontoinhaber)
    print("Kontonummer: ",kontonummer)
    print("Kontoguthaben: ", saldo)
    print("Zinssatz: ", zinssatz)

def menue_ausgabe():
    print("=========")
    print("(1) Konto neu anlegen")
    print("(2) Einzahlen")
    print("(3) Abheben")
    print("(4) Zinsgutschrift")
    print("(5) Datenausgabe")
    print("(6) Beenden")
    auswahl = int (input("=========\nWählen Sie bitte eine Option aus: "))
    return auswahl

def main():
    while(True):
        try:
            auswahl = menue_ausgabe()
            if (auswahl == 1):
                liste_konto = list(konto_anlegen())
            elif(auswahl == 2):
                betrag = float(input("Betrag: "))
                liste_konto[2]=einzahlen(liste_konto[2] ,betrag)
            elif (auswahl == 3):
                betrag = float(input("Betrag: "))
                liste_konto[2] = abheben(liste_konto[2], betrag)
            elif (auswahl == 4):
                liste_konto[2] = zinsen_gutschrift(liste_konto[2],liste_konto[3])
            elif(auswahl == 5):
                daten_ausgabe(liste_konto[0], liste_konto[1], liste_konto[2], liste_konto[3])
            elif (auswahl == 6):
                break
        except ValueError:
                print("Wählen Sie bitte eine Zahl von 1 bis 5!")


main()

