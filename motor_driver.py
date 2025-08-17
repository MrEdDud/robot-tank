from gpiozero import Motor, DigitalOutputDevice
import time

STBY = DigitalOutputDevice(22)
STBY.on()

motor_a = Motor(forward=16, backward=18)
motor_b = Motor(forward=15, backward=13)

# Test Motor A
print("Motor A forward")
motor_a.forward()
time.sleep(2)
motor_a.stop()

print("Motor A backward")
motor_a.backward()
time.sleep(2)
motor_a.stop()

# Test Motor B
print("Motor B forward")
motor_b.forward()
time.sleep(2)
motor_b.stop()

print("Motor B backward")
motor_b.backward()
time.sleep(2)
motor_b.stop()
