# Aufgabe 3 zu Übung 5

monat = {1:31,2:28,3:31,4:30,5:31,6:31,7:31,8:31,9:30,10:31,11:30,12:31}

while(True):
    try:
        abfrage_monat = int(input("Monatszahl: "))
        abfrage_jahr = int(input("Jahr: "))
        break
    except ValueError:
        print("Ungültige Eingabe!")
        continue

for x in monat:
    if ((abfrage_jahr%4 == 0 and abfrage_jahr%100 >0) or abfrage_jahr%400 == 0):
        monat[2] = 29         # Bei Dictionaries sind die Schlüssel nicht änderbar, aber die Werte schon
    if (abfrage_monat == x):
        print("Monat:",x,", mit",monat.__getitem__(x),"Tagen")




