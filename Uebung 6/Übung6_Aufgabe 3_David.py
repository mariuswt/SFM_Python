# Aufgabe 3

"""
Schreiben Sie ein Python-Script, das eine Einkaufsliste verwaltet. Darin sollen die Produkte und die Anzahl als Wert
eingetragen werden: {'Tomaten': 1, 'Gurken': 5, ...}. Zu Beginn ist die Einkaufsliste leer. Der Benutzer soll nun über
die Eingabe von „+Produkt“ ein Produkt hinzufügen, bzw. die Anzahl um 1 erhöhen, und mit „-Produkt“ die Anzahl um 1
verkleinern, bzw. das Produkt löschen können. Nach jeder Eingabe soll die Einkaufsliste auf dem Bildschirm ausgegeben
werden.
"""
einkaufliste = {}
def menue():
    print("Neues Produkt einfügen: +\"Produktnamen\"")
    print("Produkt aus der Einkaufsliste herausnehmen: \"-Produktnamen\"")
    print("Um das Programm zu beenden \"B\" drücken")
    eingabe = input("Aktion:")
    return eingabe

while (True):
    produkt = menue()
    if (produkt == "B" or produkt == "b"):
        break
    if (produkt[1:] in einkaufliste.keys()):
        if (produkt[0] == "+"):
            einkaufliste[produkt[1:]] += 1
        elif (produkt[0] == "-"):
            einkaufliste[produkt[1:]] -= 1
            if (einkaufliste[produkt[1:]] == 0):
                del einkaufliste[produkt[1:]]
    else:
        if (produkt[0] == "-" and list(einkaufliste.keys())[0:] != produkt[1:]):
            print("Produkt ist nicht in der Einkaufliste enthalten")
        else:
            einkaufliste[produkt[1:]] = 1
    print(einkaufliste)






"""if (produkt[0] == "+"):
        einkaufliste[produkt[1:]] += 1
        break
    elif(produkt[0] == "-"):
        einkaufliste[produkt[1:]] -= 1
        if (einkaufliste[produkt[1:]] == 0):
            del einkaufliste[produkt[1:]]
        break
        
        else:
            if (produkt[0] == "-" and list(einkaufliste.keys())[0:] != produkt[1:]):
                print("Produkt ist nicht in der Einkaufliste enthalten")
            else:
                einkaufliste[produkt[1:]] = 1
    print(einkaufliste)"""


