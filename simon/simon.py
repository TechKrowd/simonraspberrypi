import RPi.GPIO as GPIO
import random
import time

GREEN = 0
RED = 1
BLUE = 2
YELLOW = 3

LED_GREEN = 17
LED_RED = 27
LED_BLUE = 22
LED_YELLOW = 23

LEDS = [LED_GREEN, LED_RED, LED_BLUE, LED_YELLOW]

BTN_GREEN = 24
BTN_RED = 25
BTN_BLUE = 5
BTN_YELLOW = 6

BUTTONS = [BTN_GREEN, BTN_RED, BTN_BLUE, BTN_YELLOW]

SIZE = 4

ROUNDS = 20
sequence = list()
n = 0

def config():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    for i in range(SIZE):
        GPIO.setup(LEDS[i], GPIO.OUT)
        GPIO.setup(BUTTONS[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def randomSequence():
    sequence = list()
    for i in range(ROUNDS):
        aux = random.randint(0,SIZE-1)
        sequence.append(aux)
    return sequence, 1

def printLed(led):
    GPIO.output(led,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led,GPIO.LOW)

def printSequence(sequence, n):
    time.sleep(1)
    for i in range(n):
        printLed(LEDS[sequence[i]])
        print(sequence[i])
        time.sleep(1)

def main():
    global sequence
    global n
    try:
        #configuración
        config()
        #nueva secuencia
        sequence,n = randomSequence()
        n = 5
        printSequence (sequence, n)
    finally:
        GPIO.cleanup()

main()
