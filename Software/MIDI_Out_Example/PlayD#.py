from machine import Pin, UART
import utime

# Define pin for the LED
LED_PIN = 25

# Define UART (MIDI)
uart = UART(0, baudrate=31250, tx=0, rx=1, txbuf=64, rxbuf=64)

# MIDI Note On and Note Off constants
NOTE_ON_STATUS = 0x90  # Note On status byte
NOTE_OFF_STATUS = 0x80  # Note Off status byte

# MIDI channel and note number for D#
MIDI_CHANNEL = 1
NOTE_D_SHARP = 63

def send_note_on(note, velocity):
    midi_message = bytes([NOTE_ON_STATUS | ((MIDI_CHANNEL - 1) & 0x0F), note, velocity])
    uart.write(midi_message)

def send_note_off(note):
    midi_message = bytes([NOTE_OFF_STATUS | ((MIDI_CHANNEL - 1) & 0x0F), note, 0])
    uart.write(midi_message)

# Setup LED pin
led = Pin(LED_PIN, Pin.OUT)

# Function to play a note and then stop
def play_note_and_stop(note, duration):
    send_note_on(note, 127)  # Note On with full velocity
    led.value(1)
    utime.sleep_ms(duration)
    
    send_note_off(note)
    led.value(0)
    utime.sleep_ms(100)  # Optional: brief pause after stopping the note

# Main setup
def setup():
    led.off()
    uart.init(31250, tx=0, rx=1)
    
# Main loop
def loop():
    # Play D# (Note number 63) for 10 seconds
    play_note_and_stop(NOTE_D_SHARP, 10000)

# Run setup
setup()

# Run loop
while True:
    loop()
