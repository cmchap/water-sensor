#!/usr/bin/python

import water_sensor_functions, time

w = water_sensor_functions

# Main Loop

print 'Waiting for wetness...'
while True:
    time.sleep(1)
    if w.RCtime(17) == 1:
        w.buzz_on(18)
        print "Sensor is wet"
        w.email('wet')
        print "Waiting for dryness..."
        while True:
            time.sleep(1)
            if w.RCtime(17) == 0:
                w.buzz_off(18)
                print "Sensor is dry again"
                w.email('dry')
                print "Waiting for wetness..."
                break