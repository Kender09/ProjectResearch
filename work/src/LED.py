class LEDController:
    import time

    def __init__(self, GPIO, pin):
        self.GPIO = GPIO
        self.pin = pin
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setup(pin, self.GPIO.OUT)

    def switchOn(self):
        self.GPIO.output(self.pin, self.GPIO.HIGH)

    def switchOff(self):
        self.GPIO.output(self.pin, self.GPIO.LOW)

    def pikapika(self, time, interval):
        while True:
            if time <= 0.0:
                raise StopIteration
            self.GPIO.output(self.pin, self.GPIO.HIGH)
            self.time.sleep(interval)
            self.GPIO.output(self.pin, self.GPIO.LOW)
            self.time.sleep(interval)
            yield time
            time -= 0.1
