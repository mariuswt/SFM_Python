# Aufgabe 1
"""
Verändern Sie die Klasse „Auto“ aus der letzten Übung 9, Aufgabe 1:
- Schützen Sie die Instanzvariable „Kilometerstand“ als private Variable durch eine entsprechende property.
Ergänzen Sie die vorhandenen Instanzvariablen um:
- eine Klassenvariable „automatik“, die im Konstruktor über einen weiteren Parameter von Typ bool belegt wird.
Zählen Sie die neu erzeugten Auto- Objekte mit und ohne Automatik. Schreiben Sie eine statische Methode, welche
die Anzahl der Autos mit und ohne Automatik ausgibt.
- eine Referenz auf ein Autoradio. Das Programm soll also zusätzlich zu der Klasse „Auto“ noch über eine Klasse
 „Autoradio“ verfügen. Der __init__()- Methode der Klasse „Autoradio“ soll der Markenname des Radios sowie ein
 bool-Argument übergeben werden. Dieses bestimmt, ob das Autoradio noch über einen CD-Player verfügt (True) oder nicht
 (False). Zudem soll eine Methode namens zeige_daten() eingebaut werden, die Informationen zu dem Markennamen und der
 Ausstattung (CD-Player) ausgibt.
In der main()-Methode sollen zunächst drei Instanzen der Klasse Autoradio erzeugt werden, die sich in Markenname und
Ausstattung (CD-Player) unterscheiden. Erzeugen Sie im Anschluss noch drei Instanzen der Klasse Auto und weisen Sie
ihnen unterschiedliche Attribute und Autoradios zu. Lassen Sie sich zum Schluss noch die Daten aller Autos mittels der
Methode zeige_daten() ausgeben.
"""
class Auto_Radio:
    auto_radio_mit_cd_player = 0
    auto_radio_ohne_cd_player = 0
    def __init__(self, marke, bool):
        self.markenname = marke
        self.cd_player = bool
        if (self.cd_player == True):
            Auto_Radio.auto_radio_mit_cd_player +=1
        else:
            Auto_Radio.auto_radio_ohne_cd_player +=1

    def zeige_daten(self):
        print("Marke des Autoradios: ", self.markenname)
        if (self.cd_player == True):
            print("Mit CD-Player")
        else:
            print("Ohne CD-Player")

class Auto:
    anzahl_autos = 0
    anzahl_automatik = 0
    anzahl_schaltgetriebe = 0
    def __init__(self, kilometerst, marke, farbe, leistung, tueren, automatik, auto_radio):
        self.__kilometerstand = kilometerst
        self.marke = marke
        self.farbe = farbe
        self.leistung = leistung
        self.anzahl_tueren = tueren
        Auto.anzahl_autos +=1
        self.auto_nummer = Auto.anzahl_autos
        self.automatik = automatik
        if (self.automatik == True):
            Auto.anzahl_automatik +=1
        else:
            Auto.anzahl_schaltgetriebe +=1
        self.auto_radio = auto_radio

    @staticmethod
    def anzahl_automatik_schaltgetriebe():
        print("Gesamtanzahl der Autos mit Automatik: ",Auto.anzahl_automatik)
        print("Gesamtanzahl der Autos mit Schaltgetriebe: ",Auto.anzahl_schaltgetriebe)

    def get_kilometerstand(self):
        return self.__kilometerstand

    def set_kilometerstand(self,kmstand):
        if (kmstand < self.__kilometerstand):
            print("Der neue Kilometerstand kann nicht kleiner als der alte Kilometerstand sein")
        else:
            self.__kilometerstand=kmstand

    kilometerstand = property(get_kilometerstand,set_kilometerstand)

    def zeige_daten(self):
        print("Daten von Auto",self.auto_nummer,"\n=========")
        print("Marke: ",self.marke)
        print("Farbe: ", self.farbe)
        if (self.automatik == True):
            print("Getriebe: Automatik")
        else:
            print("Getriebe: Schaltgetriebe")
        print("Anzahl PS: ", self.leistung)
        print("Anzahl Türen: ", self.anzahl_tueren)
        self.auto_radio.zeige_daten()
        print("Kilometerstand: ", self.kilometerstand,"\n=========")

    def strecke_fahren(self,kilometer):
        self.kilometerstand = self.kilometerstand + kilometer
        print("Auto",self.auto_nummer," fährt ",kilometer, "Kilometer")


def main():
    auto_radio_1 = Auto_Radio("Bluepoint",True)
    auto_radio_2 = Auto_Radio("Samsung",False)
    auto_radio_3 = Auto_Radio("Sony", True)

    auto_1 = Auto(100,"Mercedes E350 AMG","Matt-Schwarz",450,5,True,auto_radio_1)
    auto_2 = Auto(200,"Audi RS7","Grün",700,5,True,auto_radio_2)
    auto_3 = Auto(300,"Volkswagen Golf 7","Blau",180,5,False,auto_radio_3)

    auto_1.zeige_daten()
    auto_2.zeige_daten()
    auto_3.zeige_daten()

    print("Anzahl der produzierten Autos: ",Auto.anzahl_autos)
    print("Anzahl Autos mit Automatikgetriebe: ",Auto.anzahl_automatik)
    print("Anzahl Autos mit Schaltgetriebe: ",Auto.anzahl_schaltgetriebe)
    print("Anzahl Autradios mit CD-Player: ",Auto_Radio.auto_radio_mit_cd_player)
    print("Anzahl Autradios ohne CD-Player: ", Auto_Radio.auto_radio_ohne_cd_player)


main()