from Tkinter import *
import RPi.GPIO as GPIO
import time
import urllib2
import json
from pprint import pprint

def swich_gpio(i, pin1, pin2, pin3, pin4, GPIO):
    if i == 0:
        GPIO.output(pin1, GPIO.HIGH)
        GPIO.output(pin2, GPIO.HIGH)
        GPIO.output(pin3, GPIO.LOW)
        GPIO.output(pin4, GPIO.LOW)
    elif i == 1:
        GPIO.output(pin1, GPIO.LOW)
        GPIO.output(pin2, GPIO.HIGH)
        GPIO.output(pin3, GPIO.LOW)
        GPIO.output(pin4, GPIO.LOW)
    elif i == 2:
        GPIO.output(pin1, GPIO.LOW)
        GPIO.output(pin2, GPIO.HIGH)
        GPIO.output(pin3, GPIO.HIGH)
        GPIO.output(pin4, GPIO.LOW)
    elif i == 3:
        GPIO.output(pin1, GPIO.LOW)
        GPIO.output(pin2, GPIO.LOW)
        GPIO.output(pin3, GPIO.HIGH)
        GPIO.output(pin4, GPIO.LOW)
    elif i == 4:
        GPIO.output(pin1, GPIO.LOW)
        GPIO.output(pin2, GPIO.LOW)
        GPIO.output(pin3, GPIO.HIGH)
        GPIO.output(pin4, GPIO.HIGH)
    elif i == 5:
        GPIO.output(pin1, GPIO.LOW)
        GPIO.output(pin2, GPIO.LOW)
        GPIO.output(pin3, GPIO.LOW)
        GPIO.output(pin4, GPIO.HIGH)
    elif i == 6:
        GPIO.output(pin1, GPIO.HIGH)
        GPIO.output(pin2, GPIO.LOW)
        GPIO.output(pin3, GPIO.LOW)
        GPIO.output(pin4, GPIO.HIGH)
    elif i == 7:
        GPIO.output(pin1, GPIO.HIGH)
        GPIO.output(pin2, GPIO.LOW)
        GPIO.output(pin3, GPIO.LOW)
        GPIO.output(pin4, GPIO.LOW)

"""
response = urllib2.urlopen('http://192.168.10.72:3000/api/users')
html = response.read()
print(html)

json = json.loads(html)
fat_rate = json[0]['fat_rate']
pprint(json[0]['fat_rate'])
"""

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT)
#pwm1 = GPIO.PWM(6, 100)
GPIO.setup(13, GPIO.OUT)
#pwm2 = GPIO.PWM(13, 100)
GPIO.setup(19, GPIO.OUT)
#pwm3 = GPIO.PWM(19, 100)
GPIO.setup(26, GPIO.OUT)
#pwm4 = GPIO.PWM(26, 100)

t = 0.001
count = 0
#1cycle 512 * 8
step_num = 512 * 8
while count < step_num:
    if count % 100 == 0:
        print (count*t)
    swich_gpio(count%8, 6, 13, 19, 26, GPIO)
    time.sleep(t)
    count += 1

GPIO.cleanup()
