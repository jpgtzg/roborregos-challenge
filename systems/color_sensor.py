from lib.system.system import System
from hardware.color_sensor import ColorSensorTCS34725

class ColorSensor(System):

    def __init__(self, color_sensor: ColorSensorTCS34725):
        super().__init__("Color Sensor System")
        self.color_sensor = color_sensor

    def start(self):
        pass

    def update(self):
        pass

    def get_color(self):
        return self.color_sensor.read_rgbc()