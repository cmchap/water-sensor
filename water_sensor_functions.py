#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText
import RPi.GPIO as GPIO
import string
import time

# Function Definitions

#takes either "wet" or "dry" as the condition.
def email(condition):
    print "attempting to send email"
    From = 'corymchap@gmail.com'
    To  = 'corymchapman@gmail.com'
    Subject = 'Water_sensor is '+condition+'.'
    if condition == 'wet':
        Text = 'You should really get that fixed...'
    if condition == 'dry':
        Text = 'The sensor is dry again.' 
        
    Body = string.join((
        "From: %s" % From,
        "To: %s" % To,
        "Subject: %s" % Subject,
        "",
        Text,
        ), "\r\n")
    
    # Credentials (if needed)
    username = 'corymchap'
    password = 'Jsl5veMDO7op'
    
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    print "Logging in..."
    server.login(username,password)
    print "Logged in as "+username+"."
    server.sendmail(From, [To], Body)
    server.quit()
    print "Email sent."

#RCtime takes a BCM pin number, ex. 18 
def RCtime (RCpin):
    reading = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1) 
    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
    while True:
        if (GPIO.input(RCpin) == GPIO.LOW):
            reading += 1
        if reading >= 1000:
            return 0
        if (GPIO.input(RCpin) != GPIO.LOW):
            return 1

# Turns on the piezo buzzer 
# tested to work on pin 17
def buzz_on (pin):

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

# Turns off the piezo buzzer
# tested to work on pin 17
def buzz_off(pin):

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)