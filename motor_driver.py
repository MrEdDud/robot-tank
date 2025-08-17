from gpiozero import Motor, DigitalOutputDevice
import time

STBY = DigitalOutputDevice(22)
STBY.on()

# Motor A test
motor_a = Motor(forward=16, backward=18)
motor_a.forward()
time.sleep(2)
motor_a.backward()
time.sleep(2)
motor_a.stop()

# Motor B test
motor_b = Motor(forward=15, backward=13)
motor_b.forward()
time.sleep(2)
motor_b.backward()
time.sleep(2)
motor_b.stop()
