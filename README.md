# Projektbeschreibung

Dieses Projekt steuert eine LED-Würfelanzeige mit einem Raspberry Pi Pico. 

## Verwendete Bibliotheken

- `machine`
- `utime`
- `_random`

## Anschluss der LEDs

Die LEDs sind in aufsteigender Reihenfolge von 0 bis 6 an den PINs 21, 22, 24-27, 29 angeschlossen und der Knopf ist an Pin 20 angeschlossen.

## Layout der LEDs

2   6
1 3 5
0   4

## GPIO Pins

Die GPIO Pins sind in der folgenden Grafik zu erkennen:

![Raspberry Pi Pico Pinout](https://www.raspberrypi.com/documentation/microcontrollers/images/picow-pinout.svg)

