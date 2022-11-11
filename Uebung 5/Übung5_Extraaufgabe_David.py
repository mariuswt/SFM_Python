# Zusatzaufgabe

from random import randint
def menue():
    print("(N)eues Spiel starten")
    print("(L)evel festlegen")
    print("(B)eenden")
    eingabe = input("Wählen Sie bitte eine der drei Optionen: ")
    return eingabe

def neues_spiel (level_eingabe):
    level_lokal = 10*level_eingabe
    print("Raten Sie die richtige ganzzählige Zahl zwischen 1 und",level_lokal,"\nUm Aufzugeben drücken Sie bitte die 0")
    tipp = 0
    zufallszahl = randint(1,level_lokal)
    anzahl_versuche = 0

    while (tipp != zufallszahl):
        while (True):
            try:
                tipp = int(input("Tipp:"))
                break
            except ValueError:
                print("Ungültige Eingabe")
                continue

        if (tipp == 0):
            print("Sie haben aufgegeben!")
            break

        if (tipp < zufallszahl):
            print("Zahl ist größer als ",tipp)
            anzahl_versuche +=1
        elif(tipp > zufallszahl):
            print("Zahl ist kleiner als ",tipp)
            anzahl_versuche +=1
        else:
            anzahl_versuche +=1
            print("Glückwunsch Sie haben die richtige Zahl erraten!")
            print("Anzahl der Versuche: ",anzahl_versuche)

def level ():
    level = int(input("Legen Sie ein Level größer 0 fest: "))
    while (level <= 0 ):
        level = int(input("Das Level muss größer 0 sein: "))
    return level

def beenden ():
    print("Das Spiel wird beendet")


def main ():
    spiellevel = 1
    while (True):
        auswahl = menue()
        if (auswahl == "N" or auswahl == "n"):
            neues_spiel(spiellevel)
        elif(auswahl == "L" or auswahl == "l"):
            spiellevel = level()
        elif (auswahl == "B" or auswahl == "b"):
            beenden()
            break
        else:
            print("Ungültige Eingabe!")

main()








