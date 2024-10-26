import RPi.GPIO as GPIO

class Motor:

    def __init__(self, IN1, IN2, PWM, inverted):
        self.inverted = inverted

        self.IN1 = IN1
        self.IN2 = IN2
        self.PWM = PWM

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        # Setting GPIO pins for all motors pins
        GPIO.setup(self.IN1, GPIO.OUT) 
        GPIO.setup(self.IN2, GPIO.OUT) 
        GPIO.setup(self.PWM, GPIO.OUT) 

        # Starting PWM 
        self.pwm : GPIO.PWM = GPIO.PWM(self.PWM, 100)
        self.pwm.start(0)        

    def moveMotor(self, angularVelocity : float):
        control = abs(angularVelocity)
        control = max(0, min(control, 100))

        if control == 0:
            self.pwm.ChangeDutyCycle(0)  # Stop the motor
        else:
            if self.inverted:
                GPIO.output(self.IN1, GPIO.LOW if angularVelocity < 0 else GPIO.HIGH)
                GPIO.output(self.IN2, GPIO.HIGH if angularVelocity < 0 else GPIO.LOW)
            else:
                GPIO.output(self.IN1, GPIO.HIGH if angularVelocity < 0 else GPIO.LOW)
                GPIO.output(self.IN2, GPIO.LOW if angularVelocity < 0 else GPIO.HIGH)

        self.pwm.ChangeDutyCycle(control)

    def stop(self):
        self.pwm.ChangeDutyCycle(0)
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
    
    def invert(self):
        self.inverted = not self.inverted

    def getSpeed(self):
        return self.pwm.ChangeDutyCycle(0) # TODO SET THIS TO THE REAL VALUE