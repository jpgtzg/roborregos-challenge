from lib.system.system import System
from hardware.infrared import InfraredReceiver

class Infrareds(System):
    
        def __init__(self, infrared: InfraredReceiver, infrared2: InfraredReceiver, infrared3: InfraredReceiver, infrared4: InfraredReceiver):
            super().__init__("Infrared System")
            self.infrared = infrared
            self.infrared2 = infrared
    
        def start(self):
            pass
    
        def update(self):
            pass
    
        def get_distance(self) -> int:
            return self.infrared.get_distance()
    
        def get_angle(self) -> int:
            return self.infrared.get_angle()