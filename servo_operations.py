import RPi.GPIO as GPIO
import time

# GPIO setup
servo_pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Set PWM frequency to 50Hz (standard for servos)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)


def set_angle(angle):
    """Set servo to specific angle (0° to 180°)."""
    duty = 2 + (angle / 18)
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)
