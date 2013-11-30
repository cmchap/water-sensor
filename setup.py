#!/usr/bin/python

import water_sensor_functions
import os

w = water_sensor_functions
value = 1
w.test_wet(value)
w.test_dry(value)


if max(w.wet_values) >= max(w.dry_values):
    while  max(w.wet_values) >= max(w.dry_values):
        print "Looks like your tests didn't get very good data because the dry resistance was lower than the wet resistance."
        print "Want to try again wtih more data points?"
        a = input("y/n")
        while  a != 'y' | 'Y' | 'n' | 'N':
            a = input("Please enter 'y' for yes or 'n' for no...")
        if a == 'y' | 'Y':
            num = input("You did "+value+" readings last time. How many do you want to do this time?")
            w.test_dry(value)
            w.test_wet(value)
        elif a ==  'n' | 'N':
            exit()
else:
    f = open('max_wet_resistance', 'w')
    s = str(max(w.wet_values))
    f.write(s)
    print "The important number is the last one, the highest dry resistance."
    print "I've saved that value to a file called max_wet_resistance.txt in this folder."
    b = input("Now that it's set up, would you like to start the water sensor now? \n y/n")
    while  b != 'y' | 'Y' | 'n' | 'N':
        a = input("Please enter 'y' for yes or 'n' for no...")
    if a == 'y' | 'Y':
        os.system("water_sensor.py")
    elif a ==  'n' | 'N':
        exit()