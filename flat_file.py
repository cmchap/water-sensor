#!/usr/bin/python

#########
# About #
#########

# This script uses a Raspberry Pi to sense for the presence or absence of water.
# If there is water, an email is sent and a buzzer goes off.
# When it's dry again, another email is sent, and the buzzer turns off.

# To run this script at boot, edit /etc/rc.local to include (no quotes) 'sudo python <pathtoyourscript>.py'


###########
# License #
###########
# Released under the MIT license.

import config

########################################
# Gmail login credentials to send email#
########################################

username = config.config['username'] #you don't need the "@gmail.com" bit.
password = config.config['password']

############################
# General Email Parameters #
############################

From = config.config['From']
To =  config.config['To']

#######################################
# Email Parameters when sensor is Wet #
#######################################

Subject_wet = config.config['Subject_wet']
Body_wet = config.config['Body_wet']

#######################################
# Email Parameters when semsor is Dry #
#######################################

Subject_dry = config.config['Subject_dry']
Body_dry = config.config['Body_dry']

import smtplib
import RPi.GPIO as GPIO
import string
import time

# Function Definitions

#takes either "wet" or "dry" as the condition.
def email(condition):
    print "Attempting to send email"
    if condition == 'wet':
        Body = string.join((
        "From: %s" % From,
        "To: %s" % To,
        "Subject: %s" % Subject_wet,
        "",
        Body_wet,
        ), "\r\n")
    if condition == 'dry':
        Body = string.join((
            "From: %s" % From,
            "To: %s" % To,
            "Subject: %s" % Subject_dry,
            "",
            Body_dry,
            ), "\r\n")

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    print "Logging in..."
    server.login(username,password)
    print "Logged in as "+username+"."
    server.sendmail(From, [To], Body)
    server.quit()
    print "Email sent."

#Tests whether water is present.
# returns 0 for dry
# returns 1 for wet
# tested to work on pin 18
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

    p = GPIO.PWM(pin, 2300)
    p.start(50)
    for x in range(2300, 3300):
        p.ChangeFrequency(x)
        if x == 3300:
            x =2300

# Turns off the piezo buzzer
# tested to work on pin 17
def buzz_off(pin):

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Main Loop

print 'Waiting for wetness...'
while True:
    time.sleep(1)
    if RCtime(17) == 1:
        buzz_on(18)
        print "Sensor is wet"
        email('wet')
        print "Waiting for dryness..."
        while True:
            time.sleep(1)
            if RCtime(17) == 0:
                buzz_off(18)
                print "Sensor is dry again"
                email('dry')
                print "Waiting for wetness..."
                break
GPIO.cleanup()