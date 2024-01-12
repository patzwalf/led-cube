# Projektbeschreibung

Dieses Projekt steuert eine LED-Würfelanzeige mit einem Raspberry Pi Pico. 

## Verwendete Bibliotheken

- `machine`
- `utime`
- `_random`
- [`lowpower`](https://github.com/tomjorquera/pico-micropython-lowpower-workaround)
- `dice_library` 

## Anschluss der LEDs

Die LEDs sind in aufsteigender Reihenfolge von 0 bis 6 an den PINs 21, 22, 24-27, 29 angeschlossen und der Knopf ist an Pin 20 angeschlossen.

## Layout der LEDs

2___________6  
1_____3_____5  
0___________4  

## GPIO Pins

Die GPIO Pins sind in der folgenden Grafik zu erkennen:

![Raspberry Pi Pico Pinout](https://www.raspberrypi.com/documentation/microcontrollers/images/picow-pinout.svg)

