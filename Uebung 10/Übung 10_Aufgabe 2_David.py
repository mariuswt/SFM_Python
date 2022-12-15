# Aufgabe 2
"""Implementieren Sie eine Klasse Schrank mit den Instanzvariablen name für den Modellnamen, einem Tupel abmessung
für die Breite, Tiefe und Höhe und preis für den Preis. Erstellen Sie 2 statische Methoden für zwei Einheitsschränke
sowie für einen Konstruktor für einen allgemeinen Schranktyp. Schreiben Sie neben den notwendigen
Getter- und Setter- Methoden noch die folgenden Methoden:
• getVolumen()
Berechnen des Volumens eines Schrankes.
• getPreis()
Berechnen des Preises eines Schrankes über die Formel preis = cbm*100.-€ aus dem Volumen.
• getInfo()
Rückgabe der vollständigen Schrankeigenschaften als Zeichenkette.
• getAnzahl()
Rückgabe der Anzahl der definierten Schränke mit Hilfe der Klassenvariablen zaehler.
Testen Sie anschließend diese Klasse mit mehreren definierten Schrankobjekten.
"""

class Schrank:
    zaehler = 0
    def __init__(self,name,breite,tiefe,hoehe,preis):
        self.modellname = name
        self._abmessung = (breite,tiefe,hoehe)
        self._preis = preis
        Schrank.zaehler +=1
        self.nummer = Schrank.zaehler

    def get_abmessung(self):
        return self._abmessung

    def set_abmessung(self):
        if(self._abmessung <(0,0,0)):
            print("Bitte setzen Sie Werte, die jeweils über 0 liegen!")
        else:
            return self._abmessung

    def get_preis(self):
        return self._preis*self.getVolumen()

    def set_preis(self):
        if(self._preis <0):
            print("Bitte setzen Sie einen Preis, der über 0 liegt!")
        else:
            return self._preis

    abmessung=property(get_abmessung,set_abmessung)
    preis=property(get_preis,set_preis)

    @staticmethod
    def einheitsschrank_1():
        return Schrank("IKEA-Schrank 1",1.5,1,3,400)

    @staticmethod
    def einheitsschrank_2():
        return Schrank("IKEA-Schrank 2", 2, 1.5, 4, 600)

    def getVolumen(self):
        return self.abmessung[0]*self.abmessung[1]*self.abmessung[2]

    def getInfo(self):
        print("Datenausgabe des Schranks ",self.nummer)
        print("=========================")
        print("Modell: ",self.modellname)
        print("Abmessungen: ",self.abmessung[2],"m X",self.abmessung[0],"m X",self.abmessung[1],"m")
        print("Preis: ",self.preis,"€\n")

    @staticmethod
    def getAnzahl():
        print("Anzahl bereits hergestellter Schränke: ",Schrank.zaehler," Stück")

def main():
    schrank_1 = Schrank("Testschrank_1",2,3,4,700)
    schrank_2 = Schrank("Testschrank_2",1,4,5,800)
    schrank_3 = Schrank.einheitsschrank_1()
    schrank_4 = Schrank.einheitsschrank_2()

    schrank_1.getInfo()
    schrank_2.getInfo()
    schrank_3.getInfo()
    schrank_4.getInfo()
    Schrank.getAnzahl()

main()
