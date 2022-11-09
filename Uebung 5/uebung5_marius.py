# Übung 5
# Aufgabe 1
# Beantworten Sie die folgenden Fragen:
# 1. Was wird bei der Ausführung des folgenden Codes ausgegeben?
# for i in range(1 , 3):
#      for j in range(i):
#          print(i+j)


# 2. Welche Zahlen werden durch das folgende Programm ausgegeben?
# i=0; j=9
# while i<j:
#     print(i, j)
#     if i>=3:
#         break
#     i+=1
#     j-=1


# 3. Schreiben Sie eine while-Schleife und eine for-Schleife, die jeweils in 5erSchritten von 100 bis 0 zählt.
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