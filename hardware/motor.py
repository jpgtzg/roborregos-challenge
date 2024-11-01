import RPi.GPIO as GPIO

class Motor:

    def __init__(self, IN1, IN2, PWM, inverted):
        self.inverted = inverted
        self.IN1 = IN1
        self.IN2 = IN2
        self.PWM = PWM

        # Set up GPIO mode and warnings
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        # Initialize the motor control pins
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)

        # Initialize PWM pin if provided
        if self.PWM is not None:
            GPIO.setup(self.PWM, GPIO.OUT)
            self.pwm = GPIO.PWM(self.PWM, 100)  # PWM frequency 100 Hz
            self.pwm.start(0)  # Start with 0% duty cycle (motor off)

    def move_motor(self, angularVelocity: float):
        control = abs(angularVelocity)
        control = max(0, min(control, 100))  # Clamp between 0 and 100

        if control == 0:
            self.stop()  # Stop if the control signal is 0
        else:
            if self.inverted:
                GPIO.output(self.IN1, GPIO.LOW if angularVelocity < 0 else GPIO.HIGH)
                GPIO.output(self.IN2, GPIO.HIGH if angularVelocity < 0 else GPIO.LOW)
            else:
                GPIO.output(self.IN1, GPIO.HIGH if angularVelocity < 0 else GPIO.LOW)
                GPIO.output(self.IN2, GPIO.LOW if angularVelocity < 0 else GPIO.HIGH)

            self.pwm.ChangeDutyCycle(control)

    def simple_move(self, speed: float):
        if speed == 0:
            self.stop()
            return

        if speed < 0:
            GPIO.output(self.IN1, GPIO.LOW)
            GPIO.output(self.IN2, GPIO.HIGH)
        else:
            GPIO.output(self.IN1, GPIO.HIGH)
            GPIO.output(self.IN2, GPIO.LOW)
        
        if self.PWM is not None:
            self.pwm.ChangeDutyCycle(abs(speed))

    def stop(self):
        if self.PWM is not None:
            self.pwm.ChangeDutyCycle(0)
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)

    def invert(self):
        self.inverted = not self.inverted

    def getSpeed(self):
        # Assuming this is where you want to get the last set duty cycle
        return self.pwm.duty_cycle if self.PWM is not None else 0

    def cleanup(self):
        """Release resources and cleanup GPIO."""
        self.stop()
        if self.PWM is not None:
            self.pwm.stop()
        GPIO.cleanup([self.IN1, self.IN2] + ([self.PWM] if self.PWM is not None else []))
