#!/usr/bin/env python3

# Importing the B and C inputs, and the SpeedPercent from the motor module in the ev3dev2 library
from ev3dev2.motor import LargeMotor, SpeedPercent, OUTPUT_B, OUTPUT_C
# Importing the sleep() class from the time module
from time import sleep

# Moving the right large motor
# Set a variable for your left large motor, connected to port B
l_motor = LargeMotor(OUTPUT_B)

# Set a variable for your right large motor, connected to port C 
r_motor = LargeMotor(OUTPUT_C)

# 1. Move the motor with on() and sleep() methods
#    a. turning it on at speed 70
#    b. telling the robot to wait 1 second
#    c. turning the robot off
l_motor.on(70)
sleep(1)
l_motor.off()

r_motor.on(70)
sleep(1)
r_motor.off()

# 2. Move the motors with the on_for_seconds() method
#    - Speed 70% for 1 second 
r_motor.on_for_seconds(SpeedPercent(70), 1)
l_motor.on_for_seconds(SpeedPercent(70), 1)

# 3. Move the motors with the on_for_rotations() method
#    - Speed 70% for 2 wheel rotations
l_motor.on_for_rotations(SpeedPercent(70), 2)
r_motor.on_for_rotations(SpeedPercent(70), 2)

# 3. Move the motors with the on_for_degrees() method
#    - Speed 70% 2 times 360 degrees (1 wheel rotation)
r_motor.on_for_degrees(SpeedPercent(70), (360*2))
l_motor.on_for_degrees(SpeedPercent(70), (360*2))
