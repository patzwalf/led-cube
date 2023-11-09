# main.py

# Importiert die notwendigen Bibliotheken
import machine
import utime
import _random

# Erstellt Pin-Objekte für die LEDs
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(25, 32)]

# Erstellt ein Pin-Objekt für den Knopf
button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

# Definiert, welche LEDs für jede Zahl leuchten sollen
dice = {
    1: [3],
    2: [0, 5],
    3: [0, 3, 5],
    4: [0, 1, 4, 5],
    5: [0, 1, 3, 4, 5],
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
            utime.sleep(0.1)

last_button_press = utime.ticks_ms()

while True:
    # Überprüft, ob der Knopf gedrückt wurde
    if button.value() == 0:
        # Aktualisiert die Zeit des letzten Tastendrucks
        last_button_press = utime.ticks_ms()
        
        # Führt die Würfelanimation aus
        dice_animation()
        
        # Wartet, bis der Knopf losgelassen wurde
        while button.value() == 0:
            pass
        
        # Generiert eine zufällige Zahl von 1 bis 6
        n = _random.randint(1, 6)
        
        # Zeigtdie Zahl auf den LEDs an
        display_number(n)
        
        # Wartet eine Sekunde, bevor die nächste Zahl anzeiget wird
        utime.sleep(1)
    else:
        # Überprüft, ob seit dem letzten Tastendruck 10 Sekunden vergangen sind
        if utime.ticks_diff(utime.ticks_ms(), last_button_press) > 10000:
            # Schaltet alle LEDs aus
            for led in leds:
                led.value(0)
            
            # Versetzt den Pico in den Ruhemodus
            machine.lightsleep(10000)
            button.irq(trigger=machine.Pin.IRQ_FALLING, wake=machine.DEEPSLEEP)