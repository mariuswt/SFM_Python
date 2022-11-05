#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:13:59 2022

@author: admin
"""

'''
AUFGABE 1: Fragen beantworten
'''

'''
1.) Unterschiede der Vergleichsoperatoren
'''

# "==" ist ein Vergleich 'equal to' // Gibt True zurück wenn beide gleich sind
x = 4+5
y = 5+4
if x == y:
    print('ist gleich')
        
# "is" ist ein 'identity operator' und gibt nur true aus wenn die Objekte identisch gespeichert sind (gleich ≠ identisch)
x = 4
y = 4
if x is y:
    print (id(x))
    print (id(y))
    print('ist identisch')
else:
    print('ist nicht identisch')
    
x = 'Test'
y = 'Test'
if x is y:
    print (id(x))
    print (id(y))
    print('ist identisch')
else:
    print('ist nicht identisch')
    
x = [1,2,3]
y = [1,2,3]
if x is y:
    print (id(x))
    print (id(y))
    print('ist identisch')
else:
    print('ist nicht identisch:')
    print (id(x))
    print (id(y))
# => Bei Integern und Strings werden gleiche Werte identisch gespeichert, nur bei Listen wird ein neuer Speicherort gewählt und damit sind sie nicht identisch

# "!=" ist ebenfalls ein Vergleich 'not equal to' // Gibt True zurück wenn beide  nicht gleich sind
x = 4+5
y = 4+4
if x != y:
    print('ist ungleich')

# "is not" ist ein 'identity operator' und gibt nur true aus wenn die Objekte nicht identisch gespeichert sind (gleich ≠ identisch)
x = [1,2,3]
y = [1,2,3]
if x is not y:
    print (id(x))
    print (id(y))
    print('ist nicht identisch')
else:
    print('ist identisch:')
    print (id(x))
    print (id(y))

'''
2.) Rest einer Division ermitteln
'''

x = 225 / 17
print(x)
x = 225 // 17
print(x)
y = 225-(x*17)
print('Rest ist:',y)

x = 225 % 17 #modulo operator verwenden
print('Rest ist:',x)

'''
3.) Short-Circuit-Evaluation erläutern und Beispiel geben
'''
# Um Rechenleistung zu sparen werden spätere Bedingungen nicht mehr auf true oder false überprüft, wenn eine vorausgegangene Bedingung bereits nicht erfüllt wurde
x = 4
y = 5
z1 = x < y

if z1 or 1/0: # wenn der zweite Teil der if bed. ausgeführt würde, würde Programm in div by zero Fehler laufen
    print ('True') #läuft garnicht erst in den Fehler ein, weil es nach dem ersten True Statement die funktion verlässt

x = 4
y = 5                   
z1 = x > y   
if z1 and 1/0:
    print ('True') 
else:
    print ('False') #läuft garnicht erst in den Fehler ein, weil es nach dem ersten False Statement die funktion verlässt
    

'''
4.) Welchen Datentyp und Wert haben a und b?
'''

a = 1 + 2 * 3 ** 4
b = 100 < a < 200

print(type(a),a) # Datentyp: Integer, Wert: 163
print(type(b),b) # Datentyp: Boolien, Wert: True


'''
AUFGABE 2: Zins-Programm schreiben
'''
K0 = 1000.00
n = 5
p = 2.0

Kn = K0 * (1 + p/100)**n
print (round (Kn, 2))

K0 = 1000.00
n = 5
p = -2.0

Kn = K0 * (1 + p/100)**n
print (round (Kn, 2))


from random import randint, uniform
K0 = randint(500, 10001)
n = randint(0, 6)
p = uniform(0, 5)

Kn = K0 * (1 + p/100)**n

print ('Ergebnis ist =' , round (Kn, 2))

print ('\nMit den Faktoren:' '\n\nK0 =', K0, '\nn =', n, '\np =', p)














