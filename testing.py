import water_sensor_functions as w
import RPi.GPIO as GPIO
import time

# Turns on the piezo buzzer 
# tested to work on pin 18 for PWM
def buzz_on (pin):

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    
    freq = 5
    duty_cycle = 100
    
    p = GPIO.PWM(pin, freq)
    p.start(duty_cycle)
    
    while True:
        freq = raw_input("Set the frequency")
        p.ChangeFrequency(freq)
        if freq == 999:
            GPIO.cleanup()
            break
            
# Turns off the piezo buzzer
# tested to work on pin 18 for PWM

#GPIO.output(18, GPIO.LOW)
buzz_on(18)
