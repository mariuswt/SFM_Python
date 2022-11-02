# Übung 4
# Aufgabe 1
# Beantworten Sie die folgenden Fragen:
# 1. Erläutern Sie den Unterschied zwischen den Vergleichsoperatoren:
# »==« und »is« sowie
# »!=« und »is not«.

# == wird für wertegleichheit verwendet.
# is frägt nach referenzgleichheit ab, zwei objekte müssen auf das selbe objekt zeigen
a = [1, 2, 3]
b = a
c = a[:]

print(f"a == b -> {a == b}")
print(f"a == c -> {a == c}")

print(f"a is b -> {a is b}")
print(f"a is c -> {a is c}\n")

# != fragt wieder auf werte-ungleichheit ab
# is not schaut, ob die referenz/speicheraddresse unterschiedlich ist
print(f"a != b -> {a != b}")
print(f"a != c -> {a != c}")

print(f"a is not b -> {a is not b}")
print(f"a is not c -> {a is not c}\n")

# 2. Sie wollen den Rest der Division 225 / 17 ermitteln. Wie lautet die
# Berechnung in python?
print(f"Int(225/17) = {int(225/17)} =>  Rest = {225 % 17}")

# 3. Erläutern Sie die Short-Circuit-Evaluation. Nennen Sie ein Beispiel!
# Bei einem OR verleich ist die Aussage true sobald die erste Bedingung übereinstimmt,
# nur wenn er false ist wird die zweite Bedingung überprüft

# Ist bei einem AND vergleich die erste Bedingung falsch werden die restlichen übersprungen und ebenfalls false ausgegeben

# Auswertung von Bedingungen bzw Vergleichen findet von links nach rechts statt.
print(f"True && True -> {True and True}")
print(f"True && False -> {True and False}\n")

print(f"True || True -> {True or True}")
print(f"True || False -> {True or False}")
print(f"False || False -> {False or False}\n")

# 4. Welchen Datentyp und Wert haben a und b?
a = 1 + 2 * 3 ** 4
b = 100 < a < 200
# a ist ein Integer, b ist Bool
print(f"a = {a}, Type = {type(a)}")
print(f"b = {b}, Type = {type(b)}")

# Aufgabe 2
# Schreiben Sie ein Programm Zinsen, das einen aktuellen
# Anfangskapitalwert K0 [Euro] mit einem Zinssatz p [%] nach n Jahren
# verzinst:
# Kn= K0 *(1 +p/100)^n
# Testbeispiele:
# K0 = 1000.00, n = 5, p = 2.0 folgt K5 = 1104.08
# K0 = 1000.00, n = 5, p = −2.0 folgt K5 = 903.92
K0 = round(float(input("Anfangskapitalwert: ")), 2)
p = float(input("Zinssatz: "))
n = int(input("Jahre: "))

print(f"K0 = {K0:.2f}, n = {n}, p = {p} --> K{n} = { round(K0 * (1 + p/100)**n, 2)}")
