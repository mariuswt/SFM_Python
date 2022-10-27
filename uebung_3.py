#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""""
UEBUNG 3:

Aufgabe 1
 """"
   
# 1.Sie wollen den Oktalcode 750 in binärer Darstellung anzeigen. Wie gehen Sie vor?

x= 0o750 #0o kennzeichnet Oktalcode
print (bin(x)) #bin gibt x in binaerer Darstellung aus


# 2. Wie erzeugen Sie Zufallszahlen zwischen 1 und 49?

from random import randint #Random-Modul-Methode fuer ganze Zahlen importieren
print(randint(0, 49)) #Bereich eingeben (0-49)


# 3. Sie brauchen zwei Zufallszahlen zwischen 0,0 und 10,0. Schreiben Sie geeigneten Python-Code!

import random #Random-Modul-Methode fuer Zahlen importieren
x = uniform(0.0 , 10.0 )#Einen Bereich von zwei Floatzahlen angeben
y = uniform(0.0 , 10.0 )
print('Zufallszahl1:', x, '\nZufallszahl2:', y) #Geht bestimmt auch noch eleganter


# 4. Sie wollen Geldbeträge ohne Rundungsfehler verarbeiten. Welchen Datentyp verwenden Sie?

from decimal import Decimal #Decimal als Alternative zu float verwenden (Ohne Rundungsfehler)
a = Decimal ('3.71') #Zahlen muessen als Zeichenkette uebergeben werden
b = Decimal ('4.29')
c = a + b
print (c)


# 5. Welchem Zahlenwert ist True zugeordnet?

print (int(True)) #->1 (ueber int() bekommt man den Zahlenwert von bool true)


# 6. Wie bilden Sie eine Zeichenkette, die selbst ein Anführungszeichen enthält?

print ('Das ist die \"Zeichen\"-kette') # durch \ kann gekennzeichnet werden was Teil des str sein soll


# 7. Extrahieren Sie aus der folgenden Zeichenkette das Tag zwischen den eckigen Klammern: bla [wichtig] mehr bla

s = 'bla [wichtig] mehr bla'
print (s[5:12]) # Slicing Syntax verwenden


# 8. Geben Sie drei maximal fünfstellige Zahlen rechtsbündig aus.

import random

# zufaellige ganze Zahl zwischen 0 und 99999 erzeugen
zahl1 = randint(0, 99999)
# int in str umwandeln
zahl1 = str(zahl1)
# str nach rechts verschieben
ausgabe1 = zahl1.rjust(115) #70
print(ausgabe1)

zahl2 = randint(0, 99999)
zahl2 = str(zahl2)
ausgabe2 = zahl2.rjust(115)
print(ausgabe2)

zahl3 = randint(0, 99999)
zahl3 = str(zahl3)
ausgabe3 = zahl3.rjust(115)
print(ausgabe3)


# 9. Geben Sie Hello,World! in umgekehrter Reihenfolge aus.

s = 'Hello,World!'
print (s[:: -1])



""""
Aufgabe: 2
""""

#Benutzer auffordern Kommazahl einzugeben
kommazahl = input('Fliesskommazahl eingeben: ')
vorkommaanteil = kommazahl.split('.')
print('Vorkommaanteil: ', vorkommaanteil [0])
print('Nachkommaanteil: 0.%s' % vorkommaanteil [1] [:6])


#Input in Float Zahl umwandeln
#kommazahl2 = float(kommazahl)


















