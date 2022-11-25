# Aufgabe 1

"""
1. Die in Python vordefinierten Funktionen min() und max() ermitteln das kleinste bzw. größte Element einer Liste.
Programmieren Sie die Funktion minmax(liste), die die beiden entsprechenden Elemente als Tupel zurückgibt – ohne min()
und max() zu verwenden.
"""

def minmax(liste):
    liste.sort()
    print("Kleinster Wert: ", liste[0])
    print("Größter Wert: ", liste[len(liste)-1])

test_liste = [28,94,648,88,57,44]

minmax(test_liste)

"""
2. Ein Palindrom ist ein Text, der von vorn und hinten gelesen den gleichen Inhalt hat – z. B. »Lagerregal« oder 
»Trug Tim eine so helle Hose nie mit Gurt?«. Leer- und Satzzeichen werden dabei ignoriert.
Schreiben Sie eine Funktion, die testet, ob eine Zeichenkette ein Palindrom ist. Tipp: Verwenden Sie die Funktion 
str.isalpha, um zu testen, ob ein Zeichen ein Buchstabe ist.
"""

def testing_palindrom(var):
    buchstaben_anzahl = len(var) -1
    if (str.isalpha(var) == True):
        for x in range(len(var)):
            if((var.lower().replace(" ","")[x] == (var.lower().replace(" ","")[buchstaben_anzahl]))):
                y = True
                buchstaben_anzahl -= 1
            else:
                y = False
                break
        if(y == True):
            print("Es handelt sich bei der Zeichenkette um ein Palindrom")
            print(var)
            print("Mit Palindrom:")
            print(var[len(var)::-1])
        else:
            print("Es handelt sich bei der Zeichenkette um kein Palindrom")

zeichenkette = input("Gebe eine Zeichenkette ein: ")
testing_palindrom(zeichenkette)


#Das wäre der komplizierte Weg
"""s="n i o k l k iu hun mk "
s_neu= list(map(lambda x: x.replace(" ",""),s))
print(s_neu)
print("".join(s_neu))"""

"""
3. Schreiben Sie eine Funktion, welche die Qualität von Passwörtern nach einem einfachen Punktesystem bewertet. 
Es gelten dabei die folgenden Regeln:
– Passwort mit 7 oder weniger Zeichen: immer 0 Punkte
– ab 8 Zeichen: 1 Punkt
– enthält sowohl Groß- als auch Kleinbuchstaben: +1 Punkt
– enthält mehr als sechs unterschiedliche Zeichen: +1 Punkt
(Die Regel soll Passwörter wie »11111111« verhindern.)
– enthält zumindest eine Ziffer: +1 Punkt
– enthält zumindest ein Sonderzeichen: +1 Punkt
"""


def quali_passwort(passwort):
    punkte = 0
    if (len(passwort) >= 8):
        punkte +=1
    if(any(i.islower() for i in passwort) and any(j.isupper() for j in passwort)):
        punkte += 1
    if(len(set(passwort)) > 6):
        punkte += 1
    if(any(char.isdigit() for char in passwort)):
        punkte += 1
    if (any(not char.isalnum() for char in passwort)):
        punkte +=1
    if(len(passwort) <= 7):
        punkte = 0

    print("Punktesicherheit des Passworts: ", punkte)

passwort = input("Geben Sie bitte ein Passwort ein: ")
quali_passwort(passwort)


def countdown(n):
        if n == 0:
            print (0)
        else:
            print(n)
            countdown(n - 1)

n = int(input("Von wo soll runtergezählt werden? "))
countdown(n)