import datetime
import time
import RPi.GPIO as GPIO

# use the Broadcom pin numbering scheme
GPIO.setmode(GPIO.BCM)

# set up the GPIO pin to control the LED (replace X with the appropriate pin number)
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

def set_led_state(state):
    # Turn the LED on or off
    GPIO.output(LED_PIN, state)

def read_last_number_from_file(filename):
    # Read the last number from a file
    # return the initial number (0001) if the file does not exist
    try:
        with open(filename, 'r') as f:
            # read the last line of the file
            last_line = f.readlines()[-1]
            # split the line on the tab character
            date_str, number_str = last_line.split('\t')
            # return the number as an integer
            return int(number_str)
    except FileNotFoundError:
        return 1

def write_number_to_file(filename, number_str, timestamp):
    # Write a number and timestamp to a file
    with open(filename, 'a') as f:
        # write the number and timestamp to the file
        f.write(f'{timestamp}\t{number_str}\n')

# read the last number from the file "number.txt"
last_number = read_last_number_from_file("number.txt")

# iterate through the numbers from last_number + 1 to 9999
for number in range(last_number + 1, 10000):
    # flash the LED for 1 second before starting a new number and also blink shortly to start input
