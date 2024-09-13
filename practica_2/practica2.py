#! /usr/bin/python3
from gpiozero import LED
from time import sleep

def binario_a_led(numero, leds):
    for i in range(0, 8):
        if (numero[i] == "0"):
            leds[i].off()
        else:
            leds[i].on()

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
led4 = LED(26)
led5 = LED(23)
led6 = LED(24)
led7 = LED(25)
led8 = LED(16)
leds = [led1, led2, led3, led4, led5, led6, led7, led8]

for n in range(0, 256):
    print(n)

    binario = format(n, '08b')
    binario = [char for char in binario]

    binario_a_led(binario, leds) 
    sleep(1)
    
