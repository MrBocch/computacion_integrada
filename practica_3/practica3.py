import serial
from time import sleep
from gpiozero import LED

sleep(2)

def dividirRango(valor):
    if valor <= 102:
        return 0
    elif valor <= 204:
        return 1
    elif valor <= 306:
        return 2
    elif valor <= 408:
        return 3
    elif valor <= 510:
        return 4
    elif valor <= 612:
        return 5
    elif valor <= 714:
        return 6
    elif valor <= 816:
        return 7
    elif valor <= 918:
        return 8
    else:
        return 9

def num_dig(num):

    for led in display:
        led.off()

    if num == 0:
        for led in display:
            led.on()
            dpF.off()

    if num == 1:
        dpB.on()
        dpC.on()
    elif num == 2:
        dpA.on()
        dpB.on()
        dpF.on()
        dpE.on()
        dpD.on()
    elif num == 3:
        dpA.on()
        dpB.on()
        dpF.on()
        dpC.on()
        dpD.on()
    elif num == 4:
        dpG.on()
        dpF.on()
        dpB.on()
        dpC.on()
    elif num == 5:
        dpA.on()
        dpG.on()
        dpF.on()
        dpC.on()
        dpD.on()
    elif num == 6:
        dpG.on()
        dpF.on()
        dpE.on()
        dpC.on()
        dpD.on()
        dpE.on()
    elif num == 7:
        dpA.on()
        dpB.on()
        dpC.on()
    elif num == 8:
        for led in display:
            led.on()
    elif num == 9:
        for led in display:
            led.on()
        dpE.off()

def num_led(num):
    for led in leds:
        led.off()

    for i in range(0, num):
        leds[i].on()


dpA = LED(2)
dpB = LED(3)
dpC = LED(4)
dpD = LED(17)
dpE = LED(27)
dpF = LED(22)
dpG = LED(10)
display = [dpA, dpB, dpC, dpD, dpE, dpF, dpG]

led1 = LED(9)
led2 = LED(11)
led3 = LED(5)
led4 = LED(6)
led5 = LED(13)
led6 = LED(19)
led7 = LED(14)
led8 = LED(15)
led9 = LED(21)
leds = [led1, led2, led3, led4, led5, led6, led7, led8, led9]

ser = serial.Serial("/dev/ttyACM0", 9600)

while True:
    data = ser.readline().decode("utf-8").strip()
    numero = dividirRango(int(data))
    print(data)

    num_dig(numero)
    num_led(numero)
