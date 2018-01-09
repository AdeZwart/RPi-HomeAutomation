import RPi.GPIO as GPIO
import time
import datetime as dt
from random import randint

# Init the statics
GPIO_SERVO_PIN=11
CAT_CONTROL_START_TIME=dt.time(6, 0, 0, 0)
CAT_CONTROL_END_TIME=dt.time(23, 0, 0, 0)

# Init GPIO for servo control
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_SERVO_PIN, GPIO.OUT)
pwm=GPIO.PWM(GPIO_SERVO_PIN,50)

# Init the global cat door variables
isDoorInOpen=True
isDoorOutOpen=True
isCatInDoor=True

# private functions
def OpenCatDoorIn(canCatComeIn):
    # If the door status not equals the required status
    if isDoorInOpen != canCatComeIn:

        if canCatComeIn:
            # open the cat door for coming in
            isDoorInOpen = True

        else:

            # Never close the cat door if the cat != indoor
            if isCatInDoor:

                # close the cat door for coming in
                isDoorInOpen = False

def OpenCatDoorOut(canCatGoOut):
    # If the door status not equals the required status
    if isDoorOutOpen != canCatGoOut:

        if canCatGoOut:
            # open the cat door for going out
            isDoorOutOpen = True

        else:
            # close the cat door for going out
            isDoorOutOpen = False
            
# public functions
def AddMinutes(tm, mins):
    fulldate = tm + dt.timedelta(seconds=mins)
    return fulldate

def TimeDiff(tm1, tm2):
    timeDiff = tm1 - tm2
    return timeDiff.total_seconds()

def Rotate():
    pwm.start(5)
    #time.sleep(0.475)
    #time.sleep(0.225)
    time.sleep(1)
    pwm.stop()

def CatDoorOpen():
    OpenCatDoorIn(True)
    OpenCatDoorOut(True)

def CatDoorInOnly():
    OpenCatDoorIn(True)
    OpenCatDoorOut(False)

# Can't imagine why you would want this
def CatDoorOutOnly():
    OpenCatDoorIn(False)
    OpenCatDoorOut(True)
    
def CatDoorClose(catIsIndoor):
    OpenCatDoorIn(False)
    OpenCatDoorOut(False)

# Init the feeding variables    
lastFed=dt.datetime.now()
nextFeed=AddMinutes(lastFed, 1)
endFeeding=AddMinutes(lastFed, 5)

# Run the infinite loop
while True:
    if dt.datetime.now() > nextFeed:
        print ('feeding time!')
        Rotate()
        lastFed = dt.datetime.now()
        r = 10 #randint(30, 180)
        nextFeed=AddMinutes(lastFed, r)
        print ('Next feed @ %s' %nextFeed.isoformat())
#    elif dt.datetime.now() > endFeeding:
#        print ('I\'m done feeding')
#        break
    else:
        print ('Next feed in %s seconds' %TimeDiff(nextFeed, dt.datetime.now()))
        time.sleep(5)

# Cleanup the GPIO settings        
GPIO.cleanup()
