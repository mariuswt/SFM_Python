#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 07:41:43 2022

@author: admin
"""
#%% Aufgabe 1:
    
class Auto():

    def __init__(self , kilometerstand , marke, farbe, leistung, anzahl_türen):
          
        self.kilometerstand:int = kilometerstand
        self.marke:str = marke
        self.farbe:str = farbe
        self.leistung:int = leistung
        self.anzahl_türen:int = anzahl_türen


    def zeige_daten (self):
        print("KM-Stand:", self.kilometerstand, "km")
        print("Marke: ", self.marke)
        print("Farbe: ", self.farbe)
        print("Leistung: ", self.leistung, "PS")
        print("Anzahl Türen: ", self.anzahl_türen)
        
    def strecke_fahren (self, kilometer):
        self.kilometer:int = kilometer
        self.kilometerstand += kilometer
        
        
def main():
    a2 = Auto(50000, "Audi", "Nardograu", 630, 5)
    a3 = Auto(40000, "BMW", "Frozen_Blue", 530, 3)
    
    a2.strecke_fahren(250)
    a3.strecke_fahren(300)
    
    a2.zeige_daten()
    
    a3.zeige_daten()


        
a1 = Auto(10000, "Porsche", "Enzianblau", 650, 3)

print (a1.marke) # lesender Zugriff 

a1.zeige_daten()
a1.strecke_fahren(50) 
print (a1.kilometerstand)

main()

#%% Aufgabe 2:

# nicht fertig!

from decimal import Decimal
class Bank():
    
    def posZahlEingeben(text):
        eingabe = -1
        while (eingabe < 0):
            eingabe = Decimal(input(text))
        return eingabe
    
    def kontoAnlegen():
        global inhaber 
        inhaber = input("Inhaber: ")
        global blz
        blz = int(posZahlEingeben("BLZ: "))
        global kontoNummer
        kontoNummer = int(posZahlEingeben("Kontonummer: "))
        global zinssatz 
        zinssatz = Decimal(posZahlEingeben("Zinssatz: "))
        global saldo
        saldo = Decimal("0.0")
        
        while(True):
            auswahl = menüAusgebenUndEingabe()
            if ( auswahl == 1):
                kontoAnlegen()
            elif (auswahl == 2):
                saldo = einzahlen(saldo, posZahlEingeben("Einzahlungsbetrag: "))
            elif (auswahl == 3):
                saldo = abheben (saldo,  posZahlEingeben("Auszahlungsbetrag: "))
            elif (auswahl == 4):
                zinsen_vergueten(saldo,zinssatz)
            elif(auswahl == 5):
                konto_ausgeben()
            elif (auswahl == 6):
                break
            else:
                print("Falsche Eingabe!") 

class Konto():
          
    # Einen Betrag vom Konto abbuchen
    def abheben(kontostand, betrag):
        print("Es wurden {0} € abgebucht.".format(betrag))
        return Decimal(kontostand) - Decimal(betrag)

    def einzahlen(kontostand, betrag):
        print("Es wurden {0} € eingezahlt.".format(betrag))
        return Decimal(kontostand) + Decimal(betrag)

    # Zinsen für das Konto vergüten
    def zinsen_vergueten(kontostand, prozent=0.0):
        zinsen = Decimal((kontostand * prozent)) / Decimal(100)
        print("Zinsen: {0:.2f} €".format(zinsen))
        return Decimal(kontostand) + Decimal(zinsen)

    # Kontostand formatiert ausgeben
    def konto_ausgeben():
        print("\nBesitzer: ", inhaber)
        print("Bankleitzahl: ", blz)
        print("Kontonummer: ", kontoNummer)
        print("Zinssatz: {0:.2f} %".format(zinssatz))
        print("Aktueller Kontostand: {0:.2f} €\n".format(saldo))
        
class Menu():
    
    def menüAusgebenUndEingabe():
        print("\n1.	Konto neu anlegen")
        print("2.	Einzahlen")
        print("3.	Abheben")
        print("4.	Zinsen gutschreiben")
        print("5.	Kontodaten ausgeben")
        print("6.	Ende")
        return int(input("Treffen Sie eine Auswahl: "))
        
    while(True):
        auswahl = menüAusgebenUndEingabe()
        if ( auswahl == 1):
            kontoAnlegen()
        elif (auswahl == 2):
            saldo = einzahlen(saldo, posZahlEingeben("Einzahlungsbetrag: "))
        elif (auswahl == 3):
            saldo = abheben (saldo,  posZahlEingeben("Auszahlungsbetrag: "))
        elif (auswahl == 4):
            zinsen_vergueten(saldo,zinssatz)
        elif(auswahl == 5):
            konto_ausgeben()
        elif (auswahl == 6):
            break
        else:
            print("Falsche Eingabe!") 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        