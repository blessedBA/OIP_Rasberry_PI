import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

button_up = 9   #gpio of up button 
button_down = 10 #similarly

GPIO.setup(button_up, GPIO.IN)
GPIO.setup(button_down, GPIO.IN)

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

while True:
    if GPIO.input(button_up) > 0 and GPIO.input(button_down) > 0:
        GPIO.output(leds, 256)
        print("double click!!!\n")
        time.sleep(sleep_time * 2)
        continue
    if GPIO.input(button_up) > 0:
        num += 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(button_down) > 0:
        num -= 1
        if num < 0:
            print("negative value!!!")
            num += 1
            continue
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    GPIO.output(leds, dec2bin(num))
