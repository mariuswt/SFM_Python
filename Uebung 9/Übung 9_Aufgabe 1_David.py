# Aufgabe 1
"""
Schreiben Sie eine Klasse „Auto“ in Python. Initialisieren Sie im Konstruktor die folgenden Instanzvariablen:
Kilometerstand, Marke, Farbe, Leistung, Anzahl der Türen.
Definieren Sie die Methoden
zeige_daten(), welche die Instanzvariablen auf dem Bildschirm ausgibt und
strecke_fahren(kilometer), die den Kilometerstand um den Wert des Parameters erhöht.
Schreiben Sie auch eine main()_Methode, die 2 Autos anlegt, beide Autos fahren lässt
(Kilometerstand erhöht sich) und die jeweiligen Fahrzeug-Daten ausgibt.
"""

class Auto:
    anzahl_autos = 0
    def __init__(self, kilometerst, marke, farbe, leistung, tueren,):
        self.kilometerstand = kilometerst
        self.marke = marke
        self.farbe = farbe
        self.leistung = leistung
        self.anzahl_tueren = tueren
        Auto.anzahl_autos +=1
        self.auto_nummer = Auto.anzahl_autos

    def zeige_daten(self):
        print("Daten von Auto",self.auto_nummer,"\n=========")
        print("Marke: ",self.marke)
        print("Farbe: ", self.farbe)
        print("Anzahl PS: ", self.leistung)
        print("Anzahl Türen: ", self.anzahl_tueren)
        print("Kilometerstand: ", self.kilometerstand,"\n=========")

    def strecke_fahren(self,kilometer):
        self.kilometerstand = self.kilometerstand + kilometer
        print("Auto",self.auto_nummer," fährt ",kilometer, "Kilometer")



def main():
    #liste_auto_objekte =[]

    #def objekte_speichern(auto_objekt):
    #    liste_auto_objekte.append(auto_objekt)

    auto_1= Auto(0,"Audi","Grün",450,5)
    auto_2=Auto(10,"Mercedes","Schwarz",560,5)

    #objekte_speichern(auto_1) #         Zu Testzwecken
    #objekte_speichern(auto_2) #         Zu Testzwecken

    auto_1.zeige_daten()
    auto_2.zeige_daten()
    auto_1.strecke_fahren(500)
    auto_2.strecke_fahren(300)
    auto_1.zeige_daten()
    auto_2.zeige_daten()

    #liste_auto_objekte[0].zeige_daten()        Zu Testzwecken

main()

