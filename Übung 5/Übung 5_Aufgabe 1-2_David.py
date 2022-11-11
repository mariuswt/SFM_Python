# Aufgabe 1
"""1. Was wird bei der Ausführung des folgenden Codes ausgegeben?
for i in range(1 , 3):
    for j in range(i):
        print(i+j)
i=1) 1+0
i=2) (2+0)
i=2) (2+1)  j=2 wird gar nicht eingesetzt, weil der Endwert immer exklusive ist
"""
"""for i in range(1 , 3):
    for j in range(i+2):
        print(i+j)
i=1) 1+0 =1
i=1) 1+1 =2
i=1) 1+2 =3
i=2) 2+0 =2
i=2) 2+1 =3
i=2) 2+2 =4
i=2) 2+3 =5
i=3) wird gar nicht durchlaufen, weil der Endwert immer exkliusive ist.

   for _ in range (10):
    #print ("10 mal diesen Text ausgeben")
    print(_)"""
for i in range(1 , 3):
    for j in range(i):
        print(i+j)


"""
2. i=0; j=9
while i<j: 
    print(i, j)
    if i>=3: 
        break
    i+=1 
    j-=1

1)0 9
2)1 8
3)2 7
4)3 6
5) geht nicht mehr weiter, weil man mit break die komplette While-Schleife verlässt
"""
i=0; j=9
while i<j:
    print(i, j)
    if i>=3:
        break
    i+=1
    j-=1

"""
3. 
Schreiben Sie eine while-Schleife und eine for-Schleife, die jeweils in 5er- Schritten von 100 bis 0 zählt.
"""
x = 5
endwert = 100
y = endwert
while (x<=y):
    if (y==endwert):
        print(endwert)
    y= y-x
    print(y)

for x in range (100, -1, -5):
    print (x)


#Aufgabe 2
schrauben = {"Typ 1":"Durchmesser: 0-3mm | Länge: 0-20mm",
             "Typ 2":"Durchmesser: 4-6mm | Länge: 21-30mm",
             "Typ 3":"Durchmesser: 7-20mm | Länge: 31-50 mm"}

durchmesser = int(input("Durchmesser in mm:"))
laenge = int(input("Länge in mm:"))

while(durchmesser <0 or laenge <0):
    print ("Ungültige Eingabe! Geben Sie bitte einen Durchmesser und eine Länge, die größer 0 sind!")
    durchmesser = int(input("Durchmesser in mm:"))
    laenge = int(input("Länge in mm:"))
if (0<= durchmesser <= 3 and 0<= laenge <=20):
    print("Typ 1:\n",schrauben.__getitem__("Typ 1"))
elif (4 <= durchmesser <= 6 and 21 <= laenge <= 30):
    print("Typ 2:\n",schrauben.__getitem__("Typ 2"))
elif(7 <= durchmesser <= 20 and 31 <= laenge <= 50):
    print("Typ 3:\n",schrauben.__getitem__("Typ 3"))
else:
    print("Unbekannter Schraubentyp!")


