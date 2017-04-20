import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(6, GPIO.OUT)

GPIO.output(6, GPIO.HIGH)

GPIO.cleanup()
