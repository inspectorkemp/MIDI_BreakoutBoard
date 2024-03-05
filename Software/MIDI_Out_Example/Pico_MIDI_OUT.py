from machine import Pin, UART
import utime

# Define pin for the LED
LED_PIN = 25

# Define UART (MIDI)
uart = UART(0, baudrate=31250, tx=0, rx=1, txbuf=64, rxbuf=64)

# MIDI Program Change constants
PC_STATUS = 0xC0  # Program Change status byte

# Patch numbers for demonstration (change as needed)
PATCH_PIANO = 22
PATCH_TRUMPET = 24

def send_program_change(channel, program):
    midi_message = bytes([PC_STATUS | ((channel - 1) & 0x0F), program])
    uart.write(midi_message)

# Setup LED pin
led = Pin(LED_PIN, Pin.OUT)

# Function to perform patch change
def change_patch(patch_number, channel):
    send_program_change(channel, patch_number)
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

