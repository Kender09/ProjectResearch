#! /usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # use GPIO Number

LED1 = 5 # LED1 --> GPIO5
GPIO.setup(LED1, GPIO.OUT) # set GPIO5 output

GPIO.output(LED1, GPIO.HIGH) # LED1 ON

time.sleep(3)

GPIO.output(LED1, GPIO.LOW) # LED1 OFF

GPIO.cleanup()
