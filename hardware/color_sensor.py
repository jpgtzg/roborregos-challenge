import smbus
import time

class ColorSensorTCS34725:
    ADDRESS = 0x29
    COMMAND_BIT = 0x80
    ENABLE = 0x00
    ENABLE_AEN = 0x02
    ENABLE_PON = 0x01
    ATIME = 0x01
    CONTROL = 0x0F
    ID = 0x12
    CDATA = 0x14
    RDATA = 0x16
    GDATA = 0x18  
    BDATA = 0x1A  

    # Integration time (2.4ms increments)
    INTEGRATION_TIME = 0xF6  # Set to 24ms for example

    def __init__(self, i2c_addr=ADDRESS, integration_time=INTEGRATION_TIME, gain=0x01):
        self.i2c_addr = i2c_addr
        self.bus = smbus.SMBus(1) 
        self.integration_time = integration_time
        self.gain = gain
        self._initialize_sensor()

    def _initialize_sensor(self):
        """Initialize the TCS34725 sensor."""
        self._write_byte(self.ENABLE, self.ENABLE_PON)

        # Needed for system to wake up
        time.sleep(0.003) 
        self._write_byte(self.ENABLE, self.ENABLE_PON | self.ENABLE_AEN)


        self._write_byte(self.ATIME, self.integration_time)
        self._write_byte(self.CONTROL, self.gain)

    def _write_byte(self, reg, value):
        """Write a byte to a given register."""
        self.bus.write_byte_data(self.i2c_addr, self.COMMAND_BIT | reg, value)

    def _read_word(self, reg):
        """Read a 2-byte word from a given register."""
        data = self.bus.read_i2c_block_data(self.i2c_addr, self.COMMAND_BIT | reg, 2)
        return data[1] << 8 | data[0]

    def read_rgbc(self):
        """Read the RGB and Clear data."""
        red = self._read_word(self.RDATA)
        green = self._read_word(self.GDATA)
        blue = self._read_word(self.BDATA)
        clear = self._read_word(self.CDATA)
        return red, green, blue, clear