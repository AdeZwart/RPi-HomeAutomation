import RPi.GPIO as GPIO
import time
import datetime as dt
from random import randint

# Init the statics
GPIO_DOORBELL_PIN=16
BELL_PRESSED = 0

# Init GPIO for doorbell control
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_DOORBELL_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            
# Run the program loop
while 1:
    if GPIO.input(GPIO_DOORBELL_PIN):
        if (BELL_PRESSED == 0):
            print("Doorbell rings")
            BELL_PRESSED = 1
        else:   
            time.sleep(1)
    else:
        BELL_PRESSED = 0
        time.sleep(1)

# Cleanup the GPIO settings        
GPIO.cleanup()
