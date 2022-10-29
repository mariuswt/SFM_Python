#Aufgabe 2

zahl = float(input("Bitte geben Sie eine Zahl mit Kommastellen ein: "))
print("Eingegebene Zahl mit Kommastellen: ", zahl)

print("Vorkommaanteil:", int (zahl))
print("Nachkommaanteil: {0:.6f}".format(zahl-int(zahl)))
