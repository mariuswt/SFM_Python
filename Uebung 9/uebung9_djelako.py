class Auto:
    auto=3
    def __init__(self,Kilometerstand,Marke,Farbe,Lesitung,AnzahlTüren):
        self.kilometerstand=Kilometerstand
        self.Marke=Marke
        self.Farbe=Farbe
        self.Lesitung=Lesitung
        self.AnzahlTüren=AnzahlTüren
    
    def zeigeDaten(self):
        print(self.AnzahlTüren,self.Farbe,self.kilometerstand,self.Lesitung,self.Marke)

    def strecckeFahren(self,kilometer):
        self.kilometerstand=self.kilometerstand + kilometer


def main():
    auto1=Auto(20,'BMW','Blaue',245,4)
    auto2=Auto(100,'Ford','gray',200,4)
    print(auto1.Marke,'fährt')
    auto1.strecckeFahren(50)
    print(auto1.Marke,'ist', auto1.kilometerstand, 'KM gefahren')
    print(auto1.Marke, 'daten sind:')
    auto1.zeigeDaten()

    print(auto2.Marke,'fährt')
    auto1.strecckeFahren(250)
    auto2.strecckeFahren(250)
    print(auto2.Marke, 'ist', auto2.kilometerstand, 'KM gefahren')
    print(auto2.Marke, 'daten sind:')
    auto2.zeigeDaten()

if __name__ == "__main__":
    main()
        