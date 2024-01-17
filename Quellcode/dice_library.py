# dice_library.py
"""
Diese Bibliothek enthält Funktionen zur Anzeige von Zahlen und zur Durchführung einer Würfelanimation auf einem LED-Display.

Vorbedingungen:
- Die LEDs müssen in der richtigen Reihenfolge in einer Liste gespeichert werden. 
    Beispiel: # Erstellt eine Liste von Pin-Objekten für die LEDs
              led_pins = [16, 17, 18, 19, 20, 21, 22]
              leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

- Die darstellbaren Zahlen als LEDs müssen in der richtigen Reihenfolge in einem Wörterbuch gespeichert werden, dass die LED-Indizes für jede darstellbare Zahl enthält.
    Beispiel: # Definiert, welche LEDs für jede Zahl leuchten sollen
            dice = {
                1: [3],
                2: [0, 6],
                3: [0, 3, 6],
                4: [0, 2, 4, 6],
                5: [0, 2, 3, 4, 6],
                6: [0, 1, 2, 4, 5, 6]
            }

Funktionen:
- display_number(n, leds, dice): Zeigt eine bestimmte Zahl auf dem LED-Display an.
- dice_animation(maxDisplayableNumber, leds, dice): Führt eine Würfelanimation aus, indem sie Zahlen von 1 bis maxDisplayableNumber auf dem LED-Display anzeigt.
- roll_dice_and_display(maxDisplayableNumber, leds, dice): Generiert eine zufällige Zahl zwischen 1 und maxDisplayableNumber und zeigt sie auf dem LED-Display an.

Module:
- utime: Wird verwendet, um Pausen zwischen den Animationen zu erzeugen.
- random: Wird verwendet, um zufällige Zahlen für die Würfelanimation zu generieren.
"""

import utime
import random


def display_number(n, leds, dice):
    """
    Zeigt eine Zahl auf einem LED-Display an.

    Parameters:
    n (int): Die anzuzeigende Zahl. Darauf achten entsprechend der darstellbaren Zahlen im dice Setup zu verwenden.
    leds (list): Eine Liste von LED-Objekten, die das Display repräsentieren.
    dice (dict): Ein Wörterbuch, das die LED-Indizes für jede darstellbare Zahl enthält.

    Returns: None
    """
    # Schaltet alle LEDs aus
    for led in leds:
        led.value(0)
    # Schaltet die entsprechenden LEDs ein
    for i in dice[n]:
        leds[i].value(1)


def dice_animation(maxDisplayableNumber, leds, dice):
    """
    Führt eine Würfelanimation aus, indem sie Zahlen von 1 bis maxDisplayableNumber auf einem LED-Display anzeigt.

    Parameters:
    maxDisplayableNumber (int): Die maximale Zahl, die auf dem Display angezeigt werden kann.
    leds (list): Eine Liste von LED-Objekten, die das Display repräsentieren.
    dice (dict): Ein Wörterbuch, das die LED-Indizes für jede darstellbare Zahl enthält.

    Returns: None
    """
    for i in range(maxDisplayableNumber):
        display_number(i + 1, leds, dice)
        utime.sleep(0.3)


def roll_dice_and_display(maxDisplayableNumber, leds, dice):
    """
    Generiert eine zufällige Zahl zwischen 1 und maxDisplayableNumber und zeigt sie auf einem LED-Display an.

    Parameters:
    maxDisplayableNumber (int): Die höchste Zahl, die generiert werden kann. Darauf achten entsprechend der darstellbaren Zahlen im dice Setup zu verwenden.
    leds (list): Eine Liste von LED-Objekten, die das Display repräsentieren.
    dice (dict): Ein Wörterbuch, das die LED-Indizes für jede darstellbare Zahl enthält.

    Returns: None
    """
    # Generiert eine zufällige Zahl von low bis maxDisplayableNumber
    n = random.randint(1, maxDisplayableNumber)
    
    # Zeigt die Zahl auf den LEDs an
    display_number(n, leds, dice)
