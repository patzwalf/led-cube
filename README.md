Dieses Projekt steuert eine LED-Würfelanzeige mit einem Raspberry Pi Pico. 
Es verwendet die Bibliotheken machine, utime und _random. 
Die LEDs sind in aufsteigender Reihenfolge von 0 bis 6 an den PINs 21,22,24-27,29 angeschlossen und der Knopf ist an Pin 20 angeschlossen.

Layout der LEDs:

2       6
1   3   5
0       4

Die GPIO Pins sind in der folgenden Grafik zu erkennen:
![alt text](https://www.raspberrypi.com/documentation/microcontrollers/images/picow-pinout.svg)
