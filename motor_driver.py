from gpiozero import DigitalOutputDevice, PWMOutputDevice
import time

# BCM pins that correspond to your physical header wiring
A1  = DigitalOutputDevice(23, initial_value=False)  # phys 16
A2  = DigitalOutputDevice(24, initial_value=False)  # phys 18
PWMA = PWMOutputDevice(18, initial_value=0.0)       # phys 12

B1  = DigitalOutputDevice(22, initial_value=False)  # phys 15
B2  = DigitalOutputDevice(27, initial_value=False)  # phys 13
PWMB = PWMOutputDevice(17, initial_value=0.0)       # phys 11

try:
    print("=== Motor A forward ===")
    PWMA.value = 0.5
    A1.on(); A2.off()
    time.sleep(1.5)

    print("=== Motor A backward ===")
    A1.off(); A2.on()
    time.sleep(1.5)

    print("=== Stopping Motor A ===")
    PWMA.value = 0.0
    A1.off(); A2.off()
    time.sleep(1)

    print("=== Motor B forward ===")
    PWMB.value = 0.5
    B1.on(); B2.off()
    time.sleep(1.5)

    print("=== Motor B backward ===")
    B1.off(); B2.on()
    time.sleep(1.5)

    print("=== Stopping Motor B ===")
    PWMB.value = 0.0
    B1.off(); B2.off()

finally:
    print("=== Final cleanup: stopping all motors ===")
    PWMA.value = 0.0; A1.off(); A2.off()
    PWMB.value = 0.0; B1.off(); B2.off()