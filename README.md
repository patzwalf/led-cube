# Projektbeschreibung

Dieses Projekt steuert eine LED-Würfelanzeige mit einem Raspberry Pi Pico.  
  
Der Workaround für den Energiesparmodus wurde freundlicherweise von tomjorquera erstellt. Er ist experimentell.   
Weitere Informationen auf der verlinkten Seite im Reiter "Verwendete Bibliotheken". 


## Verwendete Bibliotheken

- `machine`
- `utime`
- `_random`
- [`lowpower`](https://github.com/tomjorquera/pico-micropython-lowpower-workaround)
- `dice_library`

Ein paar Worte zur dice_library.py:  
Hier werden alle wichtigen Funktionen ausgelagert die für den Würfel gebraucht werden.  
Die Funktionen sind mit ausführlichem Doc im Code erklärt sowie alle nötigen Vorbedingungen und Fallstricke. Daher schaut Ihn euch vorher aufmerksam an. 

## Anschluss der LEDs

Die LEDs sind in aufsteigender Reihenfolge von 0 bis 6 an den PINs 21, 22, 24-27, 29 angeschlossen und der Knopf ist an Pin 20 angeschlossen.  
Der Code kann aber an euer Setup einfach angepasst werden um variabel viele LEDs zu verwenden. 

### Layout der LEDs im Beispiel

2___________6  
1_____3_____5  
0___________4  

### GPIO Pins und Beispielaufbau

Die GPIO Pins sind in der folgenden Grafik zu erkennen: ![Raspberry Pi Pico Pinout](https://www.raspberrypi.com/documentation/microcontrollers/images/picow-pinout.svg)  
Ein möglicher Aufbau für den Würfel ist im Repo zu finden:  
![Beispielaufbau](https://github.com/patzwalf/led-cube/blob/5a1680e16874a2c6c05078b42781f48f2e8cc4b3/Verkabelung%20LEDCube.JPG)

### MikroPython installieren
1) Ladet euch die aktuellste [MikroPython Version](https://micropython.org/download/RPI_PICO_W/) runter und speichert die .uf2 Datei.
2) Währed Ihr den Pico an den USB Anschluss eures Rechners anschließt haltet den Bootselect (BOOTSEL) Knopf gedrückt.
3) Zieht die .uf2 Datei auf das vom Pico bereitgestellte Laufwerk auf - damit ist die Installation von MikroPython abgeschlossen.
4) Trennt den Pico vom Strom und steckt ihn wieder an euer USB Laufwerk. Ab jetzt läuft der Pico im normalen Modus. 

### Thonny IDE installieren und benötigte Daten auf den Pico kopieren
1) Ladet euch die [Thonny IDE](https://thonny.org/) runter und installiert diese.
2) Ladet alle .py Datein aus dem Repository auf den Raspberry Pi Pico W indem Ihr Thonny benutzt. 
3) Macht euch mit dem Code vertraut. Wenn Ihr alle Datein auf dem Pico habt läuft ab jetzt automatisch das Würfelspiel (main.py). 
