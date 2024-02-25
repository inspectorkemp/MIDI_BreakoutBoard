from machine import Pin, UART
import utime

# Define pin for the LED
LED_PIN = 25

# Define UART (MIDI)
uart = UART(0, baudrate=31250, tx=0, rx=1, txbuf=64, rxbuf=64)

# MIDI control change constants
CC_PATCH_CHANGE = 0xB0  # Control Change status byte
CC_PATCH_NUMBER = 0    # Control Change number for patch change

# Patch numbers for demonstration (change as needed)
PATCH_PIANO = 0
PATCH_TRUMPET = 56

def send_control_change(channel, control, value):
    midi_message = bytes([CC_PATCH_CHANGE | (channel & 0x0F), control, value])
    uart.write(midi_message)

# Setup LED pin
led = Pin(LED_PIN, Pin.OUT)

# Function to perform patch change
def change_patch(patch_number, channel):
    send_control_change(channel, CC_PATCH_NUMBER, patch_number)
    led.value(1)
    utime.sleep_ms(1000)
    
    led.value(0)
    utime.sleep_ms(100)

# Main setup
def setup():
    led.off()
    uart.init(31250, tx=0, rx=1)
    
# Main loop
def loop():
    change_patch(PATCH_PIANO, 1)
    change_patch(PATCH_TRUMPET, 1)

# Run setup
setup()

# Run loop
while True:
    loop()
