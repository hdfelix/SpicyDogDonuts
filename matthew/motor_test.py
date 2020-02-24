#!/usr/bin/env python3

# import needed ev3 modules
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C

# import the sleep method
from time import sleep

# Set a variable to run the robot with move tank
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)

# turn the motors on and run at the same speed
tank_pair.on(left_speed = 60, right_speed = 60)

# run for 3 seconds
sleep(3)

# turn left a bit
tank_pair.on(left_speed = 50, right_speed = 60)
sleep(1)

# turn right a bit
tank_pair.on(left_speed = 60, right_speed = 50)
sleep(1)

# twirl to the left
tank_pair.on(left_speed = 0, right_speed = 80)
sleep(3)

# twirl to the right
tank_pair.on(left_speed = 80, right_speed = 0)
sleep(3)

# slow down to 0 speed at short increments
tank_pair.on(left_speed = 50, right_speed = 50)
sleep(0.3)
tank_pair.on(left_speed = 40, right_speed = 40)
sleep(0.3)
tank_pair.on(left_speed = 30, right_speed = 30)
sleep(0.3)
tank_pair.on(left_speed = 20, right_speed = 20)
sleep(0.3)
tank_pair.on(left_speed = 10, right_speed = 10)
sleep(0.3)
tank_pair(left_speed = 0, right_speed = 0)

# turn off the motors
tank_pair.off
