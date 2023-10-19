import machine
import random
import time

button = machine.Pin(0, machine.Pin.IN)

led1 = machine.Pin(1, machine.Pin.OUT)
led2 = machine.Pin(2, machine.Pin.OUT)
led3 = machine.Pin(3, machine.Pin.OUT)
led4 = machine.Pin(4, machine.Pin.OUT)
led5 = machine.Pin(5, machine.Pin.OUT)
led6 = machine.Pin(6, machine.Pin.OUT)
led7 = machine.Pin(7, machine.Pin.OUT)

numbers = (
        [led4],  # Zahl 1
        [led1, led7],  # Zahl 2
        [led1, led4, led7],  # Zahl 3
        [led1, led3, led5, led7],  # Zahl 4
        [led1, led3, led4, led5, led7],  # Zahl 5
        [led1, led2, led3, led5, led6, led7]  # Zahl 6
)

def resetLeds():
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    led5.value(0)
    led6.value(0)
    led7.value(0)

def showNumber(leds):
    resetLeds()
    for led in leds:
        led.value(1)

while True:
    if button.value():
        number = int(random.uniform(1, 6))
        showNumber(numbers[number - 1])
        time.sleep(1)  # Optional: Delay for 1 second to display the number for a short time
