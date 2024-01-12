# main.py

# Importiert die notwendigen Bibliotheken
import machine
import utime
import dice_library
import lowpower

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
        last_button_press = utime.ticks_ms()
        dice_animation(maxDisplayableNumber, leds, dice)
        roll_dice_and_display(maxDisplayableNumber, leds, dice)
    else:
        sleep_if_needed()
