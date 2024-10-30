import RPi.GPIO as GPIO
import time

class Ultrasonic:
    def __init__(self, trigger_pin, echo_pin) :
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def get_distance(self) -> float:
        GPIO.output(self.trigger_pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, GPIO.LOW)

        pulse_start = time.time()
        pulse_end = time.time()

        while GPIO.input(self.echo_pin) == 0:
            pulse_start = time.time()

        while GPIO.input(self.echo_pin) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = (pulse_duration * 34300) / 2
        return round(distance, 2)
 