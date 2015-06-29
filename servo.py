from Tkinter import *
import RPi.GPIO as GPIO
import time
import urllib2
import json
from pprint import pprint

"""
c = pycurl.Curl()
c.setopt( pycurl.URL, 'http://192.168.10.72:3000/api/users' )
c.setopt( pycurl.WRITEFUNCTION, write_data )
c.perform()
c.close()
body = write_data.getvalue()
print(body)
"""
response = urllib2.urlopen('http://192.168.10.72:3000/api/users')
html = response.read()
print(html)

json = json.loads(html)
fat_rate = json[0]['fat_rate']
pprint(json[0]['fat_rate'])

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
pwm = GPIO.PWM(17, 100)
pwm.start(5)

"""
for i in range(0, 2000):
	duty =(1.0 + ((90*i)%270)/180.0)/20.0*100.0
	pwm.ChangeDutyCycle(duty)
	time.sleep(1)
	print(i, ' : ', duty)
"""
while True:
    deg = int(input())
    duty = (1.0 + deg/180.0)/20.0*100.0
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    print fat_rate
    duty = (1.0 + fat_rate/180.0)/20.0*100.0
    pwm.ChangeDutyCycle(duty)

pwm.stop()
