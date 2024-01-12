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

#Erstellt DORMANT_PIN
DORMANT_PIN = 15

# Initialisiert den Zeitmesser mit dem Startwert
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

while True:
    if button.value() == 1:
        utime.sleep(0.02)
        last_button_press = utime.ticks_ms()
        dice_library.dice_animation(6, leds, dice)
        dice_library.roll_dice_and_display(6, leds, dice)
    elif utime.ticks_diff(utime.ticks_ms(), last_button_press) > 20000:
        # Überprüft, ob seit dem letzten Tastendruck 20 Sekunden vergangen sind
        # Schaltet alle LEDs aus
        for led in leds:
            led.value(0)
        print("going dormant")
        lowpower.dormant_with_modes({DORMANT_PIN: lowpower.EDGE_HIGH})