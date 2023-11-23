# main.py

# Importiert die notwendigen Bibliotheken
import machine
import utime
import random

# Erstellt eine Liste von Pin-Objekten für die LEDs
led_pins = [16, 17, 18, 19, 20, 21, 22]
leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

# Erstellt ein Pin-Objekt für den Knopf
button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Initialisiert die Variable mit dem Startwert
global last_button_press
last_button_press = utime.ticks_ms()

# Definiert, welche LEDs für jede Zahl leuchten sollen
dice = {
    1: [3],
    2: [0, 6],
    3: [0, 3, 6],
    4: [0, 2, 4, 6],
    5: [0, 2, 3, 4, 6],
    6: [0, 1, 2, 4, 5, 6]
}

def display_number(n):
    # Stellt sicher, dass n zwischen 1 und 6 liegt
    n = max(1, min(n, 6))
    
    # Schaltet alle LEDs aus
    for led in leds:
        led.value(0)
    
    # Schaltet die entsprechenden LEDs ein
    for i in dice[n]:
        leds[i].value(1)

def dice_animation():
    # Führt die Würfelanimation aus
    for i in range(6):
        display_number(i + 1)
        utime.sleep(0.3)

def roll_dice_and_display():
    # Generiert eine zufällige Zahl von 1 bis 6
    n = random.randint(1, 6)
    
    # Zeigt die Zahl auf den LEDs an
    display_number(n)

def check_button_and_roll():
    # Aktualisiert die Zeit des letzten Tastendrucks
    global last_button_press 
    last_button_press = utime.ticks_ms()
    
    # Führt die Würfelanimation aus und zeigt eine zufällige Zahl an
    dice_animation()
    roll_dice_and_display()

def sleep_if_needed():
    global last_button_press
    # Überprüft, ob seit dem letzten Tastendruck 5 Sekunden vergangen sind
    if utime.ticks_diff(utime.ticks_ms(), last_button_press) > 5000:
        # Schaltet alle LEDs aus
        for led in leds:
            led.value(0)


while True:
    if button.value() == 1:
        utime.sleep(0.02)
        check_button_and_roll()
    else:
        sleep_if_needed()
