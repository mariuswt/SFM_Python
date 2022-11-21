# Aufgabe 2

"""
a)
Schreiben Sie ein Python-Script, das ein Dictionary erstellt mit den Zahlen 1-100 als Schlüssel und einem Boolean-Wert,
der angibt, ob die Zahl eine Primzahl ist.
"""

liste_zahl = list(range(1,101))
liste_boolean=list(range(1,101))
y = True

for x in liste_zahl: # Warum funktionierte jedoch nicht "for x in liste_zahlen"?
    if (x%2 != 0):
        y = True
    else:
        y = False
    liste_boolean [x-1] = y

dictionary = dict(zip(liste_zahl,liste_boolean))
print(dictionary)

#print(list(dictionary.keys())[0:3])
"""
b)
Als nächstes sollen die Zahlen 1-100 in zwei Listen sortiert werden: Primzahlen sollen in eine Liste, Nicht-Primzahlen 
in eine andere Liste einsortiert werden. Quelle der zu sortierenden Zahlen ist das Dictionary aus a). Da geplant ist, 
später jederzeit neue Zahlen in das Dictionary einzutragen, sollen die bereits sortierten Zahlen aus dem Dictionary 
schrittweise entfernt werden.
"""

liste_primzahlen = [x for x in dictionary if dictionary.__getitem__(x)==True]
liste_nicht_primzahlen = [x for x in dictionary if dictionary.__getitem__(x)==False]
print(liste_primzahlen)
print(liste_nicht_primzahlen)

"""for x in range(len(liste_primzahlen)):
    if(liste_primzahlen[x+1] == dictionary.__getitem__(x+1)):
        del dictionary[x+1]"""

for x in liste_primzahlen:
    del dictionary[x]
print(dictionary)

for x in liste_nicht_primzahlen:
    del dictionary[x]
print(dictionary)



"""dictionary = {1:"h",2:"J",3:"l"}

newList= [key for key in dictionary if key==2]
for key in newList:
    del dictionary[key]
    print(dictionary)
print(newList)"""


# Wenn ich nur bestimmte Stellen im Dicitionary löschen möchte
"""myDict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
delete = []
for key in myDict:
    if key == 3:
        delete.append(key)

print(delete)

for i in delete:
    del myDict[i]

print(myDict)
"""


