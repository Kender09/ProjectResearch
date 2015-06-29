#! /usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # use GPIO Number

SV1 =12
GPIO.setup(SV1, GPIO.OUT)

servo = GPIO.PWM(SV1, 50) # set 20 ms / 50 Hz

angle = 0.0 # set angle
new_duty =(1.0 + angle/180.0)/20.0*100.0 # calculate duty
print(new_duty)
servo.start(new_duty)
print("angle 0 deg")
time.sleep(0.5)

angle = 90.0 # set angle
new_duty =(1.0 + angle/180.0)/20.0*100.0 # calculate duty
print(new_duty)
servo.ChangeDutyCycle(new_duty)
print("angle 90 deg")
time.sleep(0.5)

angle = 180.0 # set angle
new_duty =(1.0 + angle/180.0)/20.0*100.0 # calculate duty
print(new_duty)
servo.ChangeDutyCycle(new_duty)
print("angle 180 deg")
time.sleep(0.5)

angle = 0.0 # set angle
new_duty =(1.0 + angle/180.0)/20.0*100.0 # calculate duty
print(new_duty)
servo.start(new_duty)
print("angle 0 deg")
time.sleep(0.5)

servo.stop() # stop servo
