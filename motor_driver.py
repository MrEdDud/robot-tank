from gpiozero import DigitalOutputDevice, PWMOutputDevice, Device
from gpiozero.pins.rpigpio import RPiGPIOFactory
import atexit

Device.pin_factory = RPiGPIOFactory()

# BCM pins that correspond to your physical header wiring
A1  = DigitalOutputDevice(23, initial_value=False)  # phys 16
A2  = DigitalOutputDevice(24, initial_value=False)  # phys 18
PWMA = PWMOutputDevice(12, initial_value=0.0)       # phys 32

B1  = DigitalOutputDevice(22, initial_value=False)  # phys 15
B2  = DigitalOutputDevice(27, initial_value=False)  # phys 13
PWMB = PWMOutputDevice(13, initial_value=0.0)       # phys 33

try:
    def forward(speed=1):
        """Move the vehicle forward at a specified speed."""
        A1.on(); A2.off()
        B1.on(); B2.off()
        PWMA.value = speed
        PWMB.value = speed

    def reverse(speed=1):
        """Move the vehicle backward at a specified speed."""
        A1.off(); A2.on()
        B1.off(); B2.on()
        PWMA.value = speed
        PWMB.value = speed

    def left(speed=1):
        """Turn the vehicle left at a specified speed."""
        A1.off(); A2.on()
        B1.on(); B2.off()
        PWMA.value = speed
        PWMB.value = speed

    def right(speed=1):
        """Turn the vehicle right at a specified speed."""
        A1.on(); A2.off()
        B1.off(); B2.on()
        PWMA.value = speed
        PWMB.value = speed

    def stop():
        """Stop the vehicle."""
        A1.off(); A2.off()
        B1.off(); B2.off()
        PWMA.value = 0.0
        PWMB.value = 0.0
except:
    print("Error initializing motor driver. Ensure GPIO pins are correctly set up.")

def cleanup():
    """Cleanup GPIO settings."""
    A1.close()
    A2.close()
    PWMA.close()
    B1.close()
    B2.close()
    PWMB.close()

atexit.register(cleanup)  # Ensure motors stop on exit 