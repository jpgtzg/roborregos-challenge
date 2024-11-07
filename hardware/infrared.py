import RPi.GPIO as GPIO
import time

class InfraredReceiver:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)
        self.pulse_times = []
        self.capture_started = False

    def capture_pulses(self, duration=0.1):
        """
        Capture pulse timings for a specified duration.
        This is useful to detect a complete IR signal pattern.
        """
        self.pulse_times = []
        self.capture_started = True
        start_time = time.time()

        while time.time() - start_time < duration:
            pulse_start = time.time()

            while GPIO.input(self.pin) == 1:
                if time.time() - start_time > duration:
                    self.capture_started = False
                    return self.pulse_times

            pulse_end = time.time()
            pulse_duration = pulse_end - pulse_start
            self.pulse_times.append(pulse_duration)

            while GPIO.input(self.pin) == 0:
                if time.time() - start_time > duration:
                    self.capture_started = False
                    return self.pulse_times

        self.capture_started = False
        return self.pulse_times

    def decode_signal(self):
        """
        Decode captured pulse times into a binary signal.
        This assumes a basic protocol where pulse lengths map to binary.
        """
        signal = []
        for pulse in self.pulse_times:
            if pulse < 0.0005: # 0.00065 0.00007
                signal.append(0)
            else:
                signal.append(1)
        return signal

    def cleanup(self):
        GPIO.cleanup()