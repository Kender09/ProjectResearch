#! /usr/bin/env python

import RPi.GPIO as GPIO
import time

def led_init(leds):
	GPIO.setup(leds, GPIO.OUT) # set GPIO leds output

def led_on(leds):
	GPIO.output(leds, GPIO.HIGH) # leds ON

def led_off(leds):
	GPIO.output(leds, GPIO.LOW) # leds OFF

if __name__ ==("__main__"):
#start

	GPIO.setmode(GPIO.BCM) # use GPIO Number

	LED1 = 5 # LED1 --> GPIO5
	led_init(LED1)

	LED2 = 6 # LED1 --> GPIO6
	led_init(LED2)

for i in range(10):
	print(i)
	led_on(LED1)
	led_on(LED2)
	time.sleep(0.5)

	led_off(LED1)
	led_off(LED2)
	time.sleep(0.5)

GPIO.cleanup()
print("led2b done")
