# Übung 6

# Aufgabe 1
# 1. Definieren Sie in Python eine Liste mit den Vielfachen von 7, die kleiner als
# 100 sind (also [7, 14,..., 98]).
liste = []
for n in range(7, 100, 7):
    liste.append(n)
print(liste)

# 2. Welchen Datentyp verwenden Sie, um Lottozahlen zu speichern?
# A: Die Ganzzahligen Werte (INT) sollten in einem Tuple gespeichert werden, der Inhalt ist nicht veränderbar
lottozahlen = (1, 33, 98, 22, 44, 99, 99)
print((frozenset(lottozahlen)))

# 3. Schreiben Sie ein Python-Script, das die folgende Matrix umsetzt:
#
# 2 4 6
# 5 3 1
#
# und danach die Anzahl der Zeilen und die Anzahl der Spalten ausgibt.

A = [[2, 4, 6],
     [5, 3, 1]]
counter_zeilen = 0
counter_spalten = 0
run_once = 0
for zeile in A:
    counter_zeilen += 1

    if run_once == 0:
        for spalte in zeile:
            counter_spalten += 1
            run_once = 1
print(f"Zeilen: {counter_zeilen}, Spalten: {counter_spalten}")

# 4. Erläutern Sie den Unterschied zwischen den folgenden Python-Befehlen für
# zwei Sets x und y:
x = {1, 2, 3, 4, 5, 6, 7, 8, 9}
y = {"hallo", 1, 2, 22}
print(x - y)  # Aus x werden die Elemente entfernt die auch in y vorhanden sind
print(y - x)  # vice versa
print(x | y)

# 5. Welches sind die gemeinsamen Buchstaben der Wörter „Python“ und
# „Programmierung“?
for character in "Python":
    for same_character in "Programmierung":
        if character == same_character:
            print(character)

x = set("Python")
y = set("Programmierung")
print(x & y)

# 6. Entfernen Sie die Doppelgänger aus der folgenden Liste von Zahlen:
# [1, 2, 3, 2, 7, 3, 9]. Die Ergebnisliste soll aufsteigend sortiert sein.
liste = [1, 22, 2, 3, 2, 7, 3, 9]
liste = list(dict.fromkeys(liste))
liste.sort()
print(liste)


# Aufgabe 2
# a) Schreiben Sie ein Python-Script, das ein Dictionary erstellt mit den
# Zahlen 1-100 als Schlüssel und einem Boolean-Wert, der angibt, ob die
# Zahl eine Primzahl ist.

def is_prime(n):
    for i in range(2, int(n / 2)):
        if (n % i) == 0:
            return False
    return True


thisdict = {}
for number in range(1, 101):
    thisdict.update({number: is_prime(number)})
print(thisdict)

# b) Als nächstes sollen die Zahlen 1-100 in zwei Listen sortiert werden:
# Primzahlen sollen in eine Liste, Nicht-Primzahlen in eine andere Liste
# einsortiert werden. Quelle der zu sortierenden Zahlen ist das Dictionary
# aus a). Da geplant ist, später jederzeit neue Zahlen in das Dictionary
# einzutragen, sollen die bereits sortierten Zahlen aus dem Dictionary
# schrittweise entfernt werden.
prime_dict = {}
no_prime_dict = {}
for number in range(1, 101):
    if thisdict[number]:
        prime_dict.update({number: "Prime"})
    else:
        no_prime_dict.update({number: "NO Prime"})
    thisdict.pop(number)

print(prime_dict)
print(thisdict)
print(list(prime_dict.keys())[1:3])
# Aufgabe 3
# Schreiben Sie ein Python-Script, das eine Einkaufsliste verwaltet. Darin
# sollen die Produkte und die Anzahl als Wert eingetragen werden:
# {'Tomaten': 1, 'Gurken': 5, …}.
# Zu Beginn ist die Einkaufsliste leer. Der Benutzer soll nun über die Eingabe
# von „+Produkt“ ein Produkt hinzufügen, bzw. die Anzahl um 1 erhöhen, und
# mit „-Produkt“ die Anzahl um 1 verkleinern, bzw. das Produkt löschen
# können. Nach jeder Eingabe soll die Einkaufsliste auf dem Bildschirm
# ausgegeben werden.
eingabe = ""
einkaufsliste = {}
while eingabe != "stop":
    eingabe = str(input("Produkt hinzufügen(+) / entfernen(-) : "))
    if eingabe[0] == "+":
        try: # if eingabe[1:] in einkaufsliste:
            if einkaufsliste[eingabe[1:]] > 0: #
                einkaufsliste[eingabe[1:]] += 1
        except: # else:
            einkaufsliste.update({eingabe[1:]: 1})
    if eingabe[0] == "-":
        try:
            if einkaufsliste[eingabe[1:]] >= 1:
                einkaufsliste[eingabe[1:]] -= 1
                if einkaufsliste[eingabe[1:]] == 0:
                    einkaufsliste.pop(eingabe[1:])
        except:
            print("--- Artikel nicht in in der Liste! ---")
    print(einkaufsliste, "\n")
