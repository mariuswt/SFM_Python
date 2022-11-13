#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 09:36:41 2022

@author: admin
"""

'''
AUFGABE 1: Beantworten Sie folgende Fragen:
'''

# 1.) Was wird bei der Ausführung des Codes ausgegeben?

for i in range (1, 3): #Eine 1.Liste ertsellen (exkl. letztem Wert)-> 1, 2
    for j in range (i): #Eine 2. Liste erstellen (exkl. letztem Wert aus Liste 1) -> 1
        print (i+j) # Liste1 + Liste2 ausgeben lassen
                    # jz wird aber nicht 1,2,1 sondern 1,2,3 ausgegeben
                    # zählt also um Anzahl Elemente in Liste2 weiter hoch und hängt nicht nur Werte an

# 2.) Welche Zahlen werden ausgegeben?

i=0; j=9 #Startwerte für i und j festlegen
while i<9: # while schleife wird ausgeführt, solange gilt i<9
    print(i,j) # Wertepaar i und j ausgeben
    if i>3: # Sobald i>3 wird...
        break #...soll die while-Schleife verlassen werden
    i+=1 # Auf die werte für i wird in jedem Schritt 1 addiert (hochzählen)
    j-=1 # Von dem Wert für j wird in jedem Schritt 1 abgezogen (runterzählen)

# 3.) While- und For- Schleifen die in 5er-Schritten von 100 bis 0 zählen

i=100 # Startwert für i = 100
while i>-1: # while-Schleife läuft, solange i>-1 gilt (damit 0 noch drin)
    print(i) # i ausgeben lassen
    i-=5 # mit jedem Durchlauf der Schleife 5 vom Wert für i abziehen
    
for i in range (0, 101, 5): # Liste die in 5-er Schritten von 0-100 zählt
    print(100-i) # bei der Ausgabe von 100 abziehen um nicht hoch- sondern
                 # runter zu zählen
    
    
    
'''
AUFGABE 2: Klassifizierung von Schrauben
'''

durchmesser = int(input("Durchmesser [in mm]: "))
länge = int(input("Länge [in mm]: "))

if durchmesser <= 3 and länge <= 20:
    print ('Es handelt sich um eine Schraube des Typ:1')
else:
    if durchmesser >=4 and durchmesser <=6 and länge >=21 and länge <=30: # wie kann man dieses Staement anders formulieren?
        print ('Es handelt sich um eine Schraube des Typ:2')              # 4 <= durchmesser >= 20 geht nicht
    else:
        if durchmesser >=7 and durchmesser <=20 and länge >=31 and länge <=50:
            print ('Es handelt sich um eine Schraube des Typ:3')
        else:   
            print ('Unbekannter Schraubentyp!')

'''
# Das funktioniert schonmal
durchmesser = int(input("Durchmesser [in mm]: "))
länge = int(input("Länge [in mm]: "))

if durchmesser in [4,5,6] and länge in [21,22,23,24,25,26,27,28,29,30]:
    print ('Es handelt sich um eine Schraube des Typ:2')
else:   
     print ('Unbekannter Schraubentyp!')
'''


'''
AUFGABE 3: Kalender
'''

monat = int(input("Welcher Monat: "))
if monat <1 or monat >12:
    print ('Keine gültige Eingabe!')
else:    
    jahr = int(input("Welches Jahr: "))
    if jahr <0 or jahr >4000:
        print ('Keine gültige Eingabe!')

if monat in [1,3,5,7,8,10,12]:
    print('Monat hat 31 Tage.')
else:
    if monat in [4,6,9,11]:
        print('Monat hat 30 Tage.')
    else:
        if jahr % 4 == 0 and jahr % 100 != 0 or jahr % 400 == 0:
            print ('Monat hat 28 Tage.')
        else:
            print ('Monat hat 29 Tage.')
         
        
        
        


