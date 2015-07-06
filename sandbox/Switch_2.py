#! /usr/bin/env python

import RPi.GPIO as GPIO
import time

from Switch_2_1 import *

#if __name__ ==("__main__"):
#start

GPIO.setmode(GPIO.BCM) # use GPIO Number

LED1 = 5 # LED1 --> GPIO5
led_init(LED1)

SW1 = 26 # SW1 --> GPIO26
GPIO.setup(SW1, GPIO.IN) # set GPIO25 input

for i in range(50):
	print(i)

	on_off = GPIO.input(SW1) # read SW1

	if on_off == GPIO.LOW:
		led_on(LED1)

	else:
		led_off(LED1)
	print(on_off)

	time.sleep(0.2)

