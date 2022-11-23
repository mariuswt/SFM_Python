# SFM2 Python Programmierung
# Übung 7

# Aufgabe 1
# 1. Die in Python vordefinierten Funktionen min() und max() ermitteln das
# kleinste bzw. größte Element einer Liste. Programmieren Sie die Funktion
# minmax(liste), die die beiden entsprechenden Elemente als Tupel
# zurückgibt – ohne min() und max() zu verwenden.


# 2. Ein Palindrom ist ein Text, der von vorn und hinten gelesen den gleichen
# Inhalt hat – z. B. »Lagerregal« oder »Trug Tim eine so helle Hose nie mit
# Gurt?«. Leer- und Satzzeichen werden dabei ignoriert.
# Schreiben Sie eine Funktion, die testet, ob eine Zeichenkette ein Palindrom
# ist. Tipp: Verwenden Sie die Funktion str.isalpha, um zu testen, ob ein
# Zeichen ein Buchstabe ist.


# 3. Schreiben Sie eine Funktion, welche die Qualität von Passwörtern nach
# einem einfachen Punktesystem bewertet. Es gelten dabei die folgenden
# Regeln:
# – Passwort mit 7 oder weniger Zeichen: immer 0 Punkte
# – ab 8 Zeichen: 1 Punkt
# – enthält sowohl Groß- als auch Kleinbuchstaben: +1 Punkt
# – enthält mehr als sechs unterschiedliche Zeichen: +1 Punkt
# (Die Regel soll Passwörter wie »11111111« verhindern.)
# – enthält zumindest eine Ziffer: +1 Punkt
# – enthält zumindest ein Sonderzeichen: +1 Punkt
# Beispiele:
# – 'abc': 0 Punkte
# – 'abcdefghij': 2 Punkte
# – 'ab1122$$!!': 3 Punkte
# – 'aBcd1234$!': 5 Punkte


# 4. Schreiben Sie eine rekursive Python-Funktion, die als Count-Down die
# Zahlen n bis 0 auf dem Bildschirm ausgibt.


# Aufgabe 2
# Schreiben Sie ein Python-Script, das ein Bankkonto verwaltet und
# verschiedene selbstdefinierte Funktionen verwendet.
# Dabei soll ein Konto die folgenden Eigenschaften (Variable) besitzen:
# Kontoinhaber, Bankleitzahl, Kontonummer, Kontostand und Zinssatz.
# Prof. Dr. Christian Cseh, Fakultät Wirtschaftsingenieurwesen
# SFM2, http://moodle.hs-esslingen.de/moodle/ Seite 2
# Der Benutzer soll über ein einfaches Konsolenmenü die möglichen
# Operationen auswählen können:
# 1. Konto neu anlegen
# 2. Einzahlen
# 3. Abheben
# 4. Zinsen gutschreiben
# 5. Kontendaten ausgeben
# Dabei soll immer nur ein Konto gleichzeitig aktiv sein. D.h. wenn der
# Benutzer die Option 1 „Konto neu anlegen“ wählt, werden die Eigenschaften
# neu abgefragt, die alten Werte überschrieben und der Kontostand auf 0.-
# gesetzt. Achten Sie darauf, dass der Kontostand nicht negativ werden darf.


# Zusatzaufgabe
# Verändern Sie Ihr Programm zum Zahlenraten aus der Übung 5 so, dass
# einzelne Aufgaben des Programms in getrennten Funktionen implementiert
# sind. Versuchen Sie innerhalb der Funktionen keine globale Variable zu
# verändern.