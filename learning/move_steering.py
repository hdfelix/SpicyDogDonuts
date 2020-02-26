#!/usr/bin/env python3

from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from time import sleep

# Demonstrate how to use MoveSteering class.
# Have the robot rotate 360 degrees on one wheel then the other
# Using the same four methods we are now familiar with:
# on(), on_for_degrees(), on_for_rotations(), on_for_seconds()

steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)

steering_drive.on(-100, 35)
sleep(2)
steering_drive.on(100, 35)
sleep(2)
steering_drive.stop()

# Store the value of 2 360 rotations in a variable
degrees = 360 * 2

# -100 = turn all the way to the left;
steering_drive.on_for_degrees(-100, 30, degrees)
# 100 = turn all the way to the right
steering_drive.on_for_degrees(100, 30, degrees)

steering_drive.on_for_rotations(-100, 30, 2)
steering_drive.on_for_rotations(100, 30, 2)