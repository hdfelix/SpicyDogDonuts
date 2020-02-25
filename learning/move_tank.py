#!/usr/bin/env python3

from ev3dev2.motor import SpeedPercent, OUTPUT_B, OUTPUT_C
from time import sleep

# Test motor movement with the MoveTank module
from ev3dev2.motor import MoveTank


# setting a variable for the robot with MoveTank class
# setting the left and right motor ports (B and C)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

# you can drive with tank using the same four methods we used for
# the separate large motors:

# on()
tank_drive.on(30, 30)
sleep(2)
tank_drive.off()
sleep(0.5)

tank_drive.on(-30, -30)
sleep(2)
tank_drive.stop()
sleep(0.5)

# on_for_seconds()
tank_drive.on_for_seconds(30, 30, 2)
sleep(0.5)

tank_drive.on_for_seconds(-30, -30, 2)
sleep(0.5)

# on_for_rotations()
tank_drive.on_for_rotations(30, 30, 2)
sleep(0.5)

tank_drive.on_for_rotations(-30, -30, 2)
sleep(0.5)

# on_for_degrees()
tank_drive.on_for_degrees(50, 50 (360 * 2))
sleep(0.5)

tank_drive.on_for_degrees(-50, -50, (360 * 2))
sleep(0.5)
