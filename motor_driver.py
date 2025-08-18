rpi_vehicle = None
"""from gpiozero import DigitalOutputDevice, PWMOutputDevice
import time

# STBY — enable the driver
STBY = DigitalOutputDevice(22)
STBY.on()

# Motor A pins
A1 = DigitalOutputDevice(16)
A2 = DigitalOutputDevice(18)
PWMA = PWMOutputDevice(12)
PWMA.value = 1.0  # full speed

# Motor B pins
B1 = DigitalOutputDevice(15)
B2 = DigitalOutputDevice(13)
PWMB = PWMOutputDevice(11)
PWMB.value = 1.0  # full speed

def test_motor(forward_pin, backward_pin, motor_name):
    print(f"Testing {motor_name} forward")
    forward_pin.on()
    backward_pin.off()
    time.sleep(2)

    print(f"Testing {motor_name} backward")
    forward_pin.off()
    backward_pin.on()
    time.sleep(2)

    forward_pin.off()
    backward_pin.off()
    print(f"{motor_name} test complete\n")

while True:
    test_motor(A1, A2, "Motor A")
    test_motor(B1, B2, "Motor B")"""