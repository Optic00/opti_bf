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
    set_led_state(True)
    time.sleep(1)
    set_led_state(False)
    time.sleep(1)
    set_led_state(True)
    time.sleep(0.5)
    set_led_state(False)
    time.sleep(0.5)
    # convert the number to a string and pad it with leading zeros
    number_str = format(number, '04d')

    # iterate through the digits of the number
    for digit in number_str:
        # convert the digit to an integer
        digit_int = int(digit)

        # blink the LED for the appropriate number of times
        for i in range(digit_int):
            # turn the LED on
            set_led_state(True)
            # wait for 200ms
            time.sleep(0.1)
            # turn the LED off
            set_led_state(False)
            # wait for 200ms
            time.sleep(0.1)

        # pause for 1 second between digits
        time.sleep(4.0)
        
    # output the number to the console
    print(number_str)
    # write the number to the file "number.txt" with the current date and time
    write_number_to_file("number.txt", number_str, datetime.datetime.now())

# clean up the GPIO resources
GPIO.cleanup()
