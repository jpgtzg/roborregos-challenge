from systems.chassis import Chassis
from systems.intake import Intake
from systems.ultrasonics import Ultrasonics
from hardware.motor import Motor
from hardware.ultrasonic import Ultrasonic
from constants import Constants

chassis_system = None
intake = None
ultrasonics = None

def initSystems():
    
    chassis_system = Chassis(
        motor1=Motor(IN1=Constants.ChassisConstants.MOTOR1_IN1, IN2=Constants.ChassisConstants.MOTOR1_IN2, PWM=Constants.ChassisConstants.MOTOR1_PWM, inverted=Constants.ChassisConstants.MOTOR1_INVERTED),
        motor2=Motor(IN1=Constants.ChassisConstants.MOTOR2_IN1, IN2=Constants.ChassisConstants.MOTOR2_IN2, PWM=Constants.ChassisConstants.MOTOR2_PWM, inverted=Constants.ChassisConstants.MOTOR2_INVERTED),
        motor3=Motor(IN1=Constants.ChassisConstants.MOTOR3_IN1, IN2=Constants.ChassisConstants.MOTOR3_IN2, PWM=Constants.ChassisConstants.MOTOR3_PWM, inverted=Constants.ChassisConstants.MOTOR3_INVERTED),
        motor4=Motor(IN1=Constants.ChassisConstants.MOTOR4_IN1, IN2=Constants.ChassisConstants.MOTOR4_IN2, PWM=Constants.ChassisConstants.MOTOR4_PWM, inverted=Constants.ChassisConstants.MOTOR4_INVERTED)
    )

    intake = Intake(
        left_motor=Motor(IN1=Constants.IntakeConstants.LEFTMOTOR_IN1, IN2=Constants.IntakeConstants.LEFTMOTOR_IN2, PWM=Constants.IntakeConstants.LEFTMOTOR_PWM, inverted=Constants.IntakeConstants.LEFTMOTOR_INVERTED),
        right_motor=Motor(IN1=Constants.IntakeConstants.RIGHTMOTOR_IN1, IN2=Constants.IntakeConstants.RIGHTMOTOR_IN2, PWM=Constants.IntakeConstants.RIGHTMOTOR_PWM, inverted=Constants.IntakeConstants.RIGHTMOTOR_INVERTED)
    )

    ultrasonics = Ultrasonics(
        ultrasonic1=Ultrasonic(trigger_pin=Constants.UltraSonicConstants.ULTRASONIC1_TRIG, echo_pin=Constants.UltraSonicConstants.ULTRASONIC1_ECHO),
        ultrasonic2=Ultrasonic(trigger_pin=Constants.UltraSonicConstants.ULTRASONIC2_TRIG, echo_pin=Constants.UltraSonicConstants.ULTRASONIC2_ECHO),
        ultrasonic3=Ultrasonic(trigger_pin=Constants.UltraSonicConstants.ULTRASONIC3_TRIG, echo_pin=Constants.UltraSonicConstants.ULTRASONIC3_ECHO)
    )
    
def start():
    pass

def update():
    pass