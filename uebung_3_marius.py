import decimal
import random

# **Aufgabe 1**
#
# Beantworten Sie die folgenden Fragen:
# 1. Sie wollen den Oktalcode 750 in binärer Darstellung anzeigen. Wie gehen Sie vor?
oktal = 0o750
print(bin(oktal))

# 2. Wie erzeugen Sie Zufallszahlen zwischen 1 und 49?
print(random.randint(1, 49))

# 3. Sie brauchen zwei Zufallszahlen zwischen 0,0 und 10,0. Schreiben Sie geeigneten Python-Code!
for i in range(0, 2):
    print(random.uniform(0.0, 10.0))

# 4. Sie wollen Geldbeträge ohne Rundungsfehler verarbeiten. Welchen Datentyp verwenden Sie?
geldbetrag = 1.234567
print(round(geldbetrag, 2))

value1 = decimal.Decimal("1.34")
value2 = decimal.Decimal("2.56")
summ = value1 + value2
print("Summe:", summ)

# 5. Welchem Zahlenwert ist True zugeordnet?
print(int(True))

# 6. Wie bilden Sie eine Zeichenkette, die selbst ein Anführungszeichen enthält?
formated_string = "Zeichen \"Kette mit\" Anführungszeichen"
print(formated_string)

# 7. Extrahieren Sie aus der folgenden Zeichenkette das Tag zwischen den eckigen Klammern: bla [wichtig] mehr bla
formated_string = "bla [wichtig] mehr bla"
first_index = formated_string.find("[")
second_index = formated_string.find("]")

print(formated_string[first_index + 1:second_index])

# 8. Geben Sie drei maximal fünfstellige Zahlen rechtsbündig aus.
my_numbers = {1, 12345, 123}
for my_number in my_numbers:
    print(f'{my_number}'.rjust(5, " "))

# 9. Geben Sie Hello,World! in umgekehrter Reihenfolge aus.
hello_world = "Hello,World!"
print(hello_world[::-1])

# Aufgabe 2
# Schreiben Sie ein Python-Script, das den Benutzer auffordert, eine Kommazahl
# einzugeben. Die eingegebene Zahl soll im Anschluss in ihre Vor- und
# Nachkommaanteile zerlegt werden. Diese sollen auf dem Bildschirm ausgegeben
# werden, wobei die Anzahl der Nachkommastellen auf sechs begrenzt sein soll. Das
# Ergebnis soll etwa so aussehen:
# Fließkommazahl eingeben: 913.745673849
# Vorkommaanteil: 913
# Nachkommaanteil: 0.745674

number_input = decimal.Decimal(input("Geben sie eine Dezimalzahl ein"))
number_integer = int(number_input)
number_decimal = number_input - decimal.Decimal(number_integer)
print("Fließkommazahl eingeben: ", number_input)
print("Vorkommaanteil: ", number_integer)
print("Nachkommaanteil: ", round(number_decimal, 6))
