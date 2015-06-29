class MotorController:

    import time
    import RPi.GPIO as GPIO

    def __init__(self, pin1, pin2, pin3, pin4):
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setup(pin1, self.GPIO.OUT)
        self.GPIO.setup(pin2, self.GPIO.OUT)
        self.GPIO.setup(pin3, self.GPIO.OUT)
        self.GPIO.setup(pin4, self.GPIO.OUT)

    def swich_gpio(self, i):
        pin1 = self.pin1
        pin2 = self.pin2
        pin3 = self.pin3
        pin4 = self.pin4
        if i == 0:
            self.GPIO.output(pin1, self.GPIO.HIGH)
            self.GPIO.output(pin2, self.GPIO.HIGH)
            self.GPIO.output(pin3, self.GPIO.LOW)
            self.GPIO.output(pin4, self.GPIO.LOW)
        elif i == 1:
            self.GPIO.output(pin1, self.GPIO.LOW)
            self.GPIO.output(pin2, self.GPIO.HIGH)
            self.GPIO.output(pin3, self.GPIO.LOW)
            self.GPIO.output(pin4, self.GPIO.LOW)
        elif i == 2:
            self.GPIO.output(pin1, self.GPIO.LOW)
            self.GPIO.output(pin2, self.GPIO.HIGH)
            self.GPIO.output(pin3, self.GPIO.HIGH)
            self.GPIO.output(pin4, self.GPIO.LOW)
        elif i == 3:
            self.GPIO.output(pin1, self.GPIO.LOW)
            self.GPIO.output(pin2, self.GPIO.LOW)
            self.GPIO.output(pin3, self.GPIO.HIGH)
            self.GPIO.output(pin4, self.GPIO.LOW)
        elif i == 4:
            self.GPIO.output(pin1, self.GPIO.LOW)
            self.GPIO.output(pin2, self.GPIO.LOW)
            self.GPIO.output(pin3, self.GPIO.HIGH)
            self.GPIO.output(pin4, self.GPIO.HIGH)
        elif i == 5:
            self.GPIO.output(pin1, self.GPIO.LOW)
            self.GPIO.output(pin2, self.GPIO.LOW)
            self.GPIO.output(pin3, self.GPIO.LOW)
            self.GPIO.output(pin4, self.GPIO.HIGH)
        elif i == 6:
            self.GPIO.output(pin1, self.GPIO.HIGH)
            self.GPIO.output(pin2, self.GPIO.LOW)
            self.GPIO.output(pin3, self.GPIO.LOW)
            self.GPIO.output(pin4, self.GPIO.HIGH)
        elif i == 7:
            self.GPIO.output(pin1, self.GPIO.HIGH)
            self.GPIO.output(pin2, self.GPIO.LOW)
            self.GPIO.output(pin3, self.GPIO.LOW)
            self.GPIO.output(pin4, self.GPIO.LOW)

    #num 0 is false
    #spead 0.1 ~ 1.5
    def rotate(self, num, spead = 1):
        t = 0.001 / spead
        count = 0
        #1cycle 512 * 8
        step_num = abs(512 * 8 * num)
        while count < step_num:
            #if count % 100 == 0:
                #print (count*t)
            if num > 0:
                self.swich_gpio(count%8)
            else:
                self.swich_gpio((step_num-count)%8)
            self.time.sleep(t)
            count += 1


from Tkinter import *
import urllib2
import json
mc = MotorController(6, 13, 19, 26)
response = urllib2.urlopen('http://192.168.10.79:3000/api/users')
html = response.read()
#print(html)

json = json.loads(html)
fat_rate = json[0]['fat_rate']
print(fat_rate)
spead = float(input())
mc.rotate(fat_rate,spead)
mc.GPIO.cleanup()


