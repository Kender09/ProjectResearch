"""
This is the main application controller.
"""

import sys
import os

if __name__ == '__main__':
    sys.path.append('src')

    import urllib2
    import json
    import RPi.GPIO as GPIO
    import stepper_motor
    import LED
    import mysql.connector
#    import MySQLdb

    # config
    url = 'http://192.168.10.46:3000/api/users'
    mysql_cnx = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        db = 'pom_db',
        user = 'root',
        passwd = 'raspberry'
    )

    mysql_cur = mysql_cnx.cursor(buffered=True)
    sql = "SELECT * FROM pom_users"
    mysql_cur.execute(sql)
    rows = mysql_cur.fetchall()
    for row in rows:
            print(row)
    mysql_cur.close()
    mysql_cnx.close()

    GPIO.setmode(GPIO.BCM)
    led = LED.LEDController(GPIO, 17)
    mc = stepper_motor.MotorController(GPIO, 6, 13, 19, 26)
    fat_rate = 3
    """
    response = urllib2.urlopen(url)
    html = response.read()
    #print(html)

    json = json.loads(html)
    fat_rate = json[0]['fat_rate']
    print(fat_rate)
    """
    g1 = led.pikapika(2, 0.2)
    for g in g1:
        print g

    print 'input_rate: ',
    fat_rate = int(input())
    print 'input speed: ',
    spead = float(input())
    led.switchOn()
    mc.rotate(fat_rate,spead)
    led.switchOff()
    mc.GPIO.cleanup()

