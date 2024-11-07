import smbus
import time
import math

class NavX:
    def __init__(self, bus_number=1, device_address=0x3C):
        """
        Initialize the NavX I2C connection.
        
        :param bus_number: The I2C bus to use (usually 1 on Raspberry Pi)
        :param device_address: The I2C address of the NavX device (default is 0x3C)
        """
        self.bus = smbus.SMBus(bus_number)
        self.device_address = device_address
        
        # Initialize NavX
        self.initialize_navx()

    def initialize_navx(self):
        """
        Initialize the NavX device, setting the necessary settings.
        """
        self.write_register(0x3D, 0x01) 

    def read_register(self, register):
        """
        Read a single byte from a register.
        
        :param register: Register address to read from.
        :return: The byte read from the register.
        """
        return self.bus.read_byte_data(self.device_address, register)

    def write_register(self, register, value):
        """
        Write a single byte to a register.
        
        :param register: Register address to write to.
        :param value: The value to write to the register.
        """
        self.bus.write_byte_data(self.device_address, register, value)

    def get_angle(self):
        """
        Retrieve the angle (yaw) from the NavX.
        
        :return: The yaw angle in degrees.
        """
        high_byte = self.read_register(0x1E)
        low_byte = self.read_register(0x1F) 
        angle = (high_byte << 8) | low_byte 
        return angle

    def get_acceleration(self):
        """
        Retrieve the acceleration data from the NavX (X, Y, Z axes).
        
        :return: Tuple of (X, Y, Z) accelerometer values.
        """
        x_accel = self.read_register(0x32)
        y_accel = self.read_register(0x34)
        z_accel = self.read_register(0x36)
        return (x_accel, y_accel, z_accel)

    def get_gyro(self):
        """
        Retrieve the gyroscope data from the NavX (X, Y, Z axes).
        
        :return: Tuple of (X, Y, Z) gyroscope values.
        """
        x_gyro = self.read_register(0x52)
        y_gyro = self.read_register(0x54)
        z_gyro = self.read_register(0x56)
        return (x_gyro, y_gyro, z_gyro)

    def get_magnetometer(self):
        """
        Retrieve the magnetometer data from the NavX (X, Y, Z axes).
        
        :return: Tuple of (X, Y, Z) magnetometer values.
        """
        x_mag = self.read_register(0x64)
        y_mag = self.read_register(0x66)
        z_mag = self.read_register(0x68)
        return (x_mag, y_mag, z_mag)

    def get_all_sensors(self):
        """
        Retrieve all sensor data (yaw, acceleration, gyroscope, magnetometer).
        
        :return: A dictionary containing all sensor data.
        """
        return {
            'angle': self.get_angle(),
            'acceleration': self.get_acceleration(),
            'gyro': self.get_gyro(),
            'magnetometer': self.get_magnetometer()
        }
    
    def get_pitch(self):
        """
        Retrieve the pitch (forward tilt) of the robot using accelerometer data.
        
        :return: The pitch angle in degrees.
        """
        # Read accelerometer data for X, Y, Z axes
        x_accel, y_accel, z_accel = self.get_acceleration()

        # Calculate pitch using the accelerometer data
        pitch = math.atan2(x_accel, math.sqrt(y_accel**2 + z_accel**2))

        # Convert pitch from radians to degrees
        pitch_degrees = math.degrees(pitch)

        return pitch_degrees


    def cleanup(self):
        self.bus.close()