# SFM2 Python Programmierung
# Übung 7

# Aufgabe 1
# 1. Die in Python vordefinierten Funktionen min() und max() ermitteln das
# kleinste bzw. größte Element einer Liste. Programmieren Sie die Funktion
# minmax(liste), die die beiden entsprechenden Elemente als Tupel
# zurückgibt – ohne min() und max() zu verwenden.
import decimal


def min_max(eingang):
    min = eingang[0]
    max = eingang[0]
    for element in eingang:
        if element < min:
            min = element
        if element > max:
            max = element
    min_max_values = (min, max)
    return min_max_values


feld = [44, 1, 2, 5, 22, 6, 8]
print(min_max(feld))


# 2. Ein Palindrom ist ein Text, der von vorn und hinten gelesen den gleichen
# Inhalt hat – z. B. »Lagerregal« oder »Trug Tim eine so helle Hose nie mit
# Gurt?«. Leer- und Satzzeichen werden dabei ignoriert.
# Schreiben Sie eine Funktion, die testet, ob eine Zeichenkette ein Palindrom
# ist. Tipp: Verwenden Sie die Funktion str.isalpha, um zu testen, ob ein
# Zeichen ein Buchstabe ist.

def palindrom(eingabe):
    eingabe_str = ''.join(filter(str.isalnum, eingabe)).lower()
    print(eingabe_str)
    for i in range(0, int(len(eingabe_str) / 2)):
        if eingabe_str[i] != eingabe_str[-i - 1]:
            return False
    return True


print(palindrom("Trug Tim eine so helle Hose nie mit Gurt!?-_"))


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

def contains_special_caracter(password):
    if any(not c.isalpha() for c in str(password)):
        return True
    return False


def upper_and_lower(password):
    contains_lower = False
    contains_upper = False
    if any(c.islower() for c in str(password)):
        contains_lower = True
    if any(c.isupper() for c in str(password)):
        contains_upper = True
    return contains_lower and contains_upper


def contains_six_character(password):
    used_chars = []
    for element in str(password):
        if element not in used_chars:
            used_chars += element
    if len(used_chars) > 6:
        return True
    return False


def contains_number(password):
    if any(c.isdigit() for c in str(password)):
        return True
    return False


def password_calculation(password):
    points = 0
    if len(password) < 8:
        return points
    else:
        print("8 chars")
        points += 1
    if upper_and_lower(password):
        print("upper and lower")
        points += 1
    if contains_six_character(password):
        print("six different")
        points += 1
    if contains_number(password):
        print("contains number")
        points += 1
    if contains_special_caracter(password):
        print("special char")
        points += 1
    return points


passwords = ["abc",
             "abcdefghij",
             "ab1122$$!!",
             "aBcd1234$!",
             "11111111111"
             ]
for password in passwords:
    print(password, password_calculation(password), "\n")


# 4. Schreiben Sie eine rekursive Python-Funktion, die als Count-Down die
# Zahlen n bis 0 auf dem Bildschirm ausgibt.

def count_down(n):
    for number in range(int(n), -1, -1):
        print(number)


count_down(3)


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
def neues_konto_anlegen():
    inhaber = str(input("Kontoinhaber: "))
    blz = input("BLZ: ")
    kontonummer = input("Kontonummer: ")
    kontostand = 0.00
    zinssatz = float(input("Zinssatz: "))
    konto = {
        "Kontoinhaber": inhaber,
        "Bankleitzahl": blz,
        "Kontonummer": kontonummer,
        "Kontostand": kontostand,
        "Zinssatz": zinssatz,
    }
    return konto


def einzahlen(konto):
    betrag = abs(float(input("Betrag zum Einzahlen: ")))
    konto["Kontostand"] += betrag
    return konto


def abheben(konto):
    betrag = abs(float(input("Betrag zum Auszahlen: ")))
    if konto["Kontostand"] - betrag >= 0:
        konto["Kontostand"] = round(konto["Kontostand"] - betrag, 2)
    else:
        print("KONTOSTAND WIRD NEGATIV")
    return konto


def zinsen_gutschreiben(konto):
    konto["Kontostand"] = round(konto["Kontostand"] * (1 + (konto["Zinssatz"]/100)), 2)
    return konto


def kontodaten_ausgeben(konto):
    print(konto["Kontoinhaber"],
          konto['Bankleitzahl'],
          konto['Kontonummer'],
          konto['Kontostand'],
          konto['Zinssatz'])


eingabe = 1
konto = {}
while eingabe != 0:

    eingabe = int(input("\n1. Konto neu anlegen\n"
                    "2. Einzahlen\n"
                    "3. Abheben\n"
                    "4. Zinsen gutschreiben\n"
                    "5. Kontendaten ausgeben\n\n"))
    if eingabe == 1:
        konto = neues_konto_anlegen()
    if eingabe == 2:
        konto = einzahlen(konto)
    if eingabe == 3:
        konto = abheben(konto)
    if eingabe == 4:
        konto = zinsen_gutschreiben(konto)
    if eingabe == 5:
        kontodaten_ausgeben(konto)

# Zusatzaufgabe
# Verändern Sie Ihr Programm zum Zahlenraten aus der Übung 5 so, dass
# einzelne Aufgaben des Programms in getrennten Funktionen implementiert
# sind. Versuchen Sie innerhalb der Funktionen keine globale Variable zu
# verändern.
