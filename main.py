import RPi.GPIO as GPIO
from chassis import Chassis
from hardware.motor import Motor

chassis_system = None

def initSystems():
    chassis_system = Chassis(
        motor1=Motor(IN1=11, IN2=12, PWM=13, inverted=False),
        motor2=Motor(IN1=15, IN2=16, PWM=18, inverted=True),
        motor3=Motor(IN1=19, IN2=21, PWM=22, inverted=False),
        motor4=Motor(IN1=23, IN2=24, PWM=26, inverted=True)
    )

def start():
    pass

def update():
    pass