# Übung 8
# Aufgabe 1


# 1. Bearbeiten Sie nochmals Übung 6, Aufgabe 1, Frage 1:
# Definieren Sie in Python eine Liste mit den Vielfachen von 7, die kleiner als
# 100 sind (also [7, 14,..., 98]). Verwenden Sie diesmal die filter()- und eine
# geeignete Lambda-Funktion.


ismodolo = lambda number: number % 7 == 0

liste = list(range(1, 101))
liste_mod7 = list(filter(ismodolo, liste))

print(liste_mod7)

# 2. Extrahieren Sie aus der Zeichenkette „Hello, World!“ alle Vokale, verbinden
# Sie diese zu einer neuen Zeichenkette und geben Sie diese aus.

is_vocal = lambda char: char == "a" or char == "e" or char == "i" or char == "o" or char == "u"

my_string = "Hello, World!"
my_string_vocal = "".join(filter(is_vocal, my_string))
print(my_string_vocal)


# 3. Schreiben Sie eine Funktion vertauschen(), die als Übergabeparameter eine
# Liste a und die zwei Indizes i und j für die zu vertauschenden Positionen
# erhält. Nach dem Vertauschen sollen die Einträge in der Liste an den Stellen
# i und j vertauscht sein. Also z.B.:
# liste = [Mo, Di, Mi, Do, Fr, Sa, So]
# vertauschen (liste, 1, 3)
# print (liste) # [Mi, Di, Mo, Do, Fr, Sa, So]
# Ist dazu ein Rückgabewert notwendig? Testen Sie Ihre Funktion.
def vertauschen(liste, i, j):
    buffer = liste[i - 1]
    liste[i - 1] = liste[j - 1]
    liste[j - 1] = buffer
    return liste


liste = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
vertauschen(liste, 1, 3)
print(liste)
# Nein ein rückgabewert ist nicht notwendig! eine Liste ist Mutable, die Liste wird direkt am speicherort verändert