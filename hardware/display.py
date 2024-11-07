import smbus
import time

class LCDDisplay():
    LCD_CHR = 1  
    LCD_CMD = 0  

    LCD_LINE_1 = 0x80 
    LCD_LINE_2 = 0xC0 

    LCD_BACKLIGHT = 0x08 
    ENABLE = 0b00000100 

    E_PULSE = 0.0005
    E_DELAY = 0.0005

    def __init__(self, i2c_addr=0x27):
        self.i2c_addr = i2c_addr
        self.bus = smbus.SMBus(1) 
        self._lcd_byte(0x33, self.LCD_CMD)
        self._lcd_byte(0x32, self.LCD_CMD)
        self._lcd_byte(0x06, self.LCD_CMD)
        self._lcd_byte(0x0C, self.LCD_CMD)
        self._lcd_byte(0x28, self.LCD_CMD)
        self._lcd_byte(0x01, self.LCD_CMD)
        time.sleep(self.E_DELAY)
        super.__init__("Display")

    def _lcd_byte(self, bits, mode):
        # High bits
        high_bits = mode | (bits & 0xF0) | self.LCD_BACKLIGHT
        low_bits = mode | ((bits << 4) & 0xF0) | self.LCD_BACKLIGHT

        # Write to LCD
        self.bus.write_byte(self.i2c_addr, high_bits)
        self._lcd_toggle_enable(high_bits)
        self.bus.write_byte(self.i2c_addr, low_bits)
        self._lcd_toggle_enable(low_bits)

    def _lcd_toggle_enable(self, bits):
        """Toggle enable."""
        time.sleep(self.E_DELAY)
        self.bus.write_byte(self.i2c_addr, (bits | self.ENABLE))
        time.sleep(self.E_PULSE)
        self.bus.write_byte(self.i2c_addr, (bits & ~self.ENABLE))
        time.sleep(self.E_DELAY)

    def display_string(self, message, line):
        """Display a string on a specific line of the LCD."""
        message = message.ljust(16)
        if line == 1:
            self._lcd_byte(self.LCD_LINE_1, self.LCD_CMD)
        elif line == 2:
            self._lcd_byte(self.LCD_LINE_2, self.LCD_CMD)
        else:
            raise ValueError("Line number must be 1 or 2")

        for char in message:
            self._lcd_byte(ord(char), self.LCD_CHR)

    def clear(self):
        """Clear the LCD display."""
        self._lcd_byte(0x01, self.LCD_CMD)
        time.sleep(self.E_DELAY)