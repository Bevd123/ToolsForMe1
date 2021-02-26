import os

Los = input("Gebe Pfad der Datei an die du löschen möchtest")

try:
    os.remove(Los)
except:
    input("Die Datei wurde nicht Gefunden")
else:
    input("Alles gut Gelaufen")
    print("Drücke enter zum schliessen")