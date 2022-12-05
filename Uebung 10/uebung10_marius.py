# Prof. Dr. Christian Cseh, Fakultät Wirtschaftsingenieurwesen
# SFM2, http://moodle.hs-esslingen.de/moodle/ Seite 1
# SFM2 Python Programmierung
# Übung 10
# Aufgabe 1
# Verändern Sie die Klasse „Auto“ aus der letzten Übung 9, Aufgabe 1:
# - Schützen Sie die Instanzvariable „Kilometerstand“ als private Variable
# durch eine entsprechende property.
# Ergänzen Sie die vorhandenen Instanzvariablen um:
# - eine Klassenvariable „automatik“, die im Konstruktor über einen weiteren
# Parameter von Typ bool belegt wird. Zählen Sie die neu erzeugten AutoObjekte mit und ohne Automatik. Schreiben Sie eine statische Methode,
# welche die Anzahl der Autos mit und ohne Automatik ausgibt.
# - eine Referenz auf ein Autoradio. Das Programm soll also zusätzlich zu der
# Klasse „Auto“ noch über eine Klasse „Autoradio“ verfügen. Der __init__()-
# Methode der Klasse „Autoradio“ soll der Markenname des Radios sowie ein
# bool-Argument übergeben werden. Dieses bestimmt, ob das Autoradio noch
# über einen CD-Player verfügt (True) oder nicht (False). Zudem soll eine
# Methode namens zeige_daten() eingebaut werden, die Informationen zu
# dem Markennamen und der Ausstattung (CD-Player) ausgibt.
# In der main()-Methode sollen zunächst drei Instanzen der Klasse Autoradio
# erzeugt werden, die sich in Markenname und Ausstattung (CD-Player)
# unterscheiden. Erzeugen Sie im Anschluss noch drei Instanzen der Klasse Auto
# und weisen Sie ihnen unterschiedliche Attribute und Autoradios zu. Lassen Sie
# sich zum Schluss noch die Daten aller Autos mittels der Methode zeige_daten()
# ausgeben.


# Aufgabe 2
# Implementieren Sie eine Klasse Schrank mit den Instanzvariablen name für den
# Modellnamen, einem Tupel abmessung für die Breite, Tiefe und Höhe und
# preis für den Preis. Erstellen Sie 2 statische Methoden für zwei
# Einheitsschränke sowie für einen Konstruktor für einen allgemeinen
# Schranktyp. Schreiben Sie neben den notwendigen Getter- und SetterMethoden noch die folgenden Methoden:
# • getVolumen()

# Berechnen des Volumens eines Schrankes.
# • getPreis()

# Berechnen des Preises eines Schrankes über die Formel preis = cbm*100.-€
# aus dem Volumen.

# • getInfo()
# Rückgabe der vollständigen Schrankeigenschaften als Zeichenkette.
# • getAnzahl()
# Rückgabe der Anzahl der definierten Schränke mit Hilfe der Klassenvariablen
# zaehler.
# Testen Sie anschließend diese Klasse mit mehreren definierten
# Schrankobjekten.