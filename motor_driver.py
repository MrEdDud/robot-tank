from gpiozero import PWMOutputDevice, DigitalOutputDevice
import atexit  # for cleanup on exit

# Pins as BCM numbers (physical pin -> BCM)
PWMA = PWMOutputDevice(18)     # physical pin 12, PWM pin for speed
AIN1 = DigitalOutputDevice(23) # physical pin 16, direction control 1
AIN2 = DigitalOutputDevice(24) # physical pin 18, direction control 2
STBY = DigitalOutputDevice(25) # physical pin 22, standby pin

def enable_motor():
    STBY.on()

def disable_motor():
    STBY.off()

def forward(speed=1.0):
    enable_motor()
    AIN1.on()
    AIN2.off()
    PWMA.value = speed  # 0.0 to 1.0 for PWM speed control

def reverse(speed=1.0):
    enable_motor()
    AIN1.off()
    AIN2.on()
    PWMA.value = speed

def turn_left(speed=1.0):
    # If you have a second motor, you would control it here.
    # For single motor demo, just reverse as a placeholder
    reverse(speed)

def turn_right(speed=1.0):
    # For single motor demo, just forward as placeholder
    forward(speed)

def motor_stop():
    PWMA.value = 0
    AIN1.off()
    AIN2.off()
    disable_motor()

# Cleanup function to stop the motor when program exits
def cleanup():
    motor_stop()

# Register cleanup to run on program exit
atexit.register(cleanup)