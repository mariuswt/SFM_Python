# Aufgabe 1
"""

1. Bearbeiten Sie nochmals Übung 6, Aufgabe 1, Frage 1:
Definieren Sie in Python eine Liste mit den Vielfachen von 7, die kleiner als 100 sind (also [7, 14,..., 98]).
Verwenden Sie diesmal die filter()- und eine geeignete Lambda-Funktion.
"""
liste = list(range(1,101))
liste_siebener=list(filter(lambda x: x%7==0,liste))
print(liste_siebener)

"""
2. Extrahieren Sie aus der Zeichenkette „Hello, World!“ alle Vokale, verbinden Sie diese zu einer neuen Zeichenkette 
und geben Sie diese aus.
"""


zeichenkette = "Hello, World!"
liste_vokale = filter(lambda x: x=="a" or x =="e" or x=="i" or x=="o" or x=="u",zeichenkette)
print("".join(list(liste_vokale)))

"""
3. Schreiben Sie eine Funktion vertauschen(), die als Übergabeparameter eine Liste a und die zwei Indizes i und j für 
die zu vertauschenden Positionen erhält. Nach dem Vertauschen sollen die Einträge in der Liste an den Stellen i und j 
vertauscht sein. Also z.B.:
liste = [Mo, Di, Mi, Do, Fr, Sa, So]
vertauschen (liste, 1, 3)
print (liste) # [Mi, Di, Mo, Do, Fr, Sa, So]
Ist dazu ein Rückgabewert notwendig? Testen Sie Ihre Funktion.
"""
def vertauschen (liste, i, j):
    if (1<=i<=len(liste) and 1<=j<=len(liste)):
        buffer = liste[i - 1] # Mo
        liste[i - 1] = liste[j - 1] # ["Mi", "Di", "Mi", "Do", "Fr", "Sa", "So"]
        liste[j - 1] = buffer # ["Mi", "Di", "Mo", "Do", "Fr", "Sa", "So"]
    else:
        print("Ungültiger Zahlenbereich. Bitte geben Sie ausschließlich Zahlenwerte im Bereich 1 und",len(liste))

"Bei einer Liste muss man nicht return mitgeben, da sie mutable ist und somit Änderungen in einer Funktion, die Liste " \
"außerhalb dieser Funktion ebenfalls ändert"

liste = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
vertauschen (liste,0, 7)



