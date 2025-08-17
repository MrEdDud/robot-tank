from gpiozero import Motor, PWMOutputDevice, DigitalOutputDevice
import curses

# Standby
STBY = DigitalOutputDevice(22)
STBY.on()

class Vehicle:
    def __init__(self):
        # Motor A
        self.motor_a = Motor(forward=16, backward=18)
        self.pwm_a = PWMOutputDevice(12)  # PWMA
        self.pwm_a.value = 0

        # Motor B
        self.motor_b = Motor(forward=15, backward=13)
        self.pwm_b = PWMOutputDevice(11)  # PWMB
        self.pwm_b.value = 0

        self.speed = 0.5  # default speed

    def forward(self):
        self.motor_a.forward()
        self.motor_b.forward()
        self.pwm_a.value = self.speed
        self.pwm_b.value = self.speed

    def backward(self):
        self.motor_a.backward()
        self.motor_b.backward()
        self.pwm_a.value = self.speed
        self.pwm_b.value = self.speed

    def stop(self):
        self.motor_a.stop()
        self.motor_b.stop()
        self.pwm_a.value = 0
        self.pwm_b.value = 0

    def map_key_to_command(self, key):
        return {
            curses.KEY_UP: self.forward,
            curses.KEY_DOWN: self.backward,
        }.get(key)

    def control(self, key):
        action = self.map_key_to_command(key)
        if action:
            action()

rpi_vehicle = Vehicle()

def main(window):
    while True:
        curses.halfdelay(5)  # wait 0.5s per read
        key = window.getch()

        if key == 259:  # UP
            rpi_vehicle.forward()
        elif key == 258:  # DOWN
            rpi_vehicle.backward()
        else:
            rpi_vehicle.stop()

curses.wrapper(main)