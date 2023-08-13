# This script creates square waves using a raspberry pi
# using the GPIO pins which are connected to the oscilloscope
# via a breadboard. The GPIO pins are connected to the breadboard
# via a ribbon cable. The breadboard is connected to the oscilloscope
# via a BNC cable.
# The GPIO pins are connected to the breadboard as follows:
# GPIO 17 -> Breadboard pin 1
# GPIO 27 -> Breadboard pin 2
# GPIO 22 -> Breadboard pin 3
# GPIO 23 -> Breadboard pin 4
# GPIO 24 -> Breadboard pin 5
# GPIO 25 -> Breadboard pin 6
# GPIO 5V -> Breadboard pin 7
# GPIO GND -> Breadboard pin 8
# The breadboard is connected to the oscilloscope as follows:
# Breadboard pin 1 -> Oscilloscope channel 1
# Breadboard pin 2 -> Oscilloscope channel 2

import RPi.GPIO as GPIO
import time

# Set the GPIO pin numbering mode
GPIO.setmode(GPIO.BCM)

# Ignore warnings
GPIO.setwarnings(False)

# Set the GPIO pins to output mode
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

# Ask the user for the frequency of the square wave
frequency = float(input("Enter the frequency of the square wave: "))
# Ask the user for the duty cycle of the square wave
duty_cycle = float(input("Enter the duty cycle of the square wave: "))
# # Ask the user for the duration of the square wave
# duration = float(input("Enter the duration of the square wave: "))
# Ask the user for the number of cycles of the square wave
cycles = int(input("Enter the number of cycles of the square wave: "))
# Calculate the period of the square wave
period = 1 / frequency
# Calculate the time the square wave is on
on_time = period * duty_cycle
# Calculate the time the square wave is off
off_time = period - on_time

# Print the frequency, duty cycle, duration and number of cycles
print("Frequency: " + str(frequency) + " Hz")
print("Duty cycle: " + str(duty_cycle) + " %")
# print("Duration: " + str(duration) + " s")
print("Number of cycles: " + str(cycles))

# Record the start time
start_time = time.time()

# Loop for the number of cycles
for i in range(cycles):
    # Set the GPIO pins to high
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(25, GPIO.HIGH)
    # Wait for the on time
    time.sleep(on_time)
    # Set the GPIO pins to low
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    # Wait for the off time
    time.sleep(off_time)

# Record the end time
end_time = time.time()

# Calculate the duration of the square wave
duration = end_time - start_time

# Print the duration of the square wave
print("Duration: " + str(duration) + " s")

# Reset the GPIO pins
GPIO.cleanup()

# Ask user if they want to run the script again
run_again = input("Run again? (y/n): ")

# If the user wants to run the script again
if run_again == "y":
    # Run the script again
    exec(open("oscilloscope.py").read())

# If the user does not want to run the script again
elif run_again == "n":
    # End the program
    print("End of program")

# End of program
