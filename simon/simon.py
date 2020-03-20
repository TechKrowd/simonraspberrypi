import RPi.GPIO as GPIO

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

def config():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    for i in range(SIZE):
        GPIO.setup(LEDS[i], GPIO.OUT)
        GPIO.setup(BUTTONS[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
def main():
    try:
        #configuración
        config()
    finally:
        GPIO.cleanup()

main()
