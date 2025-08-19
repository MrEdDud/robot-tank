from gpiozero import DigitalOutputDevice, PWMOutputDevice
import time

# --- Setup ---
A1 = DigitalOutputDevice(16, initial_value=False)
A2 = DigitalOutputDevice(18, initial_value=False)
PWMA = PWMOutputDevice(12, initial_value=0.0)

B1 = DigitalOutputDevice(15, initial_value=False)
B2 = DigitalOutputDevice(13, initial_value=False)
PWMB = PWMOutputDevice(11, initial_value=0.0)

try:
    for x in range(5):
        # --- Motor A forward ---
        A1.on(); A2.off(); PWMA.value = 0.6
        time.sleep(2)

        # --- Motor A backward ---
        A1.off(); A2.on(); PWMA.value = 0.6
        time.sleep(2)

        # --- Motor B forward ---
        B1.on(); B2.off(); PWMB.value = 0.6
        time.sleep(2)

        # --- Motor B backward ---
        B1.off(); B2.on(); PWMB.value = 0.6
        time.sleep(2)

        # --- Stop everything ---
        A1.off(); A2.off(); PWMA.value = 0.0
        B1.off(); B2.off(); PWMB.value = 0.0

finally:
    # --- Final stop on exit ---
    A1.off(); A2.off(); PWMA.value = 0.0
    B1.off(); B2.off(); PWMB.value = 0.0