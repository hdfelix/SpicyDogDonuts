#!/usr/bin/env python3

from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from time import sleep
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
tank_pair.on(left_speed=50, right_speed=50)
sleep(8)
tank_pair.on(left_speed=-5, right_speed=-5)
sleep(0.5)
tank_pair.on(left_speed=-10, right_speed=-10)
sleep(0.5)
tank_pair.on(left_speed=-30, right_speed=-25)
sleep(1)
tank_pair.on(left_speed=-35, right_speed=-40)
sleep(1)
tank_pair.on(left_speed=-50, right_speed=-50)
sleep(6.5)
tank_pair.off()