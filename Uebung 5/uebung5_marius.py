# Übung 5
### ALT + SHIFT + E


# Aufgabe 1
# Beantworten Sie die folgenden Fragen:
# 1. Was wird bei der Ausführung des folgenden Codes ausgegeben?
for i in range(1, 3):
    for j in range(i):
        print(i + j)
# range startet ohne spezifizierung bei 0 und zählt in 1er Schritten hoch. Die Zweite Angabe wird NICHT erreicht
# i ist damit im ersten Durchlauf 1, j ist 0 -> i+j == 1
# im zweiten durchlauf ist i == 2, j ist zuerst 0 -> i+j == 2 , im zweiten durchlauf j == 1 -> i+j == 3
# 1, 2, 3

# 2. Welche Zahlen werden durch das folgende Programm ausgegeben?
i = 0
j = 9
while i < j:
    print(i, j)
    if i >= 3:
        break
    i += 1
    j -= 1
# 0 9
# 1 8
# 2 7
# 3 6


# 3. Schreiben Sie eine while-Schleife und eine for-Schleife, die jeweils in 5erSchritten von 100 bis 0 zählt.
counter = 100
while counter >= 0:
    print(counter)
    counter -= 5

for i in range(100, -1, -5):
    print(i)

# Aufgabe 2 (Klassifizierung von Schrauben)
# Ein Hersteller klassifiziert Schrauben nach folgendem Schema:
#     • Schrauben mit einem Durchmesser bis zu 3mm und einer Länge bis
#     zu 20mm sind vom Typ1.
#     • Schrauben mit einem Durchmesser von 4 bis 6mm und einer Länge
#     von 21 bis 30mm sind vom Typ2.
#     • Schrauben mit einem Durchmesser von 7 bis 20mm und einer Länge
#     von 31 bis 50mm sind vom Typ3.
# Schreiben Sie ein Programm Schrauben, die den richtigen Schraubentyp
# ermittelt, wenn Durchmesser und Länge als ganze Zahlen eingegeben
# werden. Sollte eine Schraube keiner der oben beschriebenen Kategorien
# angehören, soll die Meldung „Unbekannter Schraubentyp“ ausgegeben
# werden. Testen Sie Ihr Programm für verschiedene Eingaben.

while True:
    diameter = int(input("Durchmesser: "))
    length = int(input("Laenge: "))

    if diameter <= 3 and length <= 20:
        print(f"Typ 1\n")
    elif 4 <= diameter <= 6 and 21 <= length <= 30:
        print(f"Typ 2\n")
    elif 7 <= diameter <= 20 and 31 <= length <= 50:
        print(f"Typ 3\n")
    else:
        print(f"------ Unbekannter TYP ------\n\n")

# Aufgabe 3 (Schaltjahr)
# Schreiben Sie ein Programm „Kalender“ zum Bestimmen der Anzahl der
# Tage in einem Monat.
# Der Benutzer soll einen Monat (1-12) und einen ein Jahr (0-4000)
# eingeben. Danach werden die Anzahl der Tage in diesem Monat
# ausgegeben.
# Prof. Dr. Christian Cseh, Fakultät Wirtschaftsingenieurwesen
# SFM2, http://moodle.hs-esslingen.de/moodle/ Seite 2
# Beachten Sie hierbei die Problematik des Schaltjahrs, bei dem der Februar
# 29 statt 28 Tage besitzt. Ein Schaltjahr ist dann, wenn die Jahreszahl durch
# vier und nicht durch 100 teilbar ist oder wenn die Jahreszahl durch 400
# teilbar ist.
while True:
    month = 0
    while month not in range(1, 13):
        month = int(input("\nMonat: "))

    year = -1
    while year not in range(0, 4001):
        year = int(input("Jahr: "))

    if month % 2 == 0:
        if month == 2:
            if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
                print("Schaltjahr! 29 Tage")
            else:
                print("Tage = 28")
        else:
            print("Tage = 30")
    else:
        print("Tage = 31")

# Zusatzaufgabe
# Schreiben Sie ein Programm zum Zahlenraten: Zu Beginn kann der
# Benutzer über ein Textmenü wählen, ob er:
# ein (N)eues Spiel starten oder
# den (L)evel festlegen oder
# das Spiel (B)eenden möchte.
# Bei (N)eues Spiel starten wird eine Zufallszahl im Bereich zwischen 1 und
# (10 * Level) ermittelt, aber nur der Bereich angezeigt.
# Dann wird der Benutzer nach seinem Tipp gefragt.
# Bei der Eingabe „0“ gibt der Spieler auf und die Zufallszahl wird angezeigt.
# Danach erfolgt die Rückkehr zum Menü.
# Bei einer Zahl ungleich 0 wir dem Spieler per Textausgabe angezeigt, ob
# sein Tipp größer oder kleiner als die Zufallszahl ist. Hat er die Zahl erraten,
# wird die Anzahl der Versuche ausgegeben und es erfolgt die Rückkehr zum
# Menü. An sonst wir der Versuch gezählt und die Tipp-Eingabe wiederholt.
# Bei (L)evel wird der Benutzer nach einer Zahl für das Spiellevel gefragt. Sie
# muss größer als 1 sein. Danach erfolgt die Rückkehr zum Menü.
# Die Eingabe „B“ beendet das Programm
import random

game_selection = ""
level = 2
while game_selection != "B":
    game_selection = str(input("(N)eues Spiel\n"
                               f"(L)evel [{level}]\n"
                               "(B)eenden\n"
                               "\nEingabe: "))

    if game_selection == "N":
        number_to_guess = random.randint(1, 10 * level)
        guess_counter = 0
        guess_input = -1
        while guess_input != number_to_guess:
            guess_counter += 1
            guess_input = int(input(f"{guess_counter}. Guess [1 - {10 * level}]: "))

            if guess_input == 0:
                print(f"Aufgegeben!!! Die Zahl war {number_to_guess}")
                break
            if guess_input < number_to_guess:
                print("Guess was too low")
            if guess_input > number_to_guess:
                print("Guess was too high")
        if guess_input == number_to_guess:
            print(f"\nDie Eingabe war Korrekt! Benötigte Versuche: {guess_counter}\n")

    if game_selection == "L":
        level = 0
        while level < 2:
            level = int(input("Level setzen [größer als 2]: "))
