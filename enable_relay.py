import RPi.GPIO as GPIO
import time

pin_number=32

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_number, GPIO.OUT)

GPIO.output(pin_number, GPIO.HIGH)
