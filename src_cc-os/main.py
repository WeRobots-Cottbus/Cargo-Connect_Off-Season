#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from botconfig import *
from toolkit import *
from programs import prg1_1, prg1_2, prg2_1, prg2_2, prg3_1

prg_lst = [prg1_1, prg1_2, prg2_1, prg2_2, prg3_1]
prg_len = len(prg_lst)

def loop():
    prg_sel = 0
    while True:
        # select and run program
        if   Button.LEFT   in Brick.buttons.pressed(): prg_sel = (prg_sel - 1) % prg_len
        elif Button.RIGHT  in Brick.buttons.pressed(): prg_sel = (prg_sel + 1) % prg_len
        elif Button.CENTER in Brick.buttons.pressed(): prg_lst[prg_sel].run()

        # update display if any button is pressed
        if any(Brick.buttons.pressed()):
            DisplayText(prg_lst[prg_sel].PrgName, (5,7), True)

if __name__ == "__main__":
    loop()