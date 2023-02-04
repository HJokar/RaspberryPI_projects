import RPi.GPIO as GPIO
import time

LEDpin=4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDpin,GPIO.OUT)

while True:
    user_input = input("Input value 0 or 1: ")
    print(user_input)

    if user_input == "1":
        GPIO.output(LEDpin,1)
        time.sleep(1)
    else:
        GPIO.output(LEDpin,0)
        time.sleep(1)
