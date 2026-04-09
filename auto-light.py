import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26

GPIO.setup(led, GPIO.OUT)

divisioner = 6
state = 0

GPIO.setup(divisioner, GPIO.IN)

while True:
    if GPIO.input(divisioner):
        state = not state
        GPIO.output(led, state)
        GPIO.output(led, state)

    else:
        GPIO.output(led, state)
