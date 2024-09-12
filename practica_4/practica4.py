from gpiozero import MotionSensor, Buzzer, Button, LED
import time

time.sleep(1)

def mode1_1(leds):
    for i in range(3):
        leds[i].on()
    for i in range(3,6):
        leds[i].off()


def mode1_2(leds):
    for i in range(3):
        leds[i].off()
    for i in range(3,6):
        leds[i].on()

def mode2_1(leds):
    apagar(leds)
    leds[1].on()
    leds[3].on()
    leds[5].on()

def mode2_2(leds):
    apagar(leds)
    leds[0].on()
    leds[2].on()
    leds[4].on()

def apagar(leds):
    for led in leds:
        led.off()


buzzer = Buzzer(26)
sensor = MotionSensor(14)
btn1 = Button(6)
btn2 = Button(5)

led1 = LED(22)
led2 = LED(27)
led3 = LED(17)
led4 = LED(4)
led5 = LED(3)
led6 = LED(2)
leds = [led1, led2, led3, led4, led5, led6]

alarma = False
buzzer_prendido = False
apagar(leds)
mode = 2

lastT = time.time()

while True:
    curT = time.time()

    if btn1.is_pressed:
        print("cambiar de mode")
        if mode == 1:
            mode = 2
            time.sleep(0.1)
        else:
            mode = 1
            time.sleep(0.1)
    if btn2.is_pressed:
        print("apagar alarma")
        alarma = False
        buzzer.off()
        apagar(leds)


    if alarma:
        if buzzer_prendido:
            if (curT - lastT) >= 1:
                buzzer.off()
                buzzer_prendido = False
                lastT = curT
            if mode == 1:
                mode1_1(leds)
            else:
                mode2_1(leds)

        else:
            if (curT - lastT) >= 0.5:
                buzzer.on()
                buzzer_prendido = True
                lastT = curT
            if mode == 1:
                mode1_2(leds)
            else:
                mode2_2(leds)

    else:
        sensor.wait_for_motion()
        alarma = True
        buzzer_prendido = True
        buzzer.on()