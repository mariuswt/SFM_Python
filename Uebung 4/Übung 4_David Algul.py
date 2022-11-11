# Aufgabe 1
"""
1. Erläutern Sie den Unterschied zwischen den Vergleichsoperatoren: »==« und »is« sowie
»!=« und »is not«."""
"""
Mit == bzw. != testet man ob der Wert des Objektes, auf das die Referenzvariable zeigt, den Wert enthält, der auf der rechten Seite des "==–Operators"
steht bzw. ob der Wert auf der rechten Seite des "==–Operators" nicht enthält, während man mit "is" und "is not" testet, ob zwei Referenzvariabeln
auf dasselbe bzw. verschiedene Objekte zeigen.

Zum Beispiel:
a == 3 bzw. a != 3

a is b bzw. a is not b

"""
import copy
a = {5}
b = copy.copy(a)
print (id(a))
print(id(b))
"""
2. Sie wollen den Rest der Division 225 / 17 ermitteln. Wie lautet die Berechnung in python?
"""
print(225%17)

"""
3. Erläutern Sie die Short-Circuit-Evaluation. Nennen Sie ein Beispiel!
Die Short-Circuit-Evaluation kann nur bei den logischen Operatoren and und or angewendet werden. Hierbei wird die Auswertung abgebrochen 
sobald das Ergebnis bereits feststeht. Bei and endet die Auswertung beim ersten false-Teilergebnis. Das Gesamtergebnis ist dann zwingend
false.
Bei or endet die Auswertung beim ersten true-Teilergebnis. In diesem Fall ist das Gesamtergebnis zwingend true.
Beispiel:
"""

print("Geben Sie bitte nachfolgend Zahlen ein, bei der das Divisionsergebnis größer ist als 3")
a = float(input("Geben Sie die erste Zahl ein: "))
b = float(input("Geben Sie die zweite Zahl ein: "))
print("Die Divisionsrechnung lautet: ")
if (b!=0 and a/b>3):        # Sobald die erste Bedingung b!=0 nicht erfüllt wird, wird der zweite Ausdruck bereits nicht mehr ausgewertet
     print(a/b)             # Das spart Rechenzeit!
else:
    print("Bitte halten Sie sich an die obengenannte Regel")


"""
4. Welchen Datentyp und Wert haben a und b? a = 1 + 2 * 3 ** 4
b = 100 < a < 200
"""
a = 1 + 2 * 3 ** 4
print(type(a)) # integer

b = 100 < a < 200
print(type(b)) # Boolean mit dem Wert True, weil a tatsächlich zwischen 100 und 200 liegt


# Aufgabe 2

k0 = float(input("Anfangskaptial K0 [€]: "))
p = float(input("Zinssatz p in Prozent [%]: "))
n = float(input("Anzahl der Jahre, die verzinst werden sollen: "))

kn = k0 * (1+p/100)**n

print("Das Endkapital nach ",n, "Jahren: {0:.2f} €".format(kn))
