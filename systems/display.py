from lib.system.system import System
from hardware.display import LCDDisplay
import smbus
import time

class Display(System):


    def __init__(self, display: LCDDisplay):
        super.__init__("Display System")
        self.display = display

    def start(self):
        pass

    def update(self):
        pass

    def display_string(self, message: str):
        self.display.display_string(message)
        pass
