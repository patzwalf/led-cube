# main.py

# Importiert die notwendigen Bibliotheken
import machine
import utime
import random

# Erstellt eine Liste von Pin-Objekten für die LEDs
led_pins = [21, 22, 24, 25, 26, 27, 29]
leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

# Erstellt ein Pin-Objekt für den Knopf
button = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)

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
    for _ in range(10):
        for i in range(6):
            display_number(i + 1)
            utime.sleep(0.5)

def roll_dice_and_display():
    # Generiert eine zufällige Zahl von 1 bis 6
    n = random.randint(1, 6)
    
    # Zeigt die Zahl auf den LEDs an
    display_number(n)

def check_button_and_roll(pin=None):
    # Aktualisiert die Zeit des letzten Tastendrucks
    global last_button_press
    last_button_press = utime.ticks_ms()
    
    # Führt die Würfelanimation aus und zeigt eine zufällige Zahl an
    dice_animation()
    roll_dice_and_display()

def sleep_if_needed():
    print("Going to sleep in: " + str(10000-utime.ticks_diff(utime.ticks_ms(), last_button_press)))
    # Überprüft, ob seit dem letzten Tastendruck 10 Sekunden vergangen sind
    if utime.ticks_diff(utime.ticks_ms(), last_button_press) > 10000:
        # Schaltet alle LEDs aus
        for led in leds:
            led.value(0)
        
        # Aktuell ist KEINE Möglichkeit bekannt, den Pico wieder aufzuwecken daher keine Sleep-Funktion
        # Versetzt den Pico in den Ruhemodus und setzt Aufwachknopf
        #button.irq(trigger=machine.Pin.IRQ_FALLING, wake=machine.SLEEP)
        #machine.lightsleep()
        #button.irq(trigger=machine.Pin.IRQ_RISING, handler=check_button_and_roll)

# Setzt den ISR für den Knopf
button.irq(trigger=machine.Pin.IRQ_RISING, handler=check_button_and_roll)
last_button_press = utime.ticks_ms()

while True:
    if button.value() == 1:
        check_button_and_roll()
    else:
        sleep_if_needed()