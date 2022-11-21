# Aufgabe 1

"""
1) Definieren Sie in Python eine Liste mit den Vielfachen von 7, die kleiner als 100 sind (also [7, 14,..., 98]).
"""
lst = list (range(7,101,7))
print(lst)

"""
2) Welchen Datentyp verwenden Sie, um Lottozahlen zu speichern?
Tupel mit dem Datentyp integer
"""
lottozahlen = (1,2,5,3,4,6)
print(set(lottozahlen))
"""
3) Schreiben Sie ein Python-Script, das die folgende Matrix umsetzt:
2 4 6 
5 3 1
und danach die Anzahl der Zeilen und die Anzahl der Spalten ausgibt.
"""
matrix = [[2,4,6],[5,3,1]]

print("\nMatrixausgabe:")
for x in range(0,len(matrix)):
    #for y in range(len(matrix[0])):
        #print(matrix[x][y])
    print(str(matrix[x]).replace("[","").replace("]","").replace(",",""))
print("Anzahl der Spalten: ", len(matrix[0]))
print("Anzahl der Zeilen:  ", len(matrix))

"""
ipmort numpy as np
array = np.arrray ([[2,4,6],[5,3,1]]
rows, columns = array.shape
print ("Rows = ", rows)
print ("Columns = ", columns)
"""
"""
4) Erläutern Sie den Unterschied zwischen den folgenden Python-Befehlen für zwei Sets x und y:
print (x – y)
print (y – x)

print(x - y):
Hier nehme ich den Set x und nehme aus dieser Menge alle Elemente raus, die auch in y vorhanden sind. Y selber wird 
jedoch nicht in die Menge von x aufgenommen.
Beispiel
x = set (abcdef)
y = set (efgh) 
print (x - y) --> abcd

print (y - x):
Hier nehme ich den Set y und nehme aus dieser Menge alle Elemente raus, die auch in x vorhanden sind. X selber wird 
jedoch nicht in die Menge von y aufgenommen.
Beispiel
x = set (abcdef)
y = set (efgh) 
print (y - x) --> gh
"""
x = set ("abcdef")
y = set ("efgh")
print(x-y)
print(y-x)

"""
5) Welches sind die gemeinsamen Buchstaben der Wörter „Python“ und „Programmierung“?
"""
python = set("Python")
programmierung = set("Programmierung")
print(python & programmierung)

"""
6) Entfernen Sie die Doppelgänger aus der folgenden Liste von Zahlen: 
   [1, 2, 3, 2, 7, 3, 9]. Die Ergebnisliste soll aufsteigend sortiert sein.
"""
liste = [1, 2, 3, 2, 7, 3, 9]
liste_neu = list(set(liste))
print(liste_neu)

#Um nur die Doppelgänger herauszukriegen
set_2= set(filter(lambda x: liste.count(x)>1,liste))
print(set_2)

