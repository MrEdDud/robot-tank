from gpiozero import DigitalOutputDevice, PWMOutputDevice
import time

# --- Setup ---
STBY = DigitalOutputDevice(22)  # standby
A1 = DigitalOutputDevice(16)    # Motor A direction
A2 = DigitalOutputDevice(18)
PWMA = PWMOutputDevice(12)      # Motor A speed (PWM)

B1 = DigitalOutputDevice(15)    # Motor B direction
B2 = DigitalOutputDevice(13)
PWMB = PWMOutputDevice(11)      # Motor B speed (PWM)

# --- Enable driver ---
STBY.on()

# --- Motor A forward ---
A1.on()
A2.off()
PWMA.value = 0.6   # 60% speed
time.sleep(2)

# --- Motor A backward ---
A1.off()
A2.on()
PWMA.value = 0.6
time.sleep(2)

# --- Motor B forward ---
B1.on()
B2.off()
PWMB.value = 0.6
time.sleep(2)

# --- Motor B backward ---
B1.off()
B2.on()
PWMB.value = 0.6
time.sleep(2)

# --- Stop everything ---
A1.off()
A2.off()
PWMA.value = 0

B1.off()
B2.off()
PWMB.value = 0

STBY.off()