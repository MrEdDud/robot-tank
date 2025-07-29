from gpiozero import PWMOutputDevice, DigitalOutputDevice
from time import sleep

# Motor A pins (left)
AIN1 = DigitalOutputDevice(16)
AIN2 = DigitalOutputDevice(18)
PWMA = PWMOutputDevice(12)

# Motor B pins (right)
BIN1 = DigitalOutputDevice(15)
BIN2 = DigitalOutputDevice(13)
PWMB = PWMOutputDevice(11)

# Standby pin
STBY = DigitalOutputDevice(22)

# Enable motors (set STBY high)
STBY.on()

def run_motor(motor, speed, direction):
    if direction == 0:
        in1_state = True
        in2_state = False
    else:
        in1_state = False
        in2_state = True

    if motor == 0:
        AIN1.value = in1_state
        AIN2.value = in2_state
        PWMA.value = speed / 100  # gpiozero expects a float between 0.0 and 1.0
    elif motor == 1:
        BIN1.value = in1_state
        BIN2.value = in2_state
        PWMB.value = speed / 100

def forward(spd):
    run_motor(0, spd, 0)
    run_motor(1, spd, 0)

def reverse(spd):
    run_motor(0, spd, 1)
    run_motor(1, spd, 1)

def turn_left(spd):
    run_motor(0, spd, 0)
    run_motor(1, spd, 1)

def turn_right(spd):
    run_motor(0, spd, 1)
    run_motor(1, spd, 0)

def motor_stop():
    PWMA.value = 0
    PWMB.value = 0
    AIN1.off()
    AIN2.off()
    BIN1.off()
    BIN2.off()
    STBY.off()

# Main test loop
def main(args=None):
    try: 
        while True:
            forward(50)
            sleep(2)
            motor_stop()
            sleep(0.25)

            reverse(50)
            sleep(2)
            motor_stop()
            sleep(0.25)

            turn_left(50)
            sleep(2)
            motor_stop()
            sleep(0.25)

            turn_right(50)
            sleep(2)
            motor_stop()
            sleep(2)
    except KeyboardInterrupt:
        motor_stop()  # Ensure motors are stopped on exit